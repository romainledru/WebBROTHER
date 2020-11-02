# StocksBROTHER

StocksBROTHER is a Python script that look at the stocks market evolution, send email if a stock is becoming interessant to buy, and store data.

StocksBROTHER is built to be always running (I use it on my RaspberryPI which is also a Hub/Server for connected objects in my house)

## How does it works

1. The script is running in background in infinite loop and makes a requests of the prices each hour.
2. If a price is becoming interessant (big fall for example), then a email is send to the user with the interessant stock link.
3. Prices are stored in a stock-organised data directory in order to be processed from a Data Analysis Python Script.

The script does not look at the entire market. If you find an interessant stock to follow, you have to enter it in data.json (name + url)

## Idea

I am interested in stocks. But I realised that I spend a lot of time looking at the market, affraid to miss "the right time to buy".
I was really a time consuming. I decided to makes someone else do the job so I can concentrate on learning Python :wink:

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the needed libraries.

```bash
python -m pip install time, datetime, os, json, csv, sys
python -m pip install smtplib
python -m pip install requests
python -m pip install bs4
```

time, datetime, os, json, csv, sys should already be installed by default on python installation

## Make the script working for your needs

1. Customize the data.json: write the stocks you want to follow (by default: Air Liquide, Tesla, Adidas)
2. Create 2 files: txt.pswd and txt.username (these are simple txt files but with another extention)
    * txt.pswd contains the password of the email adress
    * txt.username contains the username of the email adress
    - !! Email adress used as sender should be a gmail account !!
    - theses informations are stored in external data for privacy. Since data are not written in the programm itself, I don't need to secure theses informations. The only secure is: they are with an other extention to distract user from opening it
3. Change the email destination
    * by default, the email sender and email destination are the same. If you want to change it, place an extra argument here:

run.py
```python
28 email.send(urlsDict[keyUrl],"EMAILADRESS@DESTINATION.COM")
```
## User-Agent Problem ?

A default user-agent is provided. It could be obsolet in a few years.
You can easily change it by typing on google: "What is my user-agent".

## Usage

```python
cd StocksBROTHER
python3 run.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

To contribute to GermanOK, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## Contact

If you want to contact me, you can reach me at romain.ledru2@gmail.com

### Next Steps!

Well, if you are still reading, that maybe means that you are interested in the project.

I want to continue updating StocksBROTHER this way:

* Allow more visited financial website
* Allow more destination email adress (add friends for example)

Feel free to propose new ideas! :smiley: