__author__ = 'gbenami'

from parsers import hapoalimCreditParser
import sys
from parserFactory import parserFactory
from writerFactory import writerFactory
from xlwings import Workbook, Range

def main():
    """
    Main function.
    """
    # Assign all program argument to local variables
    bankName = sys.argv[1]
    creditFileName = sys.argv[2]
    xlType = sys.argv[3]
    accountManageFileName = sys.argv[4]

    parser = parserFactory.createParser(bankName, creditFileName)
    writer = writerFactory.createWriter(xlType, accountManageFileName)

    # Read from parser and write to file
    while parser.hasMoreRecords():
        record = parser.getRecord()
        writer.writeRecord(record = record)

    # Save file
    writer.saveFile(accountManageFileName)

if __name__ == "__main__":
    main()
