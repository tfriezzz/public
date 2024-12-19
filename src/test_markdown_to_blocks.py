import unittest
from markdown_to_blocks import *

class TestMarkDownToBlock(unittest.TestCase):
    def simple_markdown_test(self):
        markdown = """# This is a heading

        This is a paragraph of text. It has some **bold** and *italic* words inside of it.

        * This is the first list item in a list block
        * This is a list item
        * This is another list item"""
        blocks = markdown_to_block(markdown)

        self.assertEqual(len(blocks), 3)
        self.assertEqual(blocks[0], "# This is a heading")
        self.assertEqual(blocks[1], "This is a paragraph of text. It has some **bold** and *italic* words inside of it.")
        self.assertEqual(blocks[2], "* This is the first list item in a list block\n* This is a list item\n* This is another list item")
