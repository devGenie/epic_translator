import cmd
import sys
from docopt_decorator import DocoptInteractive
from docopt import docopt
import requests

"""
    Usage: EpicTranslator translate  to <language> <text>...


    """

class GenieInteractive (cmd.Cmd):
    intro = 'Welcome to my Epic Translator!' \
    + ' (type help for a list of commands.)'
    prompt = '(EpicTranslator) '
    file = None
    base_url="https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto"
    #arguments=docopt.docopt(__doc__)
    @DocoptInteractive
    def do_translate(self, arg):
        """Usage: translate to <language> <text>..."""

        text_value=" ".join(arg['<text>'])
        #print(requests.urlencode(text_value))
        values={"tl":"esp","dt":"t","q":text_value}
        r=requests.get(self.base_url,params=values)
        print(r.json)

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