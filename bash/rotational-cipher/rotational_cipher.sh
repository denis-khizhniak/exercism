#!/usr/bin/env bash

index_of() {
    local value="$1"

    shift
    local arr=("$@")

    # find the first occurrence of value in the array and exit
    for i in "${!arr[@]}"; do
        if [[ "${arr[i]}" == "$value" ]]; then
            echo "$i"
            exit 0
        fi
    done

    # print -1 if not found
    echo -1
}

main() {
    local key="$1"
    local rot="$2"

    local alphabet=({a..z} {A..Z})

    local result=
    for ((i = 0; i < ${#key}; i++)); do
        idx=$(index_of "${key:i:1}" "${alphabet[@]}")

        if (( $idx >= 0 )); then
            # calculate rot index
            rot_idx=$(((idx + rot % 26) % 26 + idx / 26 * 26))
            result+="${alphabet[rot_idx]}"
        else
            result+="${key:i:1}"
        fi
    done

    echo "$result"
}

main "$@"
