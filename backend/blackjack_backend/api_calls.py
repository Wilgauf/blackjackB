import requests

defaultURL = "http://deckofcardsapi.com/api/deck/"
#Need to start with a DeckID so this first Function creates one for the game and shuffles it
def create_a_deck():
    response = requests.get(defaultURL+ "new/shuffle/?deck_count=1")
    if response.json()["success"] :
        #print(response.json())
        return response.json()['deck_id']
    else:
        print("Request Failed with not ok status")

# deck_id = create_a_deck()
# defaultURL = defaultURL+deck_id+"/"
# print(deck_id)

def shuffle(deck_id):
    r = requests.get(f'{defaultURL}{deck_id}/shuffle/')
    if not r.json()['success']:
        print("Error, deck was not shuffled. please try again")

#draws given number of cards. Creates new deck and draws cards if deck_id=new
def draw_card(deck_id, num=1):
    response = requests.get(f'{defaultURL}{deck_id}/draw/?count={num}')
    if response.json()["success"]:
        deck = response.json()["deck_id"]
        this_hand = []
        for card in response.json()["cards"]:
            this_hand.append(card["code"])
        if deck_id == 'new':
            data = {'deck_id': deck, 'cards' : this_hand}
        else :
            data = this_hand
        if response.json()["remaining"] <= 10:
            shuffle(deck_id)
        return data
    else:
        print("Response error, retry request")

#Next we need to draw cards from the deck and then set them to the respective hand
# def deal_a_hand(player_name="Wilson"):
#     response = requests.get(defaultURL+ "draw/?count=2")
#     if response.json()["success"]:
#         this_hand = []
#         for card in response.json()["cards"]:
#             this_hand.append(card["code"])
#             # print(card["value"])
#         # print(this_hand)
#     else:
#         print("Response error, retry request")
#     set_hand(player_name, this_hand)


# #Setting the drawn cards to a pile in the API so they can be tracked and added to.
# def set_hand(pile_name, hand):
#     cards = ",".join(hand)
#     response = requests.get(defaultURL + "/pile/"+ pile_name + "/add/?cards=" + cards)
#     if response.json()["success"]:
#         return 
#     else:
#         print("Error when trying to add cards to pile")

# deal_a_hand()


# #If the user wants to hit their hand calling this function will draw a new card then add it to their pile
# def hit_a_hand(pile_name):
#     new_card = ""
#     response = requests.get(defaultURL+ "draw/?count=1")
#     if response.json()["success"]:
#         # print(response.json())
#         new_card = response.json()["cards"][0]["code"]
#         add_to_pile(pile_name, new_card)
#     else:
#         print('Error requesting an additional card')

# #Adding the recently drawn card to the user's pile
# def add_to_pile(pile_name, card):
#     response = requests.get(defaultURL+ '/pile/' + pile_name + "/add/?cards="+card)
#     if  response.json()["success"]:
#         get_cards_in_pile(pile_name)
#     else:
#         print("Error adding card to pile")

# #Returns all the information from the users current pile
# def get_cards_in_pile(pile_name):
#     response = requests.get(defaultURL+ '/pile/' + pile_name + "/list/")
#     hand = []
#     if response.json()["success"]:
#         cards = response.json()["piles"]["Wilson"]["cards"]
#         for card in cards:
#             hand.append(card["code"])
#         #Can change to a return statement if needed    
#         print(hand)
#     else:
#         print("Error listing pile with given pile name: " + pile_name)

# hit_a_hand("Wilson")