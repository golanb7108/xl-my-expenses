__author__ = 'gbenami'

"""
xl-my-expenses - A utility for parsing a bank sheet into
your expenses excel.
Bank Parser is an interface of different bank parsers.
"""

from openpyxl import load_workbook

class bankParser(object):
    def __init__(self, fileName, bankName):
        """
        Opens the input file/stream and gets ready to parse it.
        """
        self.fileName = fileName
        self.bankName = bankName
        self.wb = load_workbook(filename = self.fileName, read_only=False)

    def hasMoreRecords(self):
        """
        Checks if there is more records, and sets the current record
        to be the next record.
        :return: True if there are.
        """
        raise NotImplementedError( "bankParser is an abstract class" )

    def getRecord(self):
        """
        Get the current record.
        :return: the current record that is pointed.
        """
        raise NotImplementedError( "bankParser is an abstract class" )

    def getDate(self):
        """
        Get the date of the expense.
        :return: return the date.
        """
        raise NotImplementedError( "bankParser is an abstract class" )

    def getCost(self):
        """
        Get the cost of the current record.
        :return: the cost.
        """
        raise NotImplementedError( "bankParser is an abstract class" )

    def getCollector(self):
        """
        Get the collector of the current record.
        :return: the Collector.
        """
        raise NotImplementedError( "bankParser is an abstract class" )

    def __str__(self):
        return "%s parser is parsing file %s." % (self.bankName, self.fileName)