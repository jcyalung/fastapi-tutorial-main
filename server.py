from fastapi import FastAPI
import game
import uvicorn
import random

app = FastAPI()



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
    card_deck = game.deck()
    val = random.uniform(0, 51)
    drawn = card_deck[int(val)]
    return({"Card" : drawn})

@app.get("/draw-cards")
def draw_cards(times: int = 5):
    card_deck = game.deck()
    if(times > 52):
        return ({ "message": "you cannot draw more than 52 cards" })
    if times and times > 0:
        drawn = {}
        for i in range(times):
            val = random.uniform(0, len(card_deck))
            drawn[card_deck[int(val)]] = 1
            card_deck.pop(int(val))
        return(drawn)
    else:
        return({"message": "you need to send valid times"})

@app.get("/random-digit/{num}")
def random_digit(num: int):
    if num and num < 0:
        return ({"message": "you need to send valid times"})
    val = random.uniform(0, num)
    return({"Digit": int(val)})

@app.get("/print-deck")
def print_deck():
    card_deck = game.deck()
    deck_str = ""
    for i in range(len(card_deck)):
        if i == len(card_deck) - 1:
            deck_str += card_deck[i]
        else:
            deck_str += card_deck[i] + ", "
    return ({"Deck:" : deck_str})

if __name__ == "__main__":
    uvicorn.run("server:app", port=8000, reload=True)