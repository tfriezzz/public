import unittest
from text_to_textnodes import *
from textnode import *

class TestTextToTextNodes(unittest.TestCase):
    def test_no_delimiter(self):
        text = "This is a test with no delimiters"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, "This is a test with no delimiters")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)

        
    def test_simple_text(self):
        text = "Hello world"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, "Hello world")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)


    def test_italic_text(self):
        text = "This is *italic* text"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text, "This is ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text, "italic")
        self.assertEqual(nodes[1].text_type, TextType.ITALIC)
        self.assertEqual(nodes[2].text, " text")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)
        
    def test_code_block(self):
        text = "This is a `code block` example"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text, "This is a ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text, "code block")
        self.assertEqual(nodes[1].text_type, TextType.CODE)
        self.assertEqual(nodes[2].text, " example")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)
        
    def test_bold_text(self):
        text = "This is **bold** text"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text, "This is ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text, "bold")
        self.assertEqual(nodes[1].text_type, TextType.BOLD)
        self.assertEqual(nodes[2].text, " text")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)
        

    def test_single_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 2)
        self.assertEqual(nodes[0].text, "This is text with a ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text, "rick roll")
        self.assertEqual(nodes[1].text_type, TextType.IMAGE)
        self.assertEqual(nodes[1].url, "https://i.imgur.com/aKaOqIh.gif")


    def test_single_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 2)
        self.assertEqual(nodes[0].text, "This is text with a link ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text, "to boot dev")
        self.assertEqual(nodes[1].text_type, TextType.LINK)
        self.assertEqual(nodes[1].url, "https://www.boot.dev")


    def test_all_delimiters(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 10)
        self.assertEqual(nodes[0].text, "This is ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)


    """def test_unpaired_bold_delimiters(self):
        text = "This has **complete bold** and **incomplete and *italic*"
        nodes = text_to_textnodes(text)
        self.assertEqual(nodes[0].text, "This has ")
        self.assertEqual(nodes[1].text, "complete bold")
        self.assertEqual(nodes[1].text_type, TextType.BOLD)
        self.assertEqual(nodes[2].text, " and **incomplete and ")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)
        self.assertEqual(nodes[3].text, "italic")
        self.assertEqual(nodes[3].text_type, TextType.ITALIC)"""

