#!/usr/bin/env python


class Element(list):

    indent = "    "

    def __init__(self, content=None, **kwargs):
        if content is None:
            self.content = []
        else:
            self.content = [content]
        if kwargs is None:
            self.attributes = None
        else:
            self.attributes = kwargs
        self.html_tag = ""
        self.ind = "    "

    def append(self, words=None):
        self.content.append(words)

    def render(self, file_out, ind=""):
        if self.attributes:
            attrib_list = [" "]
            for attribs in self.attributes:
                attrib_list.append('{}="{}"'.format(attribs,
                                                    self.attributes[attribs]))
            additions = " ".join(attrib_list)
        else:
            additions = ""
        file_out.write(
            "{}{}<{}{}>\n".format(ind,
                                  self.indent,
                                  self.html_tag,
                                  additions)
                      )
        for line in self.content:
            try:
                line.render(file_out, ind + self.indent)
            except AttributeError:
                file_out.write("{}{}{}\n".format(ind,
                                                 self.indent,
                                                 line))
        file_out.write("{}{}</{}>\n".format(ind,
                                            self.indent,
                                            self.html_tag))


# reload(hr)
# e1 = hr.Element()
# e1.append("sometext")
# e1.render()


class OneLineTag(Element):
    def __init__(self, content=None, **kwargs):
        super(OneLineTag, self).__init__(content, **kwargs)

    def render(self, file_out, ind=u""):
        file_out.write(
            "{}{}<{}> {} </{}>\n".format(ind,
                                         self.indent,
                                         self.html_tag,
                                         self.content,
                                         self.html_tag
                                        )
                      )


class SelfClosingTag(Element):
    def render(self, file_out, ind=""):
        file_out.write("{}{}<{} />\n".format(ind,
                                            self.indent,
                                            self.html_tag)
                      )


class P(Element):
    def __init__(self, content=None, **kwargs):
        super(P, self).__init__(content, **kwargs)
        self.html_tag = "p"


class Body(Element):
    def __init__(self, content=None, **kwargs):
        super(Body, self).__init__(content, **kwargs)
        self.html_tag = "body"


class List(Element):
    def __init__(self, content=None, **kwargs):
        super(List, self).__init__(content, **kwargs)
        self.html_tag = "li"


class Html(Element):
    def __init__(self, content=None, **kwargs):
        super(Html, self).__init__(content, **kwargs)
        self.html_tag = "html"

    def render(self, file_out, ind=""):
        file_out.write("<!DOCTYPE html>\n")
        if self.attributes:
            attrib_list = [" "]
            for attribs in self.attributes:
                attrib_list.append('{}="{}"'.format(attribs,
                                                    self.attributes[attribs]))
            additions = " ".join(attrib_list)
        else:
            additions = ""
        file_out.write(
            "{}{}<{}{}>\n".format(ind,
                                  self.indent,
                                  self.html_tag,
                                  additions)
                      )
        for line in self.content:
            try:
                line.render(file_out, ind + self.indent)
            except AttributeError:
                file_out.write("{}{}{}\n".format(ind,
                                                 self.indent,
                                                 line))
        file_out.write("{}{}</{}>\n".format(ind,
                                            self.indent,
                                            self.html_tag))


class Title(OneLineTag):
    def __init__(self, content=None, **kwargs):
        super(Title, self).__init__(content, **kwargs)
        self.html_tag = "title"


class Head(Element):
    def __init__(self, content=None, **kwargs):
        super(Head, self).__init__(content, **kwargs)
        self.html_tag = "head"


class Hr(SelfClosingTag):
    def __init__(self, content=None, **kwargs):
        super(Hr, self).__init__(content, **kwargs)
        self.html_tag = "hr"


class Br(SelfClosingTag):
    def __init__(self, content=None, **kwargs):
        super(Br, self).__init__(content, **kwargs)
        self.html_tag = "br"


class A(Element):
    def __init__(self, link=None, content=None):
        new_link = {"href": '{}'.format(link)}
        super(A, self).__init__(content, **new_link)
        self.html_tag = "a"


class Ul(Element):
    def __init__(self, content=None, **kwargs):
        super(Ul, self).__init__(content, **kwargs)
        self.html_tag = "ul"


class Li(Element):
    def __init__(self, content=None, **kwargs):
        super(Li, self).__init__(content, **kwargs)
        self.html_tag = "li"


class H(Element):
    def __init__(self, size, content=None, **kwargs):
        super(H, self).__init__(content, **kwargs)
        self.html_tag = "H{}".format(size)


class Meta(SelfClosingTag):
    def __init__(self, content=None, **kwargs):
        super(Meta, self).__init__(content, **kwargs)
        self.html_tag = 'meta charset="UTF-8"'
