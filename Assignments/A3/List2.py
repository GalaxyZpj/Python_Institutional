from random import shuffle, choice
def shuffle_deck(deck):
    shuffle(deck)
    return choice(deck)
suit = ("Hearts", "Spades", "Clubs", "Diamonds")
value = (2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace")
deck = []
for s in suit:
    for v in value:
        t = ()
        t += (s,) + (v,)
        deck.append(t)
print(f'{shuffle_deck(deck)[1]} of {shuffle_deck(deck)[0]}')
