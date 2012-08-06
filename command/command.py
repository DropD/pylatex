from pylatex import text
#import pylatex.tools.is_latex as is_latex
from pylatex.tools import is_latex

class command(object):
    __slots__ = ['name', 
                 'options', 
                 'option_list',
                 'arguments', 
                 'max_args',
                 'string']

    def __init__(self, name, **kwargs):
        self.name = name
        self.options = {}
        self.option_list = []
        self.arguments = []
        self.max_args = -1
        self.string = '\\{name}{options}{arguments}'

        self.set_kwargs(**kwargs)

    def set_kwargs(self, **kwargs):
        if 'max_args' in kwargs:
            self.max_args = kwargs['max_args']
        if 'option_list' in kwargs:
            self.option_list = kwargs['option_list']
        if 'options' in kwargs:
            self.set_options(**kwargs['options'])
        if 'arguments' in kwargs:
            self.set_arguments(*kwargs['arguments'])
        if 'pass_kwargs' in kwargs and kwargs['pass_kwargs']:
            for arg in self.arguments:
                if isinstance(arg, (command, environment)):
                    arg.set_kwargs(**kwargs)

    def argnum_is_ok(self, args):
        if self.max_args > -1 and self.max_args < len(self.arguments) + len(args):
            return False
        else:
            return True

    def set_arguments(self, *args):
        if self.argnum_is_ok(args):
            for arg in args:
                if is_latex(arg):
                    self.arguments.append(arg)
                else:
                    self.arguments.append(text(arg))
        else:
            raise IndexError('too many arguments for {0}, max_args = {1}'.format(self.name, self.max_args))

    def replace_arguments(self, *args):
        if self.argnum_is_ok(args):
            for i in len(args):
                if not is_latex(args[i]):
                    args[i] = text(args)
            self.arguments = args
        else:
            raise IndexError('too many arguments for {0}'.format(self.name))

    def set_argument(self, idx, arg):
        if idx < self.max_args:
            self.arguments = [self.arguments[i] for i in range(self.max_args) if i != idx]
            if not is_latex(arg):
                arg = text(arg)
            self.arguments.insert(idx, arg)
        else:
            raise IndexError('idx > max_args for {0}'.format(self.name))

    def set_options(self, **opts):
        if self.option_list:
            for opt in self.option_list:
                if opt in opts:
                    self.options[opt] = opts[opt]
        else:
            for opt in opts:
                self.options[opt] = opts[opt]

    def get_argstr(self):
        argstr = ''
        for arg in self.arguments:
            argstr += '{{{0}}}'.format(arg.get_str())
        return argstr
    
    def get_optstr(self):
        optsep = ','
        if self.options:
            optstr = optsep.join(['{0[0]}={0[1]}'.format(opt) for opt in self.options.items()])
            optstr = '['+optstr+']'
        else:
            optstr = ''
        return optstr

    def get_str(self):
        return self.string.format(name      = self.name,
                                  options   = self.get_optstr(),
                                  arguments = self.get_argstr())

class nocommand(object):
    __slots__ = []
    def __init__(self):
        super(nocommand, self).__init__()
    def get_str(self):
        return ''

