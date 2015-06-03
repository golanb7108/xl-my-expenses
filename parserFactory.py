__author__ = 'gbenami'

"""
xl-my-expenses - A utility for parsing a bank sheet into
your expenses excel.
Parser factory is a factory for bank parsers.
"""

from parsers import hapoalimAccountParser, hapoalimCreditParser, visaCreditParser
from constants import constants

class parserFactory(object):
    # Create based on parser name:
    @staticmethod
    def createParser(type, fileName):
        if type == "hapoalimCredit": return hapoalimCreditParser(fileName,type,
                                                                 constants.HAPOALIM_CREDIT_COST_INDEX)
        elif type == "hapoalimAccount": return hapoalimAccountParser(fileName, type,
                                                                     constants.HAPOALIM_ACCOUNT_COST_INDEX)
        elif type == "visaCredit": return visaCreditParser(fileName, type,
                                                           constants.VISA_CREDIT_COST_INDEX)