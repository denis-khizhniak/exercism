#!/usr/bin/env bash

main() {
    local str="$1"

    ### using awk
    # echo "$str" | awk -F'[- ]' '{ for (i = 1; i <= NF; i++)\
    # { if (match($i, "[A-Za-z]", m)) printf toupper(substr(m[0],1,1)); } }'

    ### plain bash
    # replace dash character with space to treat as separate words
    local mod_str=${str/-/ }

    # clean extra characters from the string except and create array of words
    local mod_str_arr=(${mod_str//[^[:alpha:] ]})

    local result=""
    for word in "${mod_str_arr[@]}"; do
        chr=${word:0:1}
        result+=${chr^}
    done

    echo $result
}

main "$@"
