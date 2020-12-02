#!/usr/bin/env bash

main() {
    year="$1"

    [ "$#" -ne 1 ] && echo "Usage: leap.sh <year>" >&2 && exit 1
    ! [[ $year =~ ^[0-9]+$ ]] && echo "Usage: leap.sh <year>" >&2 && exit 1

    [ $((year % 400 )) -eq 0 ] && echo "true" && exit 0
    [ $((year % 100)) -eq 0 ] && echo "false" && exit 0
    ([ $((year % 4)) -eq 0 ] && echo "true" || echo "false") && exit 0
}

main "$@"
