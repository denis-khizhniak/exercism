# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.masked_word = "".join("_" for _ in self.word)

    def guess(self, char):
        if self.status != STATUS_ONGOING:
            raise ValueError("The game is over!")

        try:
            if char in self.masked_word:
                raise ValueError("This char is already opened!")

            self.word.index(char)
            start = 0
            for _ in range(self.word.count(char)):
                char_idx = self.word.index(char, start)
                start = char_idx + 1
                self.masked_word = (
                    self.masked_word[:char_idx]
                    + char
                    + self.masked_word[char_idx + 1 :]
                )
            if self.masked_word == self.word:
                self.status = STATUS_WIN
        except ValueError:
            if self.remaining_guesses == 0:
                self.status = STATUS_LOSE
            else:
                self.remaining_guesses -= 1

    def get_masked_word(self):
        return self.masked_word

    def get_status(self):
        return self.status
