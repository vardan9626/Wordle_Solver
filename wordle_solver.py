# This class is for creating a word list for out wrodle solver
class Word_List():
    
    # This function decides the file to take words from
    def __init__(self, filename):
        self.filename = filename
        self.words = []
        with open(self.filename, 'r') as file:
            self.words = file.read().split()

    # this function return a wordlist with words of only a specific length specified by the user
    def words_of_size(self, word_size):
        return (list(filter(lambda x: len(x) == word_size, self.words)))


class Wordle_Solver(Word_List):
    
    # This constructor defines a solver  with a word list of a given size and a 
    def __init__(self, word_size, filename):
        super().__init__(filename)
        self.__define_word_size(word_size)

    def __str__(self) -> str:
        description = f"This is a wordle solver class which is used to solve wordle quiz of {self.word_size}"
        return description
    
    # This is the function which decides which word to take in a list and which words not to take
    @staticmethod
    def filter_function(guess, result, list_word):
    # Check for 'g' (green) condition
        for i in range(len(result)):
            if result[i] == 'g' and guess[i] != list_word[i]:
                return False
            elif result[i] == 'y' and guess[i] == list_word[i]:
                return False

        # Create lists of letters to be included or excluded based on the result
        include_letters = [guess[i] for i in range(len(result)) if result[i] != '_']
        exclude_letters = [guess[i] for i in range(len(result)) if result[i] == '_']

        # Check for 'y' (yellow) condition
        for letter in include_letters:
            if letter not in list_word:
                return False
            list_word = list_word.replace(letter, "", 1)

        # Check for '_' (not in word) condition
        for letter in exclude_letters:
            if letter in list_word:
                return False

        return True


    # This method will define the number of letters that each word can have
    # it is also used as a way to redefine the parameters of the solver
    def __define_word_size(self, word_size):
        self.word_size = word_size
        self.useful_words = self.words_of_size(word_size)
        self.useful_words.sort()

    # this method gets the possible answers for the wordle problem
    def get_ans(self, guess, result):
        ans = []
        for list_word in self.useful_words:
            if self.filter_function(guess, result, list_word):
                ans.append(list_word)
        self.useful_words = ans
        return ans

    # this method is used to reset the parameters of the class
    def new_word(self):
        word_size = int(input('What is the size of the word: '))
        self.__define_word_size(word_size)


if __name__ == "__main__":
    word_size = int(input('What is the size of the word: '))
    solver = Wordle_Solver(word_size, "words.txt")
    while True:
        guess = input("Enter your guess: ")
        result = input("Enter your result: ")
        if (len(guess) != word_size or len(result) != word_size):
            raise ValueError("Enter a string of valid length")
        ans = solver.get_ans(guess, result)
        print(f"Your possible answers are {ans[:]}")
        continue_guessing = int(input(
            "Enter 1 if you want to continue searching this word 0 if you to guess a new word: "))
        if continue_guessing == 0:
                solver.new_word()       
