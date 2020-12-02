#!/usr/bin/env bash

declare -A brackets_assoc=([")"]="(" ["}"]="{" ["]"]="[")

main() {
    local brackets_str="$1"
    local opened_brackets=""

    for ((i = 0; i < ${#brackets_str}; i++)); do
        bracket=${brackets_str:$i:1}

        # skip everything that is not a bracket
        [[ ! "(){}[]" =~ "$bracket" ]] && continue

        # collect if open bracket encountered
        if [[ ! ${!brackets_assoc[@]} =~ $bracket ]]; then
            opened_brackets+=$bracket
        # remove matching open bracket if closing bracket encountered
        else 
            # save length of opened brackets array and compare
            # if remains the same after removal than it's an error (nonmatching brackets)
            len_opened_brackets=${#opened_brackets}
            ! (($len_opened_brackets)) && echo "false" && exit 0
            opened_brackets=${opened_brackets%${brackets_assoc[$bracket]}}
            [[ $len_opened_brackets == ${#opened_brackets} ]] && echo "false" && exit 0
        fi
    done

    ! ((${#opened_brackets})) && echo "true" || echo "false"
}

main "$@"
