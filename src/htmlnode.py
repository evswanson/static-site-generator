


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
        props = ''
        for key, value in self.props.items():
            props += f' {key}="{value}"'
        
        return props
    
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    