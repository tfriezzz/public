import unittest
from textnode import TextNode, TextType, text_node_to_html_node 
from markdown_parser import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_single_delimiter(self):
        node = TextNode("Test with **one** delimiter", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        assert len(new_nodes) == 3
        assert new_nodes[0].text == "Test with "
        assert new_nodes[0].text_type == TextType.TEXT
        assert new_nodes[1].text == "one"
        assert new_nodes[1].text_type == TextType.BOLD
        assert new_nodes[2].text == " delimiter"
        assert new_nodes[2].text_type == TextType.TEXT


    def test_multiple_delimiters(self):
        node = TextNode("Test with **multiple** **delimiters**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        assert len(new_nodes) == 4
        assert new_nodes[0].text == "Test with "
        assert new_nodes[0].text_type == TextType.TEXT
        assert new_nodes[1].text == "multiple"
        assert new_nodes[1].text_type == TextType.BOLD
        assert new_nodes[2].text == " "
        assert new_nodes[2].text_type == TextType.TEXT
        assert new_nodes[3].text == "delimiters"
        assert new_nodes[3].text_type == TextType.BOLD
        

    def test_no_delimiter(self):
        node = TextNode("This is a test with no delimiters", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        assert len(new_nodes) == 1
        assert new_nodes[0].text == "This is a test with no delimiters" 
        assert new_nodes[0].text_type == TextType.TEXT


    def test_already_proccessed_node(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        assert len(new_nodes) == 1
        assert new_nodes[0].text == "This is a bold node"
        assert new_nodes[0].text_type == TextType.BOLD


class TestExtractMarkdownImages(unittest.TestCase):
    def test(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        should_be_value = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        is_value = extract_markdown_images(text)
        self.assertEqual(should_be_value, is_value)


class TestExtractMarkdownLinks(unittest.TestCase):
    def test(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        should_be_value = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        is_value = extract_markdown_links(text)
        self.assertEqual(should_be_value, is_value)


class TestSplitNodesImage(unittest.TestCase):
    def test_single_image(self):
        node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        assert new_nodes[0].text == "This is text with a "
        assert new_nodes[0].text_type == TextType.TEXT
        assert new_nodes[1].text == "rick roll"
        assert new_nodes[1].text_type == TextType.IMAGE
        assert new_nodes[1].url == "https://i.imgur.com/aKaOqIh.gif"


class TestSplitNodesLink(unittest.TestCase):
    def test_single_link(self):
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        assert new_nodes[0].text == "This is text with a link "
        assert new_nodes[0].text_type == TextType.TEXT
        assert new_nodes[1].text == "to boot dev"
        assert new_nodes[1].text_type == TextType.LINK
        assert new_nodes[1].url == "https://www.boot.dev"
