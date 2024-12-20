import unittest
from markdown_to_blocks import *

class TestMarkDownToBlock(unittest.TestCase):
    def simple_markdown_test(self):
        markdown = """# This is a heading

        This is a paragraph of text. It has some **bold** and *italic* words inside of it.

        * This is the first list item in a list block
        * This is a list item
        * This is another list item"""
        blocks = markdown_to_blocks(markdown)

        self.assertEqual(len(blocks), 3)
        self.assertEqual(blocks[0], "# This is a heading")
        self.assertEqual(blocks[1], "This is a paragraph of text. It has some **bold** and *italic* words inside of it.")
        self.assertEqual(blocks[2], "* This is the first list item in a list block\n* This is a list item\n* This is another list item")


class TestBlockToBlockType(unittest.TestCase):
    def test_paragraph(self):
        block = "This is a paragraph"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, "paragraph")

    def test_headline(self):
        block = "# This is a heading"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, "heading")

    def test_code(self):
        block = "```This is a code```"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, "code")

    def test_quote(self):
        block = ">This is a quote"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, "quote")

    def test_unordered_list(self):
        block = "* This is a unordered list"
        block_2 = "- This is also an unordered list"
        block_type = block_to_block_type(block)
        block_type_2 = block_to_block_type(block_2)
        self.assertEqual(block_type, "unordered_list")
        self.assertEqual(block_type_2, "unordered_list")
