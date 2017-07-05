import cmd
import sys
from docopt_decorator import DocoptInteractive
from docopt import docopt
import requests
import json

"""
    Usage: EpicTranslator translate  to <language> <text>...


    """

class GenieInteractive (cmd.Cmd):
    intro = 'Welcome to my Epic Translator!' \
    + ' (type help for a list of commands.)'
    prompt = '(EpicTranslator) '
    file = None

    base_url="https://glosbe.com/gapi/translate?from=en"
    #arguments=docopt.docopt(__doc__)
    @DocoptInteractive
    def do_translate(self, arg):
        """Usage: translate to <language> <text>..."""

        text_value=" ".join(arg['<text>'])
        lingo=arg["<language>"]
        values={"dest":lingo,"format":"json","phrase":text_value,"pretty":"true"}
        r=requests.get(self.base_url,params=values)
        lingo_result=json.loads(r.text)['tuc']

        print("\n {} can mean the following in {}".format(text_value,lingo))
        for variation in lingo_result:
            if "phrase" in variation:
                print("\t"+variation['phrase']['text'])

    @DocoptInteractive
    def do_languages(self, arg):
        """Usage: languages
        """

        print(arg)

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye liguist!')
        exit()

#opt = docopt(__doc__, sys.argv[1:])