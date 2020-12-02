#!/usr/bin/env bash

main() {
    (($#)) || exit 0
    local n=$1

    # no primes under 2
    ((n < 2)) && exit 0

    # initialize array for all not multiples by default (=0)
    for i in $(seq 2 $n); do
        local numbers_list+=([$i]=0)
    done

    for ((p = 2; p <= n; p++)); do
        for ((m = 2; m * p <= n; m++)); do
            numbers_list[m * p]=1
        done
    done

    local result=()
    for num in ${!numbers_list[@]}; do
        ((${numbers_list[num]})) || result+=($num)
    done
    echo "${result[@]}"
}

main "$@"
