import HangmanFuncs

def main():
   pass


num_of_tries = 2
old_letters_guessed = []
HangmanFuncs.open_game()
file_path = input("Please enter a path: ")
word_index = int(input("Please enter a word index: "))
num_of_words_in_file,secret_word = HangmanFuncs.choose_word(file_path,word_index)

HangmanFuncs.print_hangman(1)
HangmanFuncs.show_hidden_word(secret_word,old_letters_guessed)



while(not HangmanFuncs.check_win(secret_word,old_letters_guessed) and num_of_tries < 8):
   user_guess = input("Guess a letter:")
   user_guess = user_guess.lower()
   while not HangmanFuncs.check_valid_input(user_guess,old_letters_guessed):
      HangmanFuncs.handle_mistake(old_letters_guessed)
      user_guess = input("Guess a letter:")
      user_guess = user_guess.lower()

   if HangmanFuncs.try_update_letter_guessed(user_guess,old_letters_guessed, secret_word):
      HangmanFuncs.show_hidden_word(secret_word,old_letters_guessed)
   else:
      print(" :( ")
      HangmanFuncs.print_hangman(num_of_tries)
      num_of_tries += 1
      HangmanFuncs.show_hidden_word(secret_word,old_letters_guessed)

   

if(HangmanFuncs.check_win(secret_word, old_letters_guessed)):
   print("WIN")
else:
   print("LOSE")



#    C:\Users\yarin\Desktop\excercise.txt