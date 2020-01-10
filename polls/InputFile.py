import xlrd

path = 'features.xlsx'


#def inputFeatures(features):
wb = Workbook()
ws = wb.active
ws = wb.load_workbook('/data/features.xlsx')
a = wb.cell['A2']
print(a)