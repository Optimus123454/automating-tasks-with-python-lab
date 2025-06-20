import requests
import webbrowser
import sys

#Headers to add to get requests
headers = {'User-Agent': 'scryfall_card_lookup/1', 'Accept': '*/*'}

#Save default api search url
url = "https://api.scryfall.com/cards/named?fuzzy="

#Get user input for which card to search for
userSearchQuery = input("Please enter the name of the card you would like to search for (Try to be as specific as possible and only use alphanumeric characters): ")

#Replace whitespace with '+' for proper url syntax
userSearchQuery = userSearchQuery.rstrip()
userSearchQuery = userSearchQuery.replace(" ", "+")
userSearchQuery = userSearchQuery.lower()
#print(userSearchQuery) used for testing

#Append user input into the url for proper api url
url = url+userSearchQuery
#print(url) used for testing

#Make response object
r = requests.get(url, headers=headers)
#print(r) used for testing

#Check if response is valid, if it is parse the json data into a dictionary
if r.status_code == 200:
    cardInfo = r.json()

    #Print basic information about the card
    print(f'Card name: {cardInfo['name']}')
    print(f'Mana Cost: {cardInfo.get('mana_cost', 'N/A')}')
    print(f'Type Line: {cardInfo.get('type_line', 'N/A')}')
    print(f'Oracle Text: {cardInfo.get('oracle_text', 'N/A')}')
    print(f'Power/Toughness: {cardInfo.get('power', 'N/A')}/{cardInfo.get('toughness', 'N/A')}')

    #Set the cards scryfall url found in the json to an object for use
    cardURL = cardInfo['scryfall_uri']

    #Display a link that opens to the cards scryfall web page
    print(f"You may manually go to the following link to open the card on scryfall's website: {cardURL}")

#If the response was invalid inform the user and display the error code
else:
    print(f"Error: {r.status_code} Could not find the card. Try to be specific with card names. ex: Atraxa Praetor's Voice  instead of simply 'Atraxa'")