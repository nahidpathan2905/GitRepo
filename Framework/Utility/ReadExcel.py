import openpyxl

class ReadTD:

    @staticmethod
    def getTestData(rowIndex,colIndex):
        workbook = openpyxl.load_workbook(
            "C:\\Users\\mulanii\\PycharmProjects\\Framework\\TestData\\Nahid.xlsx")
        sheet = workbook['Sheet2']

        s2 = sheet.cell(row=rowIndex, column=colIndex).value
        return s2
