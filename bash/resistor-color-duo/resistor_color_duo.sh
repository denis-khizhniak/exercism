#!/usr/bin/env bash

declare -A band_colors=(
    [black]=0
    [brown]=1
    [red]=2
    [orange]=3
    [yellow]=4
    [green]=5
    [blue]=6
    [violet]=7
    [grey]=8
    [white]=9
)


main() {
    i=0
    for param in "$@"; do
        if [ -z ${band_colors[$param]+"check"} ]; then
            echo "invalid color"
        fi

        printf "%s" "${band_colors[$param]}"
        if [[ $i == 1 ]]; then
            break
        else
            (( i++ ))
        fi
    done
}

main "$@"
