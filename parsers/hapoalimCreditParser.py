__author__ = 'gbenami'

"""
xl-my-expenses - A utility for parsing a bank sheet into
your expenses excel.
HaPoalim Credit Parser is an instance of a bank parser for hapoalim.
"""

from billingDataParserByIndex import billingDataParserByIndex

class hapoalimCreditParser(billingDataParserByIndex):
    def __init__(self, fileName, bankName, costIndex):
        """
        Opens the input file/stream and gets ready to parse it.
        """
        billingDataParserByIndex.__init__(self, fileName, bankName, costIndex)