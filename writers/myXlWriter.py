# -*- coding: utf-8 -*-
__author__ = 'gbenami'

"""
xl-my-expenses - A utility for parsing a bank sheet into
your expenses excel.
my Xl Writer is an instance of XL writer.
"""

from xlWriter import xlWriter
from constants import constants
from xlrd.book import colname

class myXlWriter(xlWriter):
    def __init__(self, fileName, writerType):
        """
        Opens the input file/stream and gets ready to parse it.
        """
        xlWriter.__init__(self, fileName, writerType)
        self.emptyRowsPerSheet = {}

    def _findFreeRow(self, record):
        """
        Find free row to write records to.
        """
        expenseStartColumn, expenseStartRow, expenseEndColumn, expenseEndRow = 0, 0, 0, 0
        sheetName = constants.MONTH_NUM_TO_STRING[record.getDate().tm_mon]

        # check if already found the the empty row
        if sheetName in self.emptyRowsPerSheet:
           self.emptyRowsPerSheet[sheetName] = (self.emptyRowsPerSheet[sheetName][0] + 1,
                                                self.emptyRowsPerSheet[sheetName][1])
        else:
            self.ws = self.wb.sheet_by_name(sheetName)
            recordsSignature = [constants.DATE_SIG, constants.CATEGORY_SIG,
                                constants.DESCRIPTION_SIG, constants.COST_SIG]
            num_rows = self.ws.nrows - 1
            num_cells = self.ws.ncols - 1
            curr_row = -1

            while curr_row < num_rows:
                curr_row += 1
                curr_cell = -1
                while curr_cell < num_cells:
                    if curr_cell > constants.MAX_COL_NUM:
                        break
                    curr_cell += 1

                    rowTuple = [self.ws.cell_value(curr_row, curr_cell + i) for i in range(4)]
                    if rowTuple == recordsSignature:
                        expenseStartColumn = curr_cell
                        expenseStartRow = curr_row + 1
                        expenseEndColumn = curr_cell + 4

            wsRows = [self.ws.row_values(rowx=expenseStartRow + i, start_colx=expenseStartColumn, end_colx=expenseEndColumn)
                      for i in range(num_rows - expenseStartRow)]

            foundEmptyLine = False
            emptyRow = -1
            for rowNumber, line in enumerate(wsRows):
                if all(item == "" for item in line) and not foundEmptyLine:
                    foundEmptyLine = True
                    emptyRow = rowNumber + 1
                elif not all(item == "" for item in line) and foundEmptyLine:
                    foundEmptyLine = False
            firstEmptyRow = emptyRow + int(expenseStartRow)

            self.emptyRowsPerSheet[sheetName] = (firstEmptyRow, colname(colx=expenseStartColumn))
        return self.emptyRowsPerSheet[sheetName]

    def writeRecord(self, record):
        """
        Checks if there is more records, and sets the current record
        to be the next record.
        :return: True if there are.
        """
        (emptyRow, emptyColumn) = self._findFreeRow(record)
        dateSlot = "%s%s" % (str(emptyColumn), str(emptyRow))
        collectorSlot = "%s%s" % (str(chr(ord(emptyColumn.lower()) + 2)).upper(), str(emptyRow))
        costSlot = "%s%s" % (str(chr(ord(emptyColumn.lower()) + 3)).upper(), str(emptyRow))

        self.infoToSave[(self.ws.name, dateSlot)] = "%s/%s/%s" % (record.getDate().tm_mday,
                                                                   record.getDate().tm_mon,record.getDate().tm_year)
        self.infoToSave[(self.ws.name, collectorSlot)] = record.getCollector()
        self.infoToSave[(self.ws.name, costSlot)] = record.getCost()