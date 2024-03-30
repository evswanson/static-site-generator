import unittest
from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        answer = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), answer)


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node_1 = LeafNode(tag="p", value="This is a paragraph of text.")
        answer_1 = "<p>This is a paragraph of text.</p>"
        self.assertEqual(node_1.to_html(), answer_1)

    def test_to_html_prop(self):
        node_2 = LeafNode(tag="a", value="Click me!", props={"href": "https://www.youtube.com"})
        answer_2 = '<a href="https://www.youtube.com">Click me!</a>'
        self.assertEqual(node_2.to_html(), answer_2)

    def test_to_html_no_tag(self):
        node = LeafNode(value="Value with no tag")
        answer = "Value with no tag"
        self.assertEqual(node.to_html(), answer)

    def test_to_html_no_value(self):
        node = LeafNode(tag="a", props={"href": "https://www.youtube.com"})
        self.assertRaises(ValueError, node.to_html)



if __name__ == "__main__":
    unittest.main()
