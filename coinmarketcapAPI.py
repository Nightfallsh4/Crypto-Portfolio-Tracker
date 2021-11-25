 Documentation for the used api at https://coinmarketcap.com/api/documentation/v1/#section/Quick-Start-Guide


"""This is a program to make api calls to coinmarketcap.com and get back data on specific coins"""

import requests, time

api_key = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"

class CMC:

    def __init__(self,key):
        """The class defines an API object of coinmarketmap.com"""
        self.api_key = key
        self.url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
        self.dic = {}
        e = str(input("Enter the name of the coin(s) you want to check the price of\nAdd a comma in between to check multiple coins \neg. bitcoin,ethereum,polkadot = ")).lower()
        self.list = e.split(",")    #splits the string type inputs at ',' into a list
        
        for i in self.list:
            self.dic[i] = None      #creates a key,value pair for all the entered coins as NONE to be updated later
        
        self.parameters = {'slug':e, 'convert': 'INR'}      #creates parameters attribute which contains the coins string and the FIAT currency convertion(like either USD,CAD,EUR)
        self.headers = {'Accepts': 'application/json','X-CMC_PRO_API_KEY': self.api_key}        #defines a headers attribute containing the api key and the format the data is returned 
        print("Setup done\n")


    def getprice(self):
        """Gets the price of the inputted coin(s) and prints the name and price of the coin(s)"""
        print("Getting price....\n")
        data = requests.get(self.url, params = self.parameters, headers = self.headers)     # Queries the coinmarketcap api for the coins inputted in the specified currency
        if data.status_code != 200:     #checks the recieved status code for successful query. if not successful it print an error message and exits the application
            print("There was an error in the server please try again in a few seconds.")    
            time.sleep(5)
            exit()
        d = data.json()

        for i in d['data']:     #Iterates through the data recieved and prints the name and price of the coin
            print(f"{d['data'][i]['name']} - Rs.{d['data'][i]['quote']['INR']['price']}")
            print()
    

    def calculate_portfolio(self):
        """Queries the price of the coins and gets input of the amount of each coin you have to calculate the current size of your portfolio"""
        print("Getting price....\n")
        data = requests.get(self.url, params = self.parameters, headers = self.headers)     # Queries the coinmarketcap api for the coins inputted in the specified currency
        if data.status_code != 200:     #checks the recieved status code for successful query. if not successful it print an error message and exits the application
            print("There was an error in the server please try again in a few seconds.")
            time.sleep(5)
            exit()
        d = data.json()
        total = 0
        for i in d['data']: #takes input of the amount of each of the coins and updates self.dic attribute
            while True:
                try:
                    num = float(input(f"Enter the number of {d['data'][i]['name']} you have:- "))
                    break
                except:
                    print("Enter only numbers!!!")
                    time.sleep(3)
            self.dic[i] = num 
            price = num * float(d['data'][i]['quote']['INR']['price'])
            total = total + price
        print()
        for i in d['data']:
            print(f"{d['data'][i]['name']}- {self.dic[i]} = {float(d['data'][i]['quote']['INR']['price'])*self.dic[i]}")
        print()
        print(f"Total porfolio size- {total}")
        
cmc = CMC(key=api_key)
cmc.getprice()
cmc.calculate_portfolio()
