#!/usr/bin/env bash

main() {
    ! (($#)) && exit 0

    for ((i=2; i<=${#@}; i++)); do
        echo "For want of a ${@:i-1:1} the ${@:i:1} was lost."
    done
    
    echo "And all for the want of a $1."
}

main "$@"
