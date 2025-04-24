from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value):
        super().__init__(tag, value)
    
    def to_html(self):
        if self.value == None:
            raise ValueError()

        if self.tag == None:
            return value

        return f'<{self.tag}>{self.value}</{self.tag}>'
