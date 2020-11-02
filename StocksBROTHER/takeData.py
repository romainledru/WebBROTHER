import requests
from bs4 import BeautifulSoup


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"}

""""
The class is written do extract data from Yahoo Finance
If the user wants to exact data from an other source, class_ should be modified in takeData()
"""

class TakeData():
    def __init__(self, url, headers=headers): # a working user-agent is provided as default. But any new user could give it's own headers
        self.page = requests.get(url, headers=headers)
        self.soup = BeautifulSoup(self.page.content, "html.parser")


    def findPrice(self):
        """Data Extract Function: from html page

        Returns:
            float: price from stock
        """

        return float(self.soup.find(class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)").get_text())
    

    def findEvolution(self):
        """Data Extract Function: from html page

        Returns:
            float: moving value and % value from stock
        """

        rawData = self.soup.find(class_="Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)").get_text()
        value, evol = self.organiseEvolutionData(rawData) # evol is in %
        return value, evol
    

    def organiseEvolutionData(self,rawData):
        """Data Transformation Function: from a String raw data to a float computable data

        Args:
            rawData (str): data from the html page

        Returns:
            float: computable data
        """

        listRawData = rawData.split()
        value, evol = listRawData[0],listRawData[1]
        for char in ("(",")","%"):
            evol = evol.replace(char,"")
        return float(value), float(evol)
