__author__ = 'gbenami'

"""
xl-my-expenses - A utility for parsing a bank sheet into
your expenses excel.
"""

from openpyxl import load_workbook
from bankParser import bankParser

class hapoalimParser(bankParser):
    def __init__(self, fileName, bankName):
        """
        Opens the input file/stream and gets ready to parse it.
        """
        bankParser.__init__(self, fileName, bankName)
        first_sheet = self.wb.get_sheet_names()[0]
        self.ws = self.wb.get_sheet_by_name(first_sheet)
        self.currentRow = 0
        self.wsRows = []

        # Get all rows
        rowsToIter = "A1:G" + str(self.ws.get_highest_row())
        self.wsRows = [row for row in self.ws.iter_rows(rowsToIter)]

    def hasMoreRecords(self):
        """
        Are there more records in the file.
        :return: True if there are.
        """
        pass

    def advance(self):
        """
        Reads the next command from the input and makes it the
        current command. Should be called only if hasMoreRecords()
        is true. Initially there is no current command.
        :return:
        """
        pass

    def getRecord(self):
        """
        Get the current record.
        :return: the current record that is pointed.
        """
        pass

    def getDate(self):
        """
        Get the date of the expense.
        :return: return the date.
        """
        pass

    def getCost(self):
        """
        Get the cost of the current record.
        :return: the cost.
        """
        pass

    def getCollector(self):
        """
        Get the collector of the current record.
        :return: the Collector.
        """
        pass


