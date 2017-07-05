import cmd
import sys
from docopt_decorator import DocoptInteractive
from docopt import docopt

class GenieInteractive (cmd.Cmd):
    intro = 'Welcome to my Epic Translator!' \
    + ' (type help for a list of commands.)'
    prompt = '(Epic Translator) '
    file = None

    @DocoptInteractive
    def do_translate(self, arg):
        """Usage: translate <text> <target>"""
        print(arg)

    @DocoptInteractive
    def do_languages(self, arg):
        """Usage: languages
        """

        print(arg)

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()

#opt = docopt(__doc__, sys.argv[1:])