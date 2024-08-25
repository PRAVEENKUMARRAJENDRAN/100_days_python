from random_word import RandomWords

class Hangman:
    def __init__(self):
        self.live_images = stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


    def word_generator(self):
        r = RandomWords()
        word_guess = r.get_random_word()

        return word_guess

    def guess_generator(self, word_len):
        guess_word = []
        for i in range(word_len):
            guess_word += "_"  
        return guess_word


    def letter_gap_fillers(self, word_array, letter, guess_word):
        for i, l in enumerate(word_array):
            if l == letter:
                guess_word[i] = letter




    def lives_saver(self):
        word = self.word_generator()
        word_len = len(word)
        
        guess_word = []
        for _ in range(word_len):
            guess_word += "_"

        print(word, word_len, guess_word, len(guess_word))

        lives = 6

        while(lives):
            
            if '_' not in guess_word:
                print("You Won!")
                return 

            letter_guess = input("Guess a letter: ")
            word_array = list(word)

            if letter_guess not in word_array:
                print("You guessed {0}, that's not in the word. You lose a life.".format(letter_guess))
                lives -= 1

                print(self.live_images[lives])

            else:
                self.letter_gap_fillers(word_array, letter_guess, guess_word)
                print(guess_word)
                print(self.live_images[lives])

    




if __name__ == '__main__':
    h = Hangman()
    print("Hangman Problem")
    h.lives_saver()
