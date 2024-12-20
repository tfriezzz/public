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


def block_to_block_type(block):
    match block:
        case _ if re.match(r"^```.*```$", block, re.DOTALL):
            return "code"
            
        case _ if re.match(r"^#{1,6}\s\w+", block):
            return "heading"
        
        case _ if re.match(r"^>\w+", block):
            return "quote"

        case _ if re.match(r"^(\* |- )\w+", block, re.MULTILINE):
            return "unordered_list"

        case _:
            print(f"block: {block}, type: paragraph")
            return "paragraph"


