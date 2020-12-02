#!/usr/bin/env bash

main() {
    (($#)) || exit 0

    num=$1
    local result=()
    local reversed=0

    ((num & 1)) && result+=("wink")
    ((num & 2)) && result+=("double blink")
    ((num & 4)) && result+=("close your eyes")
    ((num & 8)) && result+=("jump")
    ((num & 16)) && reversed=1

    local reversed_result=()
    if (($reversed)); then
	for ((i = ${#result[@]} - 1; i >= 0; i--)); do
	    reversed_result+=("${result[i]}")
	done
	result_str="$(printf ",%s" "${reversed_result[@]}")"
    else
	result_str="$(printf ",%s" "${result[@]}")"
    fi

    echo "${result_str#,}"
}

main "$@"
