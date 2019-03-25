# -*- coding: utf-8 -*-
''' Main file to run all selenium tests '''

import sys
from behave.__main__ import main as behave_main

if __name__ == "__main__":
    args = sys.argv
    args[0] = 'selenium_tests'
    # If a browser was specified run tests only on that browser
    if any(arg.lower().startswith('browser=') for arg in args):
        behave_main(args)
    else:
        print('\n  WILL RUN TESTS ON ALL BROWSERS  \n')

        args.append('-D')
        args.append('browser=firefox')
        behave_main(args)

        args[-1] = 'browser=chrome'
        behave_main(args)

        args[-1] = 'browser=edge'
        behave_main(args)

        args[-1] = 'browser=ie'
        behave_main(args)
