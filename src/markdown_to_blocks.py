from enum import Enum
import re
from markdown_parser import *
from htmlnode import *
from textnode import *

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
        # Other block types...

def markdown_to_blocks(markdown):
    blocks = list(map(str.strip, (markdown.split("\n\n"))))
    return blocks


def unordered_list_checker(block):
    sub_blocks = markdown_to_blocks(block)
    for block in sub_blocks:
        if re.match(r"^(\* |- )\w+", block, re.MULTILINE):
            return "unordered_list"


def ordered_list_checker(block):
    sub_blocks = list(map(str.strip, (block.split("\n"))))
    blocks = [bool(re.match(r"^\d+\.\s.+", block, re.MULTILINE)) for block in sub_blocks]
    if all(blocks):
        return "ordered_list"


def block_to_block_type(block):
    match block:
        case _ if re.match(r"^```.*```$", block, re.DOTALL):
            return "code"
            
        case _ if re.match(r"^#{1,6}\s\w+", block):
            return "heading"
        
        case _ if re.match(r"^>\w+", block):
            return "quote"

        case _ if block[0:2] == "* " or block[0:2] == "- ":
            return unordered_list_checker(block)

        case _ if block[0:3] == "1. ":
            return ordered_list_checker(block)

        case _:
            print(f"block: {block}, type: paragraph")
            return "paragraph"


