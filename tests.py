# -*- coding: utf-8 -*-
# pylint: disable=unused-import
''' Main file to run all tests. Import all your test classes here'''

from unittest import main

from app.tests import TestUtils, TestLogger, TestSerializer
from app.frontend.tests import FrontEndTest
from app.login.tests import LoginTest

if __name__ == '__main__':
    main(verbosity=2)
