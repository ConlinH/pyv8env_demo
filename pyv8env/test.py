import os
import sys
sys.path.append(os.path.dirname(os.getcwd()))

import pyv8env
from pyv8env.env.impl import *
from pyv8env.env.downloader import DownloadHandler


def callback(ctx, *arg):
  print(ctx.exec_js('''debugger;  window; ''', 'VM1'))

  print(ctx.exec_js('''debugger;  1+1;'''))

  print(ctx.exec_js('''debugger;  window.outerWidth;'''))

def test():

    win = Window(
        hook=False,
        # download_handler=TestDownloadHandler()
    )
    win.start(devtool=False, callback=callback)
    # win.start(devtool=True)



if __name__ == '__main__':
    test()
