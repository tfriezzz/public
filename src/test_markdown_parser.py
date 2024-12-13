import unittest
from textnode import TextNode, TextType, text_node_to_html_node 
from markdown_parser import split_nodes_delimiter


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
        assert len(new_nodes) == 5
        assert new_nodes[0].text == "Test with "
        assert new_nodes[0].text_type == TextType.TEXT
        assert new_nodes[1].text == "multiple"
        assert new_nodes[1].text_type == TextType.BOLD
        assert new_nodes[2].text == " "
        assert new_nodes[2].text_type == TextType.TEXT
        assert new_nodes[3].text == "delimiters"
        assert new_nodes[3].text_type == TextType.BOLD
        assert new_nodes[4].text == ""
        assert new_nodes[4].text_type == TextType.TEXT


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


