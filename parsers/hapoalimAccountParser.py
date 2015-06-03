__author__ = 'gbenami'

"""
xl-my-expenses - A utility for parsing a bank sheet into
your expenses excel.
HaPoalim Account Parser is an instance of a bank parser for hapoalim.
"""

from bankParser import bankParser
from debitRecord import debitRecord
from constants import constants

class hapoalimAccountParser(bankParser):
    def __init__(self, fileName, bankName):
        """
        Opens the input file/stream and gets ready to parse it.
        """
        bankParser.__init__(self, fileName, bankName)

    def hasMoreRecords(self):
        """
        Checks if there is more records, and sets the current record
        to be the next record.
        :return: True if there are.
        """
        while self.currentRow < len(self.wsRows):
            currentRow = self.wsRows[self.currentRow]
            self.currentRow += 1

            try:
                firstCell = str(currentRow[0].value)
                if any(regex.match(firstCell) for regex in constants.DATE_PATT) and \
                                currentRow[4].value is not None:
                    date = str(currentRow[0].value)
                    collector = currentRow[1].value
                    cost = str(currentRow[4].value)
                    self.currentRecord = debitRecord(date, collector, cost)
                    self.recordsList.append(self.currentRecord)
                    return True
            except Exception:
                pass
        # In case no more rows or no more records
        return False