from scripts.base import Script
from models import *

class DBShell(Script):

    description = "Database Shell"

    def run(self):
        welcome = "Database Shell"
        print "\n" + welcome
        print "=" * len(welcome)

        try:
            from IPython.terminal.embed import InteractiveShellEmbed
            ipshell = InteractiveShellEmbed(banner1='')
            ipshell()
        except ImportError:
            try:
                # ipython < v0.11
                # pylint: disable=E0611
                from IPython.Shell import IPShellEmbed
                IPShellEmbed()('')
            except ImportError:
                import code
                code.InteractiveConsole(context).interact('')

if __name__ == '__main__':
    DBShell().run()
