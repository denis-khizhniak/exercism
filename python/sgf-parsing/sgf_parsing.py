import re


class SgfTree:
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for k, v in self.properties.items():
            if k not in other.properties:
                return False
            if other.properties[k] != v:
                return False
        for k in other.properties.keys():
            if k not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for a, b in zip(self.children, other.children):
            if a != b:
                return False
        return True

    def __ne__(self, other):
        return not self == other


def parse(input_string):

    # separate a validation part from the recursive part
    # as we are validating the whole string in one shot

    # validate input_string to comply with SGF format
    def validate_str(input_string):

        # raise exception if input string is empty
        if len(input_string) == 0:
            raise ValueError("Input string is not a valid SGF!")

        # check non empty input string
        check_str = input_string
        while len(check_str) > 0:
            common_re = r"\((;([A-Z]+\[(\\\]|[^();]+)\])*)+\)"
            if re.search(common_re, check_str):
                check_str = re.sub(common_re, "", check_str)
            else:
                raise ValueError("Input string is not a valid SGF!")

    # recursively parse the input string
    def recursive_parse(input_string):
        # initialize empty properties and children's list
        properties = {}
        children = []

        # decompose next properties block until ";", "(" or <end of string>
        props_m = re.match(r"\(?;([^();]+)(?:\(|\)|;|$)", input_string)
        if props_m:
            props_str = props_m.group(1)

            # replace "\\]" with "]" for parameters block given the correct string after validation
            # replace "\t" with space
            props_str = props_str.replace("\\]", "]")
            props_str = props_str.replace("\t", " ")

            props_pairs_lst = re.findall(r"\w+(?:\[[^();]+?\](?!]))+", props_str)
            for props_pair_str in props_pairs_lst:
                props_lst = re.findall(r"\w+|(?<=\[)[^();]+(?=\])", props_pair_str)
                properties[props_lst[0]] = props_lst[1:]

            border_char_idx = props_m.end() - 1
            if input_string[border_char_idx] == ";":
                # if stopped at ";" pass the rest of the input_stringing to recursion
                children.append(recursive_parse(input_string[border_char_idx:]))
            elif input_string[border_char_idx] == "(":
                # if stopped at "(" iterate through subtrees (children) inside the brackets
                for subtree in re.findall(r"\(;.+?(?:\(.+?\))?\)", input_string[border_char_idx:]):
                    children.append(recursive_parse(subtree))

        return SgfTree(properties, children)

    validate_str(input_string)

    return recursive_parse(input_string)
