import smtplib


class Emailing():
    def __init__(self):
        self.server = smtplib.SMTP("smtp.gmail.com",587)
        self.server.ehlo()
        self.server.starttls()
        self.server.ehlo()

        self.destination = self.takeData("txt.username")

        self.server.login(self.takeData("txt.username"),self.takeData("txt.pswd"))
        # username and password are not communicated.
        # I do not need to secure the file: I use only txt but with an other extention to distract the user from opening it :)


    def takeData(self,dataName):
        """Security Function: sensible values are taken from external files

        Args:
            dataName (str): file path

        Returns:
            str: content of the file
        """

        with open(dataName,"r") as file:
            data = file.read()
            file.close()
        return data
    

    def send(self,url,destination=None): # TO USER: by default, destination = sender. You can change the destination by adding an argument in the function call (in run.py)
        """Emailing Function: content of email is edited here

        Args:
            destination (str): email Adress from destination
            url (str): this url link from the interesant stock is provided in the email
        """
        
        if destination == None:
            destination = self.destination

        subject = "Prices are falling !"
        body = "Check out the link: {}".format(url)
        
        msg = f"Subject: {subject}\n\n{body}"

        self.server.sendmail(self.takeData("txt.username"),destination,msg)
            
        print("Email Sent")
        self.server.quit()
