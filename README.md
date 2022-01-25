# UNO-game-agent
An agent that plays the UNO game

# Deck
Uno deck based on ![](UNO_deck.png)

# Running the code
Execute with:
```
python UNO.py
```
To start 2 player UNO game.


Expected output:
```
[uriegas@Dell UNO-game-agent]$ python UNO.py
           )     )   
        ( /(  ( /(   
    (   )\()) )\())  
    )\ ((_)\ ((_)\   
 _ ((_) _((_)  ((_)  
| | | || \| | / _ \  Welcome to UNO GAME from terminal.
| |_| || .` || (_) | You are playing against a machine.
 \___/ |_|\_| \___/  

Eduardo{
        id: 712,
        cards{
                UnoCard{ color: red,    special: colorChange }
                UnoCard{ color: red,    number: 8 }
                UnoCard{ color: blue,   number: 1 }
                UnoCard{ color: blue,   number: 6 }
                UnoCard{ color: blue,   number: 1 }
                UnoCard{ color: red,    number: 9 }
                UnoCard{ color: red,    number: 6 }
                UnoCard{ color: green,  number: 7 }
        }
}
Current card is: None
Insert the number of your selection (Type '?' for help)>
```

# TODO
At the moment the code is fixed to work only for 2 players, it would be desirable to make the code work with multiplayers
Special powers aren't implemented yet.

* Differentiate selected card vs new card (eat card) in terminal