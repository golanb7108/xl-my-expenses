__author__ = 'gbenami'

"""
xl-my-expenses - A utility for parsing a bank sheet into
your expenses excel.
my Xl Writer is an instance of XL writer.
"""

from openpyxl import load_workbook
from xlWriter import xlWriter
from openpyxl import workbook

class myXlWriter(xlWriter):
    def __init__(self, fileName, writerType):
        """
        Opens the input file/stream and gets ready to parse it.
        """
        xlWriter.__init__(self, fileName, writerType)
        # calculate here the first free line for writing

    def writeRecord(self, record):
        """
        Checks if there is more records, and sets the current record
        to be the next record.
        :return: True if there are.
        """
        # TODO - need to be implemented
        pass