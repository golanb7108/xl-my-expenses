__author__ = 'gbenami'

"""
xl-my-expenses - A utility for parsing a bank sheet into
your expenses excel.
Parser factory is a factory for bank parsers.
"""
from parsers import bankParser
from parsers import *

class parserFactory(object):
    # Create based on parser name:
    @staticmethod
    def createParser(type, fileName):
        if type == "hapoalim": return hapoalimParser(fileName, type)

