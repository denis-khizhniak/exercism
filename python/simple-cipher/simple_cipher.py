import random
from string import ascii_lowercase
from itertools import cycle, starmap


class Cipher:
    def __init__(self, key=None):
        self.key = self.generate_key(100) if not key else key

    def encode(self, text):
        return "".join(starmap(self.shift_letter, zip(text, self.shifts_cycle)))

    def decode(self, text):
        return "".join(
            starmap(
                self.shift_letter, zip(text, map(lambda x: -1 * x, self.shifts_cycle))
            )
        )

    @staticmethod
    def generate_key(length):
        return "".join(random.choice(ascii_lowercase) for _ in range(length))

    @staticmethod
    def shift_letter(alpha, shift):
        return ascii_lowercase[(ascii_lowercase.index(alpha) + shift) % 26]

    @property
    def shifts_cycle(self):
        return cycle(map(ascii_lowercase.index, self.key))
