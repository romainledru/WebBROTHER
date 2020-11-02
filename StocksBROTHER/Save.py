import json
import csv
import sys
import os
import datetime


class Save:
    def __init__(self,fileName):
        self.fileName = fileName
        self.existQuestion()
    

    def existQuestion(self):
        """Checking Function: check if file already exist. If not, a new one is created with a header.
        The function is usualy called on a new day: Each day has its .csv file (useful for data processing)
        """

        if not os.path.isfile(self.fileName):
            header = ["time","value"]
            with open(self.fileName,"w") as newCsvFile:
                writer = csv.DictWriter(newCsvFile, fieldnames=header)
                writer.writeheader()
        

    def downloadJson(self):
        """Json read Function: Used to track URLs
        this function is used to read "data.json"

        Returns:
            dict: json content of tracked URLs
        """

        with open(self.fileName,'r') as file:
            return json.loads(file.read())


    def writeLineCsv(self,lineData):
        """Store Data Function: add a new line on a csv file
        this function is used by storeDataInCsv(price).
        

        Args:
            lineData (list): [current time, price]
        """

        with open(self.fileName, "a") as csvFile:
                writer = csv.writer(csvFile, delimiter=',')
                writer.writerow(lineData)
        

    def downloadCsv(self):
        """Test Function.
        gives acces to a csv file and also possible automatic writing problem
        """

        with open(self.fileName, newline='') as csvFile:
            reader = csv.reader(csvFile)
            try:
                for row in reader:
                    print(row)
            except csv.Error as e:
                sys.exit('file {}, line {}: {}'.format(self.fileName, reader.line_num, e))
    

    def storeDataInCsv(self,price):
        """Store Data Function: write a line on Csv file

        Args:
            price (float): price of the current stock
        """

        timeCurrent = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.writeLineCsv([timeCurrent,price])
