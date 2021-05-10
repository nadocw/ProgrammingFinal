# Connor Wertz Final, Python Integers

def getLang():
    lang = input("What language? Choose Spanish or English ")
    lang = lang[0]
    if lang in ["s"]:
        lang = es
        print("Seleccionaste español")
    else:
        lang = en
        print("You selected English")
    return lang

# Get user integer input and determine prime factors
def checkNums(lang):
    print(lang[0])
    num = int(input(lang[1]))
    i = 2
    factors = []

    while 2 < num:
        if num % i == 0:
            factors.append(i)
            num = num / i
        else:
            i += 1
    print(lang[2])

    print(factors)
    print(" ") # Spacing for better viewing
    # Embedded ask function
    ask(lang)

# Loop checkNums or quit program
def ask(lang):
    askToRepeat = input(lang[3])
    askToRepeat = askToRepeat[0]
    if askToRepeat in ["y", "Y", "s", "S"]:
        askToRepeat = "y"
        print(lang[4])
    if askToRepeat in ["no", "No", "n", "N"]:
        askToRepeat = "n"    
        print(lang[5])
        quit()
    # Loop checkNums if user input = yes
    while askToRepeat == "y":
        checkNums(lang)

# en-US
en = [
    "Let's check all the prime factors of a number!",
    "What number do you want to check? ",
    "Your prime factors are: ",
    "Do you want to try this again? Yes or No ",
    "Your response was Yes. Let's do it again! \n",
    "Thank you for checking out my program!"
]

# es-MX
es = [
    "¡Comprobemos todos los factores primos de un número! ",
    "¿Qué número quieres comprobar? ",
    "Tus factores primos son: ",
    "¿Quieres volver a intentarlo? Sí o No ",
    "Tu respuesta fue Sí. ¡Hagámoslo de nuevo! \n",
    "¡Gracias por revisar mi programa!"
]

# On load, get user input.
lang = getLang()
checkNums(lang)