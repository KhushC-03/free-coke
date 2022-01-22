import requests
import cloudscraper
import random
import os
os.system('cls')

headers = {
    'Host': 'prod.api.atscale.digital',
    'Content-Length': '0',
    'Sec-Ch-Ua': '"Chromium";v="97", " Not;A Brand";v="99"',
    'Content-Type': 'application/json',
    'Sec-Ch-Ua-Mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'Campaignid': '61daefc99f0e07129c4a87af',
    'Sec-Ch-Ua-Platform': '"macOS"',
    'Accept': '*/*',
    'Origin': 'https://www.thiszeroisonus.com',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.thiszeroisonus.com/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
}


def getLocalStores(POSTCODE):
    CloudScraper = cloudscraper.create_scraper()
    r = CloudScraper.get(f'https://postcodes.io/postcodes/{POSTCODE}',timeout=10)
    if r.status_code == 200:
        longitude = r.json()['result']['longitude']
        latitude = r.json()['result']['latitude']

    print('\x1b[1;36mCopy the id of the store you would like to enter!')
    t = requests.post('https://prod.api.atscale.digital/api/user/locations', headers=headers,json={"latitude":latitude,"longitude":longitude}, verify=True,timeout=10)
    for store in t.json()['data']:
        print(f'{store["originalAddress"]} | ID: {store["_id"]}')
    input()
    menu()

class freecoke():
    def __init__(self,email,name,surname,storeid):
        self.v = requests.Session()
        self.NAME  = name
        self.SURNAME = surname
        if not '@' in email:
            self.EMAIL = f'{self.NAME}{self.SURNAME}{random.randint(10,1000000)}@{email}'
        else:
            self.EMAIL = email
        self.STOREID = storeid
    
    def headers(self):
        return {
            'Host': 'prod.api.atscale.digital',
            'Content-Length': '0',
            'Sec-Ch-Ua': '"Chromium";v="97", " Not;A Brand";v="99"',
            'Content-Type': 'application/json',
            'Sec-Ch-Ua-Mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
            'Campaignid': '61daefc99f0e07129c4a87af',
            'Sec-Ch-Ua-Platform': '"macOS"',
            'Accept': '*/*',
            'Origin': 'https://www.thiszeroisonus.com',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://www.thiszeroisonus.com/',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        }
      
    def checkuser(self):
        r = self.v.post(f'https://prod.api.atscale.digital/api/user/check-user/{self.EMAIL}', headers=self.headers(), verify=True)
        if r.json()['result'] == True:
            print('\x1b[1;36mEmail Submitted Successfully!')
            self.submitEntry()
        else:
            print('\x1b[1;31mEmail Already Used :(')
    
    def submitEntry(self):
        date = random.randint(1,28)
        month = random.randint(1,12)
        year = random.choice([1997,1998,1999,2000,2001,2002,2003])
        signupData = {
            "firstName":self.NAME,
            "lastName":self.SURNAME,
            "email":self.EMAIL,
            "terms":True,
            "date":f"05/05/2000",
            "country":"United Kingdom of Great Britain and Northern Ireland (the)",
            "socialType":"organic",
            "venueId":self.STOREID
        }
        
        r = self.v.post('https://prod.api.atscale.digital/api/user/signup', headers=self.headers(),json=signupData, verify=True)
        if r.json()['result'] == True:
            print('\x1b[1;32mDrink Fetched - Check Email!')
        else:
            print('\x1b[1;31mError Fetching Drink')


def menu():
    print('\x1b[1;37m')
    print(' [1] Get Store IDS')
    print(' [2] Get Drinks')
    print('-------------------')
    I1 = input(' >')
    if I1 == '1':
        postCode = input('Input your postcode: ')
        getLocalStores(postCode)
    else:
        howmany = input('How many would you like to get? ')
        catchall = input('Enter your catchall (without @) or email: ')
        name = input('Enter your name: ')
        surname = input('Enter your surname: ')
        storeID = input('Enter your store ID: ')
        for i in range(int(howmany)):
            freecoke(catchall,name,surname,storeID).checkuser()
        menu()

menu()


