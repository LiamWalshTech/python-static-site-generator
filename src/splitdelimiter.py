from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    nodes_array = []

    for old_node in old_nodes:
        text_split = old_node.text.split(delimiter)
        nodes_array.append(TextNode(text_split[0], TextType.NORMAL))
        nodes_array.append(TextNode(text_split[1], TextType.CODE))
        nodes_array.append(TextNode(text_split[2], TextType.NORMAL))

    return nodes_array
