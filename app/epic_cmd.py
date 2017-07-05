import cmd
import sys
from docopt_decorator import DocoptInteractive
from docopt import docopt
import requests

"""
    Usage: EpicTranslator translate <text> to <language>


    """

class GenieInteractive (cmd.Cmd):
    intro = 'Welcome to my Epic Translator!' \
    + ' (type help for a list of commands.)'
    prompt = '(EpicTranslator) '
    file = None
    base_url="https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto"

    @DocoptInteractive
    def do_translate(self, arg):
        """Usage: translate <text> to <language>"""
        params={"tl":"esp","dt":"t",q:""}
        r=requests.get(base_url)
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