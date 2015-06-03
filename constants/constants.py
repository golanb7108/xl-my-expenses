# -*- coding: utf-8 -*-
__author__ = 'gbenami'

"""
xl-my-expenses - A utility for parsing a bank sheet into
your expenses excel.
constants.py holds all of the constants in the project.
"""

import re


DATE_SIG = u"תאריך"
CATEGORY_SIG = u"קטגוריה"
DESCRIPTION_SIG = u"תיאור"
COST_SIG = u"סכום"
MONTH_NUM_TO_STRING = {1: u'ינואר', 2: u'פברואר', 3: u'מרץ', 4: u'אפריל', 5: u'מאי', 6: u'יוני', 7: u'יולי',
                       8: u'אוגוסט', 9: u'ספטמבר', 10: u'אוקטובר', 11: u'נובמבר', 12: u'דצמבר'}
PARSER_TYPES = {u'נתוני כרטיס אשראי - פועלים': "hapoalimCredit", u'עובר ושב - פועלים': "hapoalimAccount",
                u'נתוני כרטיס אשראי - ויזה': "visaCredit"}
XL_TYPES = {u'מעקב הוצאות הכנסות נקי': "my"}
DATA_TYPE_TO_PARSE = "Data needing transfer"
XL_TYPE_TO_WRITE = "Write to expenses type"
FILE_TYPES = [XL_TYPE_TO_WRITE, DATA_TYPE_TO_PARSE]
RAW_DATA_FILE = "Data File"
TARGET_EXPENSE_FILE = "Expenses File"
LOGO_PATH = r'C:\Users\gbenami\PycharmProjects\xl-my-expenses\periphery\logo.ico'
VERSION = "v0.01"
DOWNLOAD_URL = "https://github.com/golanb7108/xl-my-expenses"
DATE_PATT = [re.compile("(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):(\d{2})"),
            re.compile("(\d{2})/(\d{2})/(\d{4})"), re.compile("(\d{2})/(\d{2})/(\d{2})")]
HAPOALIM_CREDIT_COST_INDEX = 3
HAPOALIM_ACCOUNT_COST_INDEX = 4
VISA_CREDIT_COST_INDEX = 4