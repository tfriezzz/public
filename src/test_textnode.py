import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_non_eq(self):
        node = TextNode("This is a node", TextType.IMAGE)
        node2 = TextNode("This is a diffrent node", TextType.IMAGE)
        self.assertNotEqual(node, node2)


    def test_none_url(self):
        node = TextNode("No url", TextType.LINK, url=None)
        node2 = TextNode("No url", TextType.LINK, url=None)
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
