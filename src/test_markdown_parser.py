import unittest
from textnode import TextNode, TextType, text_node_to_html_node 
from markdown_parser import split_nodes_delimiter


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_basic_split(self):
        node = TextNode("That's a **bold** statement", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

        assert len(new_nodes) == 3
        assert new_nodes[0].text == "That's a "
        assert new_nodes[0].text_type == TextType.TEXT
        assert new_nodes[1].text == "bold"
        assert new_nodes[1].text_type == TextType.BOLD
        assert new_nodes[2].text == " statement"
        assert new_nodes[2].text_type == TextType.TEXT
