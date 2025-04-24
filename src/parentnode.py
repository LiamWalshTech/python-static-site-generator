from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("invalid HTML: no tag")
        if self.children is None:
            raise ValueError("invalid Children: no children given")

        opening_tag = f"<{self.tag}{self.props_to_html()}>"
        closing_tag = f"</{self.tag}>"
        children_strings = []

        for child in self.children:
            children_strings.append(child.to_html())

        return opening_tag + "".join(children_strings) + closing_tag

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
