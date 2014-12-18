class Element(list):
    """Creates all elements for the HTML rendering"""
    indent = "    "

    def __init__(self, content=None, **kwargs):
        if content is None:
            self.content = []
        else:
            self.content = [content]
        self.attribute = kwargs
        self.html_tag = ""

    def append(self, words=None):
        self.content.append(words)

    def render(self, file_out, ind="    "):
        attribute_list = []
        if self.attribute:
            for key, value in self.attribute.items():
                attribute_list.append('{}="{}"'.format(key, value))
        file_out.write("{}<{} {}>\n".format(ind,
                                            self.html_tag,
                                            " ".join(attribute_list)))
        for text in self.content:
            try:
                text.render(file_out, self.indent + ind)
            except AttributeError:
                file_out.write("{}{}\n".format(ind,
                                               text))

        file_out.write("{}</{}>\n".format(ind, self.html_tag))


class Body(Element):
    """Creates a body tag"""
    def __init__(self, content=None, **kwargs):
        super(Body, self).__init__(content, **kwargs)
        self.html_tag = "body"


class Html(Element):
    """Creates an HTML tag as well as a doctype"""
    def __init__(self, content=None, **kwargs):
        super(Html, self).__init__(content, **kwargs)
        self.html_tag = "html"

    def render(self, file_out, ind="    "):
        attribute_list = []
        if self.attribute:
            for key, value in self.attribute.items():
                attribute_list.append("{}={}".format(key, value))
        file_out.write("<!DOCTYPE html>\n")
        file_out.write("{}<{} {}>\n".format(ind,
                                            self.html_tag,
                                            " ".join(attribute_list)))
        for text in self.content:
            try:
                text.render(file_out, self.indent + ind)
            except AttributeError:
                file_out.write("{}{}\n".format(ind,
                                               text))

        file_out.write("{}</{}>\n".format(ind, self.html_tag))


class P(Element):
    "Creates a paragraph tag"""
    def __init__(self, content=None, **kwargs):
        super(P, self).__init__(content, **kwargs)
        self.html_tag = "p"


class Head(Element):
    """Creates a header tag"""
    def __init__(self, content=None, **kwargs):
        super(Head, self).__init__(content, **kwargs)
        self.html_tag = "head"


class OneLineTag(Element):
    """Creates a tag that is positioned all on one line"""
    def render(self, file_out, ind="    "):
        file_out.write("{}<{}>".format(ind, self.html_tag))
        for text in self.content:
            try:
                text.render(file_out, self.indent + ind)
            except AttributeError:
                file_out.write("{}".format(text))

        file_out.write("</{}>\n".format(self.html_tag))


class Title(OneLineTag):
    """Creates a title tag"""
    def __init__(self, content=None, **kwargs):
        super(Title, self).__init__(content, **kwargs)
        self.html_tag = "title"


class SelfClosingTag(Element):
    """Creates a tag that closes itself"""
    def __init__(self, content=None, **kwargs):
        super(SelfClosingTag, self).__init__(content, **kwargs)

    def render(self, file_out, ind=""):
        file_out.write("{}{}<{} />\n".format(ind,
                                             self.indent,
                                             self.html_tag))


class Hr(SelfClosingTag):
    """Adds in a horizontal line"""
    def __init__(self, content=None, **kwargs):
        super(Hr, self).__init__(content, **kwargs)
        self.html_tag = "hr"


class Br(SelfClosingTag):
    """Adds in a line break"""
    def __init__(self, content=None, **kwargs):
        super(Br, self).__init__(content, **kwargs)
        self.html_tag = "br"


class A(Element):
    """Creates a link to a webpage, a.k.a, an anchor"""
    def __init__(self, link=None, content=None):
        new_link = {"href": '{}'.format(link)}
        super(A, self).__init__(content, **new_link)
        self.html_tag = "a"


class Ul(Element):
    """Creates an unordered list"""
    def __init__(self, content=None, **kwargs):
        super(Ul, self).__init__(content, **kwargs)
        self.html_tag = "ul"


class Li(Element):
    """Creates an item in a list"""
    def __init__(self, content=None, **kwargs):
        super(Li, self).__init__(content, **kwargs)
        self.html_tag = "li"


class H(Element):
    """Creates a header off of a given size"""
    def __init__(self, size, content=None, **kwargs):
        super(H, self).__init__(content, **kwargs)
        self.html_tag = "H{}".format(size)


class Meta(SelfClosingTag):
    """Sets the encoding of the HTML output"""
    def __init__(self, content=None, **kwargs):
        super(Meta, self).__init__(content, **kwargs)
        self.html_tag = 'meta charset="UTF-8"'
