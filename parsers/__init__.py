__author__ = 'gbenami'

"""
xl-my-expenses - A utility for parsing a bank sheet into
your expenses excel.
__init__.py is an importing script.
"""

__all__ = ['bankParser', 'hapoalimCreditParser', 'hapoalimAccountParser']
# deprecated to keep older scripts who import this from breaking
from parsers.bankParser import bankParser
from parsers.hapoalimCreditParser import hapoalimCreditParser
from parsers.hapoalimAccountParser import hapoalimAccountParser

