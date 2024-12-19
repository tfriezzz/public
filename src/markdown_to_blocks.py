from markdown_parser import *
from htmlnode import *
from textnode import *


def markdown_to_blocks(markdown):
    block = list(map(str.strip, (markdown.split("\n\n"))))
    return block


markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""

#print(f"test: {markdown}")

#print(markdown_to_blocks(markdown))
for block in markdown_to_blocks(markdown):
    print(block)
