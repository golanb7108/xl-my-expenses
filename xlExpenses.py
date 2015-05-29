__author__ = 'gbenami'

from parsers import hapoalimParser
import sys
from parserFactory import parserFactory
from writerFactory import writerFactory
from xlwings import Workbook, Range

def main():
    """
    Main function.
    """
    bankName = sys.argv[1]
    creditFileName = sys.argv[2]
    xlType = sys.argv[3]
    accountManageFileName = sys.argv[4]
    saveToFile = sys.argv[5]
    parser = parserFactory.createParser(bankName, creditFileName)
    writer = writerFactory.createWriter(xlType, accountManageFileName)

    while parser.hasMoreRecords():
        record = parser.getRecord()
        writer.writeRecord(record = record)

    writer.saveFile(accountManageFileName)

if __name__ == "__main__":
    main()
