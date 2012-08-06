def is_seq(arg):
    return (not hasattr(arg, 'strip')
            and hasattr(arg, '__getitem__')
            or  hasattr(arg, '__iter__'))

def is_str(arg):
    return hasattr(arg, 'strip')

def is_latex(arg):
    return hasattr(arg, 'get_str')
