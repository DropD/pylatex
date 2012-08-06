from environment import environment

class doc_env(environment):

    def __init__(self, *args):
        super(doc_env, self).__init__('document', content=args)

