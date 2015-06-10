# xl-my-expenses

Xl-my-expenses transfers all of your expenses from the credit company excel
to your own expenses excel.

![xl-my-expenses](https://github.com/golanb7108/xl-my-expenses/blob/master/periphery/logo.png)

## Requirements

`python` and the following modules:

- `xlmywings` for writing to the target excel.
- `openpyxl` for reading the source excel.
- `lxml` for windows handling.
- `pywin32` for windows handling.
- `xlrd` for reading excels. (installation description later)

## Installation

Install the modules with a python package manager
like `pip`:

    $ pip install xlwings

For getting the xl-my-expenses code:

    $ git clone https://github.com/golanb7108/xl-my-expenses.git

For installing xlrd:
- Unpack it to Python\Lib( for ex. ‘c:\Python27\Lib\xlrd-0.9.3\’)
- Find out setup.py file location(for ex. ‘c:\Python27\Lib\xlrd-0.9.3\setup.py’)
- Run command line(cmd.exe)
- Type ‘python setup.py install’ inside of opened console

## Usage

Currently (WIP) the only way to use this tool is from the command line:

    $ python xlExpenses.py <bankName> <creditDebitFile> <xlType> <generalExpensesFile>

## Contributors

See https://github.com/golanb7108/xl-my-expenses/watchers
