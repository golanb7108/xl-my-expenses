__author__ = 'gbenami'

"""
xl-my-expenses - A utility for parsing a bank sheet into
your expenses excel.
Writer factory is a factory for xl writers.
"""
from writers import *

class writerFactory(object):
    # Create based on parser name:
    @staticmethod
    def createWriter(type, fileName):
        if type == "my": return myXlWriter(fileName, type)

