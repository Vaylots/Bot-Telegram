from bs4 import BeautifulSoup
import requests

def parsing_monday():
    url = 'https://animedub.ru/raspisanie.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('div', id='raspisanieMont')

    mass = []
    anime_Monday = ''

    for quote in quotes:	
        mass.append(quote.text)

    for i in mass:
        anime_Monday = anime_Monday + i + '\n'

    return anime_Monday
     
        
def parsing_tuesday():
    url = 'https://animedub.ru/raspisanie.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('div', id='raspisanieTuet')

    mass = []
    anime_Tuesday = ''

    for quote in quotes:	
        mass.append(quote.text)

    for i in mass:
        anime_Tuesday = anime_Tuesday + i + '\n'

    return anime_Tuesday


def parsing_wednesday():
    url = 'https://animedub.ru/raspisanie.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('div', id='raspisanieWedt')

    mass = []
    anime_Wednesday = ''

    for quote in quotes:	
        mass.append(quote.text)

    for i in mass:
        anime_Wednesday = anime_Wednesday + i + '\n'
    
    return anime_Wednesday
 

def parsing_thursday():
    url = 'https://animedub.ru/raspisanie.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('div', id='raspisanieThut')

    mass = []
    anime_Thursday = ''

    for quote in quotes:	
        mass.append(quote.text)

    for i in mass:
        anime_Thursday = anime_Thursday + i + '\n'
    
    return anime_Thursday
    

def parsing_friday():
    url = 'https://animedub.ru/raspisanie.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('div', id='raspisanieFrit')

    mass = []
    anime_Friday = ''

    for quote in quotes:	
        mass.append(quote.text)

    for i in mass:
        anime_Friday = anime_Friday + i + '\n'

    return anime_Friday

def parsing_saturday():
    url = 'https://animedub.ru/raspisanie.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('div', id='raspisanieSunt')

    mass = []
    anime_Saturday = ''

    for quote in quotes:	
        mass.append(quote.text)

    for i in mass:
        anime_Saturday = anime_Saturday + i + '\n'
    
    return anime_Saturday

def parsing_sunday():
    url = 'https://animedub.ru/raspisanie.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('div', id='raspisanieSunt')

    mass = []
    anime_Sunday = ''

    for quote in quotes:	
        mass.append(quote.text)

    for i in mass:
        anime_Sunday = anime_Sunday + i + '\n'
    
    return anime_Sunday










