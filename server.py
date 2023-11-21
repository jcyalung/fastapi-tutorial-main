from fastapi import FastAPI
import uvicorn
import random

app = FastAPI()

card_values = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven","Eight","Nine","Ten","Jack","Queen", "King"]
card_suits = ["Spades","Diamonds","Clubs","Hearts"]

def deck(card_values, card_suits):
    card_deck = []
    for i in range(0, len(card_suits)):
        for j in range(0, len(card_values)):
            card_deck.append(card_values[j] + " of " + card_suits[i])
    return(card_deck)

card_deck = deck(card_values, card_suits)

@app.get("/")
def root():
    return({ "message": "hello world" })

@app.get("/flip-coin")
def flip_coin():
    val = random.random()
    head_tail = ""
    if(val <= 0.5):
        head_tail = "heads"
    else:
        head_tail = "tails"
    return({ "value": head_tail })

@app.get("/flip-coins")
def flip_coins(times: int = 10):
    if times and times > 0:
        head_count = 0
        tail_count = 0
        for i in range(times):
            val = random.random()
            if(val <= 0.5):
                head_count += 1
            else:
                tail_count += 1
        return({ "heads": head_count, "tails": tail_count })
    else:
        return({ "message": "you need to send valid times" })


@app.get("/draw-card")
def draw_card():
    card_deck = deck(card_values, card_suits)
    val = random.uniform(0, 51)
    drawn = card_deck[int(val)]
    return({"Card" : drawn})

@app.get("/draw-cards")
def draw_cards(times: int = 5):
    if times and times > 0:
        drawn = {}
        for i in range(times):
            val = random.uniform(0,52)
            drawn[card_deck[int(val)]] = 1
        return(drawn)
    else:
        return({"message": "you need to send valid times"})

@app.get("/random-digit/{num}")
def random_digit(num: int):
    if num and num < 0:
        return ({"message": "you need to send valid times"})
    val = random.uniform(0, num)
    return({"Digit": int(val)})


if __name__ == "__main__":
    uvicorn.run("server:app", port=8000, reload=True)