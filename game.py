card_values = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven","Eight","Nine","Ten","Jack","Queen", "King"]
card_suits = ["Spades","Diamonds","Clubs","Hearts"]

def deck() -> list:
    card_deck = []
    for i in range(0, len(card_suits)):
        for j in range(0, len(card_values)):
            card_deck.append(card_values[j] + " of " + card_suits[i])
    return(card_deck)

