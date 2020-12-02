#!/usr/bin/env bash

main() {
    strand="$1"
    declare -A strand_types=( [A]=0 [C]=0 [G]=0 [T]=0 )

    for ((i = 0; i < "${#strand}"; i++)); do
        if [[ ! ${strand:$i:1} =~ [ACGT] ]]; then
            echo "Invalid nucleotide in strand"
            exit 1
        fi
        ((strand_types["${strand:$i:1}"]+=1))
    done

    for entry in A C G T; do
        echo "${entry}: ${strand_types[$entry]}"
    done
}

main "$@"
