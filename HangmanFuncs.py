
MAX_TRIES = 6
def open_game():
    HANGMAN_ASCII_ART = """    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \\
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                       |___/"""
    print(HANGMAN_ASCII_ART,'\n',MAX_TRIES)


def check_valid_input(letter_guessed, old_letters_guessed):
    if(letter_guessed.__len__() > 1 or not letter_guessed.isalpha() or letter_guessed.lower() in old_letters_guessed):
        return False
    if(letter_guessed.__len__() == 1 and letter_guessed.isalpha() and not(letter_guessed.lower() in old_letters_guessed)):
        return True



def try_update_letter_guessed(letter_guessed, old_letters_guessed, secret_word):
    if(check_valid_input(letter_guessed, old_letters_guessed)):
        old_letters_guessed.append(letter_guessed.lower())
        return is_letter_in_secret_word(letter_guessed, secret_word)
    else:
        return handle_mistake(old_letters_guessed)
        
def is_letter_in_secret_word(letter_guessed, secret_word):
    if not secret_word.__contains__(letter_guessed):
        return False
    return True


def handle_mistake(old_letters_guessed):
    print('X')
    print(*sorted(old_letters_guessed), sep=' -> ')
    return False


def show_hidden_word(secret_word, old_letters_guessed):
    for letter in secret_word:
        if not old_letters_guessed.__contains__(letter):
            secret_word = secret_word.replace(letter,"_")
    secret_word = " ".join(secret_word)
    print(secret_word)


def check_win(secret_word, old_letters_guessed):
    for letter in secret_word:
        if not old_letters_guessed.__contains__(letter):
            return False
    return True




def choose_word(file_path, index):
    counts = {}
    inputFile = open(file_path, "r")
    fileData = inputFile.read()
    inputFile.close()
    words = fileData.split(" ")
    for word in words:
        if word not in counts:
            counts[word] = 0
        counts[word] += 1
    chosenWord = words[(index - 1 ) % words.__len__()]
    return (counts.__len__(),chosenWord)






def picture1():
    print("   x-------x")



def picture2():
    print("""    x-------x
    |
    |
    |
    |
    |""")



def picture3():
    print("""    x-------x
    |       |
    |       0
    |
    |
    |""")


def picture4():
    print("""    x-------x
    |       |
    |       0
    |       |
    |
    |""")


def picture5():
    print("""    x-------x
    |       |
    |       0
    |      /|\\
    |
    |""")

def picture6():
    print("""    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |""")


def picture7():
    print("""    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |""")


HANGMAN_PHOTOS = {1:picture1,2:picture2,3:picture3,4:picture4,5:picture5,6:picture6,7:picture7}

def print_hangman(num_of_tries):
    HANGMAN_PHOTOS[num_of_tries]()

        



    

def main():
    pass

if __name__ == "__main__":
    main()

