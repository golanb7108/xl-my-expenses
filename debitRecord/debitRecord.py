__author__ = 'gbenami'

"""
xl-my-expenses - A utility for parsing a bank sheet into
your expenses excel.
Debit Record represents a debit credit card record.
"""
import time
import re

class debitRecord(object):
    def __init__(self, date, collector, cost):
        """
        Opens the input file/stream and gets ready to parse it.
        """
        datePatt = [re.compile("(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):(\d{2})"),
                    re.compile("(\d{2})/(\d{2})/(\d{4})")]
        if datePatt[0].match(date):
            fmt_date = time.strptime(date, "%Y-%d-%m %H:%M:%S")
        elif datePatt[1].match(date):
            fmt_date = time.strptime(date, "%d/%m/%Y")

        self.date = fmt_date
        self.collector = collector
        self.cost = cost

    def getDate(self):
        """
        Get the date of the expense.
        :return: the date.
        """
        return self.date

    def getCollector(self):
        """
        Get the collector of the expense.
        :return: the collector.
        """
        return self.collector

    def getCost(self):
        """
        Get the cost of the expense.
        :return: the cost.
        """
        return self.cost
