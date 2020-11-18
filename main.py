from Hangman import Hangman 
#From the file hangman.py, import the python program hangman 
print("Welcome to Hangman!\n")
#print welcome message to player 
play = input("Would you like to play a game? (y/N) ")
#Looking for input from user y/n
if play.lower() != "y":
#if the response (lowercase) is not equal to "y", give the goodbye message and exit python
   print("Maybe later! Goodbye!")
#print goodbye message 
   exit()
#Exit python 
play_again = True
#this is to repeat the game if the player wants to play again after winning/losing the game 
game = Hangman()
#instructions for the variable game 
game.initialize_file('words.dat')
#using a data file of words for the user to guess
while play_again and game.num_words_available > 0:
#if the user wants to play again and hasn't used up all the words, then continue the program 
   print("Starting game.")
#print line of text 
   game.display_statistics()
#displays the statistics of the number of games played, and how many have been won/lost, as well as how many words are left in
#the word bank 
   print("\n")
#reprint the input the user entered 
   game.new_word()
#generate a new word 
   while not game.game_over:
#while the player is still playing 
      game.display_game()
#display the blank hangman template 
      user_guess = input("Enter a letter to guess. ")
#prompt user for input 
      if not user_guess.isalpha():
#if the guess is not a letter....
         print("Sorry, I don't understand. That's not a letter. \n")
#print this statement along with what they input 
      elif not game.guess(user_guess.upper()):
#if user already guessed that letter...
         print("Sorry, you've alread guessed that letter. \n")
#print this statement along with what letter the user input 


   game.reveal_word()
#show the word that the user was trying to guess 
   game.display_statistics()
#reprint the game statistics: how many won/lost/number of words left 
   game.game_over = False
#game is not over 
   again = input("Would you like to play again? (y/N)")
#prompt user for input to play again 
   if again.lower() != "y":
#if user inputs anything other than y, then... 
      play_again = False
#then the game is over and the program will...
print("Thanks for playing! Goodbye!")
#display this text on the screen 
exit()
#and exit python3 
