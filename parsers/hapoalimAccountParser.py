__author__ = 'gbenami'

"""
xl-my-expenses - A utility for parsing a bank sheet into
your expenses excel.
HaPoalim Account Parser is an instance of a bank parser for hapoalim.
"""

from billingDataParserByIndex import billingDataParserByIndex
from debitRecord import debitRecord
from constants import constants

class hapoalimAccountParser(billingDataParserByIndex):
    def __init__(self, fileName, bankName, costIndex):
        """
        Opens the input file/stream and gets ready to parse it.
        """
        billingDataParserByIndex.__init__(self, fileName, bankName, costIndex)