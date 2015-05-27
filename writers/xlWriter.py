__author__ = 'gbenami'

"""
xl-my-expenses - A utility for parsing a bank sheet into
your expenses excel.
xl Writer is an interface of different xl writers.
"""

from openpyxl import load_workbook
from openpyxl import workbook

class xlWriter(object):
    def __init__(self, fileName, writerType):
        """
        Opens the input file/stream and gets ready to parse it.
        """
        self.fileName = fileName
        self.writerType = writerType
        self.wb = load_workbook(filename = self.fileName, read_only=False)

    def _findFreeRow(self, record):
        """
        Find free row to write records to.
        """
        raise NotImplementedError( "xlWriter is an abstract class" )

    def writeRecord(self, record):
        """
        Checks if there is more records, and sets the current record
        to be the next record.
        :return: True if there are.
        """
        raise NotImplementedError( "xlWriter is an abstract class" )

    def __str__(self):
        return "%s writer is writing to file %s." % (self.writerType, self.fileName)
