#!/usr/bin/env bash

rhyme=("the house that Jack built"
    "the malt\nthat lay in"
    "the rat\nthat ate"
    "the cat\nthat killed"
    "the dog\nthat worried"
    "the cow with the crumpled horn\nthat tossed"
    "the maiden all forlorn\nthat milked"
    "the man all tattered and torn\nthat kissed"
    "the priest all shaven and shorn\nthat married"
    "the rooster that crowed in the morn\nthat woke"
    "the farmer sowing his corn\nthat kept"
    "the horse and the hound and the horn\nthat belonged to"
)

recite_rhyme() {
    local verse=$1
    local iter=$2

    ! (($iter)) && local text="This is" || local text=""

    printf "${text} ${rhyme[verse - 1]}"
    [[ "$verse" == 1 ]] && printf "." || recite_rhyme $(($verse - 1)) $((++i))
}

main() {
    local start_verse=$1
    local end_verse=$2

    if ! (((start_verse >= 1 && start_verse <= 12)) \
        && ((end_verse >= 1 && end_verse <= 12)))
    then
        echo "Verse number is invalid!"
        exit 1
    fi

    for i in $(seq $start_verse $end_verse); do
        recite_rhyme $i 0
        echo -e "\n"
    done
}

main "$@"
