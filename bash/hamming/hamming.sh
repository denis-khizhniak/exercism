#!/usr/bin/env bash

main() {
    strand1="$1"
    strand2="$2"

    # check the input
    if [[ ${#@} != 2 ]]; then
        echo "Usage: hamming.sh <string1> <string2>"
        exit 1
    fi

    # check that both strands are of equal size
    if [[ ${#strand1} != ${#strand2} ]]; then
        echo "left and right strands must be of equal length"
        exit 1
    fi

    cnt=0
    for ((i = 0; i <= ${#strand1}; i++)); do
        [[ "${strand1:$i:1}" != "${strand2:$i:1}" ]] && ((cnt++))
    done

    echo $cnt
}

main "$@"
