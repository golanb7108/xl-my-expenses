__author__ = 'gbenami'

from parserFactory import parserFactory
from xlMyApp import xlMyApp
from writerFactory import writerFactory
from Tkinter import *

def main():
    """
    Main function.
    """
    # init the xl my expenses app
    root = Tk()
    app = xlMyApp(root)

    # Assign all program argument to local variables
    bankName = str(app.bankName)
    creditFileName = str(app.creditFileName)
    xlType = str(app.xlType)
    accountManageFileName = str(app.accountManageFileName)

    parser = parserFactory.createParser(bankName, creditFileName)
    writer = writerFactory.createWriter(xlType, accountManageFileName)

    # Read from parser and write to file
    while parser.hasMoreRecords():
        record = parser.getRecord()
        if record.getCost() != "None":
            writer.writeRecord(record = record)

    # Save file
    writer.saveFile(accountManageFileName)

if __name__ == "__main__":
    main()
