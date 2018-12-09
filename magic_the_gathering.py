import random

deck = ["island", "island", "island", "island", "island",

        "island", "island", "island", "island", "island",

        "island", "island", "island", "island", "island",

        "island", "island", "island", "island", "island",

        "island", "island", "island", "island", "island ",

        "counterspell", "counterspell", "counterspell", "counterspell",

        "Teferi hero of Dominaria", "Teferi hero of Dominaria",

        "Teferi hero of Dominaria", "Wrath of God", "Wrath of God", "Wrath of God",

        "Search for Azcanta", "Search for Azcanta","Search for Azcanta",

        "Search for Azcanta", "Settle the Wreckage", "Settle the Wreckage", 

        "Settle the Wreckage", "Settle the Wreckage", "Path to Exile",

        "Path to Exile","Path to Exile","Path to Exile", "Snapcaster mage",

        "Snapcaster mage","Snapcaster mage","Snapcaster mage", "Termiinus",

        "Termiinus","Termiinus","Termiinus", "Jace the mindsculpter",

        "Jace the mindsculpter", "Swords to Plowshare", "Swords to Plowshare","Swords to Plowshare"]
# When making a list, there is no need to put -> :

hand = 7 # The amount of strings we want to pull
    

opening_hand = random.sample(deck, hand) # hand of seven is being pulled from the deck



opening_hand = random.sample(deck, hand)


print(opening_hand) # pulls seven strings randomly from deck
    
