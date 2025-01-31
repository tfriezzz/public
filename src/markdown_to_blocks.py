from enum import Enum
import re
from markdown_parser import *
from htmlnode import *
from textnode import *
from text_to_textnodes import *

"""class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
        # Other block types..."""


def markdown_to_blocks(markdown):
    blocks = list(map(str.strip, (markdown.split("\n\n"))))
    return blocks


def unordered_list_checker(block):
    lines = block.split("\n")
    for line in lines:
        if not re.match(r"^(\* |- )", line.strip()):
            return None
    return "unordered_list"


def ordered_list_checker(block):
    sub_blocks = list(map(str.strip, (block.split("\n"))))
    blocks = [
        bool(re.match(r"^\d+\.\s.+", block, re.MULTILINE)) for block in sub_blocks
    ]
    if all(blocks):
        return "ordered_list"


def block_to_block_type(block):
    if block.startswith("```") and block.endswith("```"):
        return "code"
    elif re.match(r"^#{1,6}\s\w+", block):
        return "heading"
    elif all(re.match(r"^>\s*.+", line) for line in block.split("\n")):
        return "quote"
    elif block.startswith("* ") or block.startswith("- "):
        return unordered_list_checker(block)
    elif block.startswith("1. "):
        return ordered_list_checker(block)
    else:
        return "paragraph"


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        # print(f"DEBUG child:{text_node}")
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    parent_node = ParentNode("div", [])
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type is None:
            raise ValueError(f"Invalid block type for block: {block}")
        match block_type:
            case "paragraph":
                children = text_to_children(block)
                paragraph_node = ParentNode("p", children)
                parent_node.children.append(paragraph_node)
            case "heading":
                level = 0
                for char in block:
                    if char == "#":
                        level += 1
                    else:
                        break
                if level + 1 >= len(block):
                    raise ValueError(f"Invalid heading level: {level}")
                text = block[level + 1 :]
                children = text_to_children(text)
                tag = f"h{level}"
                heading_node = ParentNode(tag, children)
                parent_node.children.append(heading_node)
            case "code":
                code_content = block[3:-3].strip()
                code_text = LeafNode("code", code_content)
                pre_node = ParentNode("pre", [code_text])
                parent_node.children.append(pre_node)
            case "quote":
                children = text_to_children(block[2:])  # Fix optional space
                quote_node = ParentNode("blockquote", children)
                parent_node.children.append(quote_node)
            case "unordered_list":
                items = block.split("\n")
                html_items = []
                for item in items:
                    text = (item[1:]).lstrip()
                    children = text_to_children(text)
                    html_items.append(ParentNode("li", children))
                unordered_list_node = ParentNode("ul", html_items)
                parent_node.children.append(unordered_list_node)
            case "ordered_list":
                items = block.split("\n")
                html_items = []
                for item in items:
                    text = item[3:]
                    children = text_to_children(text)
                    html_items.append(ParentNode("li", children))
                ordered_list_node = ParentNode("ol", html_items)
                parent_node.children.append(ordered_list_node)
            case _:
                raise ValueError("Invalid block type")
    return parent_node


def extract_title(markdown):
    pattern = r"^#\s+(.+)$"
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if re.match(pattern, block):
            return block[2:]
