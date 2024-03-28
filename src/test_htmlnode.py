import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        answer = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), answer)


if __name__ == "__main__":
    unittest.main()
