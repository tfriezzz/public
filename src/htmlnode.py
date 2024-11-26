class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError


    def props_to_html(self):
            return "".join(f' {key}="{value}"' for key, value in self.props.items())


    def __eq__(self, other):
        if isinstance(other, HTMLNode):
            return (self.tag == other.tag and 
                    self.value == other.value and 
                    self.children == other.children and 
                    self.props == other.props)
        return False

    
    def __repr__(self):
        return f"tag:{self.tag} value:{self.value} children:{self.children} props:{self.props}"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("LeafNode must have value")
        super().__init__(tag, value, None, props if props else {})


    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have value")
        if self.tag is None:
            return str(self.value)
        else:
            props_string = str(self.props_to_html()) if self.props else ""
            return f"<{self.tag}{props_string}>{self.value}</{self.tag}>"



class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props if props else {})


    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if self.children is None or len(self.children) == 0:
            raise ValueError("ParentNode must have children")
        else:
            html_string = str(self.props_to_html()) if self.props else ""
            children_string = ""
            for child in self.children:
                children_string += str(child.to_html())
                print(f"test: {children_string}")
            return f"<{self.tag}{html_string}>{children_string}</{self.tag}>"
