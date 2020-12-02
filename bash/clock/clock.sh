#!/usr/bin/env bash

main() {
    local hours=${1:-0}
    local minutes=${2:-0}
    local sign=${3:-""}
    local delta=${4:-0}

    if (($# < 2 || $# > 4 || $# == 3)) ||
        ! [[ "$1" =~ [0-9]+ && "$2" =~ [0-9]+ && "$4" =~ [0-9]* ]] ||
        # can't get working regex for +,- or empty, for ex. "$3" =~ [+-]* is not working
        ! [[ "$3" == "+" || "$3" == "-" || -z "$3" ]]; then
        echo "invalid arguments"
        exit 1
    fi

    minutes=$((minutes + ${sign}${delta}))
    hours=$(((24 + hours % 24 + minutes / 60 % 24 - (minutes % 60 < 0 ? 1 : 0)) % 24))
    minutes=$(((60 + minutes % 60) % 60))

    printf "%02d:%02d" $hours $minutes
}

main "$@"
