from pylatex import command
from pylatex import text
#import pylatex.tools.is_latex as is_latex
from pylatex.tools import is_latex

class environment(object):
    __slots__ = ['name', 'begin', 'end',
                 #'options', 'option_list',
                 #'arguments', 'max_args',
                 'string', 'content']

    def __init__(self, name, **kwargs):
        self.name = name
        self.content = []
        self.string = '{begin}\n{content}\n{end}'

        self.begin = command('begin{{{name}}}'.format(name=self.name), **kwargs) 
        self.end   = command('end', arguments = [self.name], max_args=1, option_list=[])

        self.set_kwargs(**kwargs)

    def set_kwargs(self, **kwargs):
        if 'content' in kwargs:
            self.add_content(kwargs['content'])

    def add_content(self, content):
        if not is_latex(content):
            self.content.append(text(content))
        elif p.is_seq(content):
            self.content.extend(content)
        else:
            self.content.append(contend)

    def get_str(self):
        return self.string.format(begin   = self.begin.get_str(),
                                  end     = self.end.get_str(),
                                  content = '\n'.join([c.get_str() for c in self.content]))
