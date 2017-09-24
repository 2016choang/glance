from parse import getData
import json
import csv

def updateDB():
    data = getData('data.pickle')

    with open('data.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(['Company', 'Keyword', 'Salience'])

        for company in data:
            for pair in data[company]:
                writer.writerow([company,pair[0],pair[1]])

if __name__ == '__main__':
    updateDB()