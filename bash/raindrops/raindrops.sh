#!/usr/bin/env bash

main() {
    str=""
    number="$1"

    (( $number%3 == 0 )) && str+="Pling"
    (( $number%5 == 0 )) && str+="Plang"
    (( $number%7 == 0 )) && str+="Plong"

    [[ -z $str ]] && echo "$number" || echo "$str"
}

main "$@"
