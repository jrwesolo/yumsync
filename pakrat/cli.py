#!/usr/bin/python -tt

import pakrat
import sys
from optparse import OptionParser

parser = OptionParser(version='pakrat %s' % pakrat.__version__)
parser.add_option('--dest',
    help='Root destination for all YUM repositories')
parser.add_option('-d', '--repodir', action='append', default=[],
    help='A "repos.d" directory of YUM configurations. (repeatable)')
parser.add_option('-f', '--repofile', action='append', default=[],
    help='A YUM configuration file. (repeatable)')
parser.add_option('-r', '--repoversion', default=None,
    help=('The version of the repository to create. By default, this will '
          'be the current date in format: YYYY-MM-DD'))
options, args = parser.parse_args()

if not options.dest:
    print '--dest is required'
    sys.exit(1)

pakrat.sync(
    options.dest,
    repofiles=options.repofile,
    repodirs=options.repodir,
    repoversion=options.repoversion
)
