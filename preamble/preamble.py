from pylatex import preamble_commands as pc
from pylatex import nocommand
from pylatex.tools import is_latex

class preamble(object):
    __slots__ = ['documentclass',
                 'package_list',
                 'definitions',
                 'docinfo',
                 'string']
    
    def __init__(self, *args, **kwargs):
        self.documentclass = pc.documentclass('scrartcl', a4paper='true')
        self.package_list  = []
        self.definitions   = []
        self.docinfo       = [nocommand(), nocommand(), nocommand(), nocommand()]
        self.string   = '{dclass}\n\n%packages{pkgs}\n\n%definitions{defs}\n\n%document info{docinfo}'

        self.set_args(*args)
        self.set_kwargs(**kwargs)

    def set_args(self, *args):
        pass

    def set_kwargs(self, **kwargs):
        if 'documentclass' in kwargs:
            if not is_latex(kwargs['documentclass']):
                self.documentclass = pc.documentclass(kwargs['documentclass'])
            else:
                self.documentclass = kwargs['documentclass']

    def add_pkgs(self, *pkgs):
        for pkg in pkgs:
            self.add_pkg(pkg)

    def add_pkg(self, pkg):
        if is_latex(pkg):
            self.package_list.append(pkg)
        else:
            self.package_list.append(pc.usepackage(pkg))

    def add_pkg_set(self, pkg_set):
        for i in pkg_set:
            pkg = pc.usepackage(i, **pkg_set[i])
            self.package_list.append(pkg)

    def add_definition(self, lhs, rhs):
        defn = pc.newcommand(lhs, rhs)
        self.definitions.append(defn)

    def add_docinfo(self, *args):
        self.set_title(args[0])
        if len(args) > 1:
            self.set_subtitle(args[1])
        if len(args) > 2:
            self.set_author(args[2])
        if len(args) > 3:
            self.set_date(args[3])

    def add_docinfo(self, **kwargs):
        if 'title' in kwargs:
            self.set_title(kwargs['title'])
        if 'subtitle' in kwargs:
            self.set_subtitle(kwargs['subtitle'])
        if 'author' in kwargs:
            self.set_author(kwargs['author'])
        if 'date' in kwargs:
            self.set_date(kwargs['date'])


    def set_author(self, author):
        self.docinfo[2] = pc.author(author)

    def set_title(self, title):
        self.docinfo[0] = pc.title(title)

    def set_date(self, date):
        self.docinfo[3] = pc.date(date)

    def set_subtitle(self, subtitle):
        self.docinfo[1] = pc.subtitle(subtitle)

    def get_pkg_str(self):
        pkgstr = ''
        for pkg in self.package_list:
            pkgstr += '\n'+pkg.get_str()
        return pkgstr

    def get_def_str(self):
        defstr = ''
        for defn in self.definitions:
            defstr += '\n'+defn.get_str()
        return defstr

    def get_info_str(self):
        infstr = ''
        for info in self.docinfo:
            infstr += '\n'+info.get_str()
        return infstr

    def get_str(self):
        return self.string.format(dclass  = self.documentclass.get_str(),
                                  pkgs    = self.get_pkg_str(),
                                  defs    = self.get_def_str(),
                                  docinfo = self.get_info_str())
