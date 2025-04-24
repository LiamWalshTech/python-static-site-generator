import unittest

from splitdelimiter import split_nodes_delimiter
from textnode import TextNode, TextType, text_node_to_html_node

class TestSplitDelimiter(unittest.TestCase):
    def test_simple(self):
        node = TextNode("This is text with a `code block` word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.NORMAL),
        ])

if __name__ == "__main__":
    unittest.main()
