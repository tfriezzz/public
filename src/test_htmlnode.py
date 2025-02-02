import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLnode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("<a>", "this is the value", None, {"href": "www.example.com"})
        node2 = HTMLNode("<a>", "this is the value", None, {"href": "www.example.com"})
        self.assertEqual(node, node2)

    def test_props_to_html(self):
        node = HTMLNode("a", "value", None, {"href": "https://www.example.com", "target": "_blank"})
        expected_props = ' href="https://www.example.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_props)

    def test_node_without_props(self):
        node = HTMLNode("p", "This is a paragraph.")
        expected_string = "tag:p value:This is a paragraph. children:None props:None"
        self.assertEqual(repr(node), expected_string)


class TestLeafNode(unittest.TestCase):
    def test_to_html_with_tag_and_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.example.com"})
        expected_html = '<a href="https://www.example.com">Click me!</a>'
        self.assertEqual(node.to_html(), expected_html)
    
    def test_to_html_without_tag(self):
        node = LeafNode(None, "Just text", {})
        expected_html = "Just text"
        self.assertEqual(node.to_html(), expected_html)

    def test_to_html_value_error(self):
        with self.assertRaises(ValueError):
            node = LeafNode("p", None)
            node.to_html()


class TestParentNode(unittest.TestCase):
    def test_basic_parent(self):
        node = ParentNode(
            "div",
            [LeafNode("p", "hello")]
        )
        self.assertEqual(node.to_html(), "<div><p>hello</p></div>")


    def test_multiple_children(self):
        node = ParentNode(
            "div",
            [LeafNode("p", "hello"), LeafNode("p", "goodbye")]
        )
        self.assertEqual(node.to_html(), "<div><p>hello</p><p>goodbye</p></div>")


    def test_nested_parent(self):
        node = ParentNode(
            "div",
            [ParentNode("div", [LeafNode("p", "hello")])]
        )
        self.assertEqual(node.to_html(), "<div><div><p>hello</p></div></div>")


    def test_invalid_parent(self):
        with self.assertRaises(ValueError):
            #no tag
            node = ParentNode(None, [LeafNode("p", "hello")])
            node.to_html()
        
        with self.assertRaises(ValueError):
            # empty children
            node = ParentNode("div", [])
            node.to_html()


if __name__ == "__main__":
    unittest.main()
