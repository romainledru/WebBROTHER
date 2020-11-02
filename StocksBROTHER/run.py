import time
from Save import Save
from takeData import TakeData
from emailing import Emailing
import datetime
import os


while True:

    urlsExtract = Save("data.json")
    jsonDict = urlsExtract.downloadJson()
    for topic in jsonDict.keys(): # topic: keys on first json level

        try:
            urlsDict = jsonDict[topic][0]
        except IndexError:
            print("No value found on {}".format(topic))
            continue

        for keyUrl in urlsDict: # keyUrl: key on second json level
            valueExtract = TakeData(urlsDict[keyUrl])
            price = valueExtract.findPrice()
            value, evol = valueExtract.findEvolution()

            if evol <= -3: # Email will be sent if the day evolution of an stock fall by 3%
                email = Emailing()
                email.send(urlsDict[keyUrl])

            # pick the actual price and store it in CSV file
            if not os.path.isdir("data/"+keyUrl): # If no directory exist for the stock, create one
                os.mkdir("data/"+keyUrl)
            storeData = Save("data/"+keyUrl+"/"+str(datetime.date.today())+".csv")
            storeData.storeDataInCsv(price)

    time.sleep(60*60) # Wait an HOUR
    
    # I decide to not stop the emailing if prices are still falling above 3% in an hour (I do spam: don't miss this offer!)
