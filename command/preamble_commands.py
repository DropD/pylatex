from command_factory import command_factory

# document class
documentclass = command_factory('documentclass', ma=1,
    ol = ['10pt', '11pt', '12pt',
          'letterpaper', 'a4paper', 'a5paper', 'b5paper', 'executivepaper', 'legalpaper',
          'fleqn', 'leqno',
          'titlepage', 'notitlepage',
          'onecolumn', 'twocolumn',
          'twoside', 'oneside',
          'landscape',
          'openright', 'openany',
          'draft'])

# usepackage
usepackage = command_factory('usepackage', ma=1, ol='')

# title command
title         = command_factory('title',    ma=1)
subtitle      = command_factory('subtitle', ma=1)
author        = command_factory('author',   ma=1)
date          = command_factory('date',     ma=1)


# newcommand
newcommand = command_factory('newcommand', ma=2)
