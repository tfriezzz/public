import unittest
from markdown_to_blocks import *
from markdown_parser import *

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
        block = "* This is an unordered list\n* Next line"
        block_2 = "- This is also an unordered list\n Next line"
        block_type = block_to_block_type(block)
        block_type_2 = block_to_block_type(block_2)
        self.assertEqual(block_type, "unordered_list")
        self.assertEqual(block_type_2, "unordered_list")


    def test_ordered_list(self):
        block = "1. This is a simple ordered list"
        block_2 = "1. This is a multiline ordered list\n1. Next line"
        block_type = block_to_block_type(block)
        block_type_2 = block_to_block_type(block_2)
        self.assertEqual(block_type, "ordered_list")
        self.assertEqual(block_type_2, "ordered_list")


class TestMarkdownToHTML(unittest.TestCase):
    def test_paragraph(self):
        node = markdown_to_html_node("This is a paragraph")
        self.assertEqual(node.to_html(), "<div><p>This is a paragraph</p></div>")
    

    def test_heading(self):
        node = markdown_to_html_node("# Heading")
        self.assertEqual(node.to_html(), "<div><h1>Heading</h1></div>")


    def test_code(self):
        node = markdown_to_html_node("```Code```")
        self.assertEqual(node.to_html(), "<div><pre><code>Code</code></pre></div>")


    def test_quote(self):
        node = markdown_to_html_node(">Quote") # Fix optional space
        self.assertEqual(node.to_html(), "<div><blockquote>Quote</blockquote></div>")


    def test_unordered_list(self):
        markdown = "- item one\n- item two\n- item three"
        node = markdown_to_html_node(markdown)
        
        expected_html = "<div><ul><li>item one</li><li>item two</li><li>item three</li></ul></div>"
        assert node.to_html() == expected_html


    def test_ordered_list(self):
        markdown = "1. item one\n2. item two\n3. item three"
        node = markdown_to_html_node(markdown)
        
        expected_html = "<div><ol><li>item one</li><li>item two</li><li>item three</li></ol></div>"
        assert node.to_html() == expected_html


class TestExtractTitle(unittest.TestCase):
    def test_simple(self):
        text = "# This is the title"
        is_value = extract_title(text)
        should_be_value = "This is the title"
        self.assertEqual(should_be_value, is_value)
