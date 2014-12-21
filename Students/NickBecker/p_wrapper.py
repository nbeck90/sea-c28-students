def para_string(func):
    """Wraps the result of a function with <p> and </p>"""
    def add_tags(*args, **kwargs):
        return "<p> {} </p>".format(func(*args, **kwargs))
    return add_tags


@para_string
def get_string(string):
    """Returns a string"""
    return string
