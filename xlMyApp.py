# -*- coding: utf-8 -*-
__author__ = 'gbenami'

from Tkinter import *
import ttk
from tkFileDialog import *
from constants import constants

class xlMyApp:
    def __init__(self, root):
        self.root = root
        self.root.wm_title("Xl-My-Expenses")
        self.root.iconbitmap(constants.LOGO_PATH)
        self.addItems()
        self.root.mainloop()

    def addItems(self):
        uiFields = [constants.DATA_TYPE_TO_PARSE, constants.RAW_DATA_FILE, constants.XL_TYPE_TO_WRITE, constants.TARGET_EXPENSE_FILE]
        ents = self.makeForm(self.root, uiFields)
        self.root.bind('<Return>', (lambda event, e=ents: self.fetch(e)))
        self.addButton("Quit", self.root.quit)
        self.addButton("Sync", (lambda e=ents: self.fetch(e)))

    def addButton(self, text, command):
        b1 = Button(self.root, text=text, command=command)
        b1.pack(side=RIGHT, padx=5, pady=5)

    def fetch(self, entries):
        self.bankName = constants.PARSER_TYPES[entries[0][1].get()]
        self.creditFileName = entries[1][1].get()
        self.xlType = constants.XL_TYPES[entries[2][1].get()]
        self.accountManageFileName = entries[3][1].get()
        self.root.quit()

    def btnInBrowseClick(self, row, ent):
        rFilePath = askopenfilename(defaultextension='*',
            initialdir='.', initialfile='', parent=row, title='select a file')
        ent.insert(10, rFilePath)

    def returnLambda(self, row, ent):
        row = row
        ent = ent
        return lambda: self.btnInBrowseClick(row, ent)

    def makeForm(self, root, fields):
       entries = []
       for field in fields:
           btn = None
           row = Frame(root)
           lab = Label(row, width=25, text=field, anchor='w')
           if field in constants.FILE_TYPES:
               box_value = StringVar()
               ent = ttk.Combobox(row, width=70, textvariable=box_value)
               if field == constants.DATA_TYPE_TO_PARSE:
                   ent['values'] = constants.PARSER_TYPES.keys()
               elif field == constants.XL_TYPE_TO_WRITE:
                   ent['values'] = constants.XL_TYPES.keys()
               ent.current(0)
           else:
               ent = Entry(row, width=70)
               btn = Button(row, text='Browse', command=self.returnLambda(row, ent))
               btn.pack(side=RIGHT, expand=YES, fill=X)
           row.pack(side=TOP, fill=X, padx=5, pady=5)
           lab.pack(side=LEFT)
           ent.pack(side=RIGHT, expand=YES, fill=X)
           entries.append((field, ent, btn))

       return entries