# -*- coding: utf-8 -*-
__author__ = 'gbenami'

"""
xl-my-expenses - A utility for parsing a bank sheet into
your expenses excel.
constants.py holds all of the constants in the project.
"""

DATE_SIG = u"תאריך"
CATEGORY_SIG = u"קטגוריה"
DESCRIPTION_SIG = u"תיאור"
COST_SIG = u"סכום"
MONTH_NUM_TO_STRING = {1: u'ינואר', 2: u'פברואר', 3: u'מרץ', 4: u'אפריל', 5: u'מאי', 6: u'יוני', 7: u'יולי',
                       8: u'אוגוסט', 9: u'ספטמבר', 10: u'אוקטובר', 11: u'נובמבר', 12: u'דצמבר'}
PARSER_TYPES = {u'נתוני כרטיס אשראי - פועלים': "hapoalimCredit", u'עובר ושב - פועלים': "hapoalimAccount"}
XL_TYPES = {u'מעקב הוצאות הכנסות נקי': "my"}
DATA_TYPE_TO_PARSE = "Data needing transfer"
XL_TYPE_TO_WRITE = "Write to expenses type"
FILE_TYPES = [XL_TYPE_TO_WRITE, DATA_TYPE_TO_PARSE]
RAW_DATA_FILE = "Data File"
TARGET_EXPENSE_FILE = "Expenses File"