#!/usr/bin/env bash

main () {
    [[ ${#@} > 1 ]] && {
        echo "Usage: error_handling.sh <person>"
            exit 1
        }

    [ -z ${1+x} ] && {
        echo "Usage: error_handling.sh <person>"
            exit 1
        }

    echo "Hello, $1"
}

main "$@"
