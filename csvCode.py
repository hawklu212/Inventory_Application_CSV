import csv
from tkinter import *
from tkinter import ttk


def readCSV(filetxt,str,foc):
    with open(filetxt) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                if foc==row[0] or foc==row[1] or foc =="All":
                    str += (f'{row[2]}            {row[3]}            {row[4]}\n')
                line_count += 1
    return str


def createcsventry(filetxt,category,product,name,price,quantity):

    if (category=='' or product== '' or name == '' or price=='' or quantity==''):
        return "Missing Fields to create Item"

    with open(filetxt) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                if name==row[2]:
                    return "Product is a duplicate, not Created"

    data = [category,product,name,'$'+price,quantity]
    file = open(filetxt, 'a',newline='', encoding='UTF8')
    writer = csv.writer(file)
    writer.writerow(data)
    file.close()
    return "Success, Item Created"

def deleteentry(filetxt,name):
    if name=='':
        return "No input given,\n at least product name must be specified"
    tracklist = list()
    marker= True
    with open(filetxt) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                tracklist.append(row)
                line_count += 1
            else:
                if name!=row[2]:
                    tracklist.append(row)
                else:
                    marker=False
                line_count += 1
        if marker:
            return "Item does not exist to Delete"
    with open(filetxt, 'w',newline='') as writeFile:

        writer = csv.writer(writeFile)

        writer.writerows(tracklist)
    return "Success, item was deleted"

def modifyentry(filetxt,category,product,name,price,quantity):
    if (category == '' or product == '' or name == '' or price == '' or quantity == ''):
        return "Missing  Fields"
    tracklist = list()
    marker= True
    with open(filetxt) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                tracklist.append(row)
                line_count += 1
            else:
                if name!=row[2]:
                    tracklist.append(row)
                else:
                    marker=False
                    tracklist.append([category,product,name,price,quantity])
                line_count += 1
        if marker:
            return "Item does not exist to Modify"
    with open(filetxt, 'w',newline='') as writeFile:

        writer = csv.writer(writeFile)

        writer.writerows(tracklist)
    return "Success, item was Modified"

def exportcsv(filetxt,csvName):
    orig=list()
    if csvName=='':
        return "Filename parameter required"
    if not csvName.endswith('.csv'):
        return "Filename must end with .csv"
    with open(filetxt) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                orig.append(row)
                line_count += 1
            else:
                orig.append(row)
    with open(csvName, 'w',newline='') as writeFile:

        writer = csv.writer(writeFile)

        writer.writerows(orig)
        return "New File Successfully exported"