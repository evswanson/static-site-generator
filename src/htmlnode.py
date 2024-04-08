


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag # a string representing the html tag name
        self.value = value # a string representing the value of the HTML tag name
        self.children = children # a list of HTMLNode objects representing the children of this node
        self.props = props # dictionary of key-value pairs representing attributes

    def to_html(self):
        # child classes will override
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ''
        props = ''
        for key, value in self.props.items():
            props += f' {key}="{value}"'
        
        return props
    
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        if self.tag is None:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
        

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML: no tag")
        if self.children is None:
            raise ValueError("Invalid HTML: no children")
        leafs = ""
        for child in self.children:
            leafs += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{leafs}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
        