import random

deck_of_cards = ['Ace of Hearts','Two of Hearts','Three of Hearts',
'Four of Hearts','Five of Hearts','Six of Hearts','Seven of Hearts',
'Eight of Hearts','Nine of Hearts','Ten of Hearts','Jack of Hearts',
'Queen of Hearts','King of Hearts','Ace of Diamonds','Two of Diamonds',
'Three of Diamonds','Four of Diamonds','Five of Diamonds','Six of Diamonds',
'Seven of Diamonds','Eight of Diamonds','Nine of Diamonds','Ten of Diamonds',
'Jack of Diamonds','Queen of Diamonds','King of Diamonds','Ace of Spades',
'Two of Spades','Three of Spades','Four of Spades','Five of Spades',
'Six of Spades','Seven of Spades','Eight of Spades','Nine of Spades',
'Ten of Spades','Jack of Spades','Queen of Spades','King of Spades',
'Ace of Clubs','Two of Clubs','Three of Clubs','Four of Clubs','Five of Clubs',
'Six of Clubs','Seven of Clubs','Eight of Clubs','Nine of Clubs','Ten of Clubs',
'Jack of Clubs','Queen of Clubs','King of Clubs']

print('Choose a number 1 through 52: ')
print('Or, if you want a random card, type "random":')
card_choice = input('> ')

if card_choice == 'random':
    a_random_card = random.choice(deck_of_cards)
    print(f'Great! The card you have is the {a_random_card}')
    print('Would you like to pick another random card?')
else:
    the_card = int(card_choice)
    print(f'Great! The card you have is the {deck_of_cards[the_card]}')
    print('Pick another card: ')
    card_choice = input('> ')
