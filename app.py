import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
move = open("./moves.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)
moves = json.load(move)
# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.
for i in range(0, 809):
    name = data[i]["name"]["english"]
    print(f"{i + 1}: {name}")
# Add a language choice feature and print the pokemons name based on the user input
choose = input("Would You Like A Different Language Option (Yes/No): ")
chose = choose.upper()
if chose == "YES":
    language = input("What Language Do You Want It To Be In: (English, Japanese, Chinese, French): ")
    for l in range(0, 809):
        name = data[l]["name"][f"{language.lower()}"]
        print(f"{l + 1}: {name}")
# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user
if chose == "NO":
    language = "english"
    print("ok")
type = input("Would You Like To Find A Specific Type (Yes/No): ")
if type.upper() == "YES":
    type_type = input("What Type Do You Want To Find: ")
    type_type = type_type.lower()
    type_type = type_type.capitalize()
    for t in range(0, 809):
        if type_type in data[t]["type"]:
            name = data[t]["name"][f"{language.lower()}"]
            print(f"{t + 1}: {name}")
if type.upper() == "NO":
    print("ok")
    type_type = None
#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 
find = input("Do You Want To Find A Pokemon (Yes/No): ")
find = find.upper()
if find == "YES":
    letter = input("What Pokemon Do You Want To Search For: ")
    letter = letter.lower()
    letter = letter.capitalize()
    for f in range(0, 809):
        if letter in data[f]["name"]["english"]:
            name = data[f]["name"][f"{language.lower()}"]
            print(f"{f + 1}: {name}")
if find == "NO":
    print("ok")
#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!
pick = input("Type A Pokemon: ")
pick = pick.lower()
pick = pick.capitalize()
for p in range(0, 809):
    if pick == data[p]["name"]["english"]:
        for m in moves:
            if moves[m]["type"]    
            learn = moves["ename"]
            print(learn)
