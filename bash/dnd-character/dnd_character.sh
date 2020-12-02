#!/usr/bin/env bash

modifier() {
    echo $(($1 - 10 < 0 ? ($1 - 11) / 2 : ($1 - 10) / 2))
}

generate() {
    declare -i local dices_number=4

    declare -i local min
    declare -i local sum

    declare -i local mod
    declare -i local hitpoints

    local abilities=(strength dexterity constitution intelligence wisdom charisma)

    for ability in "${abilities[@]}"; do
        sum=0
        unset min
        # roll dices
        for ((i = 0; i < $dices_number; i++)); do
            dice=$(($RANDOM % 6 + 1))
            ((sum += $dice))
            ((${min:=$dice} > dice)) && min=$dice
        done
        echo "$ability $((sum -= min))"
    done

    mod=$(modifier ${abilities[constitution]})
    hitpoints=$((10 + mod))
    echo "hitpoints $hitpoints"
}

main() {
    ! (($#)) && { echo "arguments are incorrect"; exit 1; }

    local func="$1"
    local arg="$2"

    $func "$arg"
}

main "$@"
