#!/usr/bin/env bash

main() {
    string="$1"

    for (( i=${#string}; i>0; i-- )); do
        reversed_string+=${string:$i-1:1}
    done

    echo "$reversed_string"
}

main "$@"
