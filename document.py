from pylatex import doc_env

class document(object):
    __slots__ = ['preamble', 
                 'doc_env',
                 'string']

    def __init__(self, preamble, *args):
        self.preamble = preamble
        self.string = '{preamble}\n{document}'
        if args:
            self.doc_env = doc_env(*args)
        else:
            self.doc_env = doc_env()

    def add_content(self, *args):
        self.doc_env.add_content(args)

    def get_str(self):
        return self.string.format(preamble = self.preamble.get_str(),
                                  document = self.doc_env.get_str())
