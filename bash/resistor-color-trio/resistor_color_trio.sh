#!/usr/bin/env bash

declare -A bands=([black]=0
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
    res=(${bands[$1]} ${bands[$2]})
    if [[ ${#res[@]} < 2 ]]; then
        echo "Invalid color specified"
        exit 1
    fi

    zeros=${bands[$3]}
    units="ohms"

    # compose number from resistors
    number=$(printf "%d" ${res[0]} ${res[1]})

    # remove leading zeros
    number=$(echo $number | sed -E 's/0*([0-9]+)/\1/g')

    # get the right order of magnitude
    number=$((number * 10 ** $zeros))

    # calculate the number of "000" in the number for units magnitude
    for ((i = 0; number % 1000 == 0 && number > 0; number = number / 1000)); do
        ((i++))
    done

    # put proper units
    case $i in
    1) units="kilo$units" ;;
    2) units="mega$units" ;;
    3) units="giga$units" ;;
    esac

    echo "$number $units"
}

main "$@"
