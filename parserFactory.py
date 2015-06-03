__author__ = 'gbenami'

"""
xl-my-expenses - A utility for parsing a bank sheet into
your expenses excel.
Parser factory is a factory for bank parsers.
"""

from parsers import hapoalimAccountParser, hapoalimCreditParser, visaCreditParser

class parserFactory(object):
    # Create based on parser name:
    @staticmethod
    def createParser(type, fileName):
        if type == "hapoalimCredit": return hapoalimCreditParser(fileName, type)
        elif type == "hapoalimAccount": return hapoalimAccountParser(fileName, type)
        elif type == "visaCredit": return visaCreditParser(fileName, type)

