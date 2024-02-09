import random
from words import words
import string

def valid_word():
  word = random.choice(words)
  while '-' in word or ' ' in word:
    word = random.choice(words)
  return word.upper()

def hangman():
  word = valid_word()
  word_letters = set(word)
  alphabet = set(string.ascii_uppercase)
  used_letters = set()
  lives = 6

  while word_letters and lives > 0:
    print('you have ', lives, ' lives left and Letter used : ', ' '.join(used_letters))

    word_list = [letter if letter in used_letters else '_' for letter in word]
    print('Current Word : ', ' '.join(word_list))

    user_letter = input('Guess a letter : ').upper()
    if user_letter in alphabet - used_letters:
      used_letters.add(user_letter)
      if user_letter in word_letters:
        word_letters.remove(user_letter)
      else:
        lives -= 1
        print('Letter is not in word!')
    elif user_letter in used_letters:
      print('Character already used, guess a different letter! : ')
    else:
      print('Invalid Character! Try again.')
  if lives == 0:
    print('You died, the word was :', word)
  else:
    print('You guessed the word', word, 'correctly!')

hangman()