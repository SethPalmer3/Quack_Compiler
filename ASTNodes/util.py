import logging

logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


ZERO_SPACE_CHAR = '\u200B'
TAB_CHAR = '  '
LB = "{"
RB = "}"

MR = {}


def flatten(m: list):
    """Flatten nested lists into a single level of list"""
    flat = []
    for item in m:
        if isinstance(item, list):
            flat += flatten(item)
        else:
            flat.append(item)
    return flat

def append_zero_size_char(input: str) -> str:
    mod_str = input
    i = 0
    while i < mod_str.__len__() - 1:
        if mod_str[i] == '\u200B' and mod_str[i+1] != '\u200B':
            first_half = mod_str[0:i+1]
            second_half = mod_str[i+1:]
            mod_str = first_half + '\u200B' + second_half
            i += 1
        i += 1
    return mod_str

def remove_zero_size_char(input: str) -> str:
    return input.replace('\u200B', '')

