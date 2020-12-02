allergies_values = {
    "eggs": 1,
    "peanuts": 2,
    "shellfish": 4,
    "strawberries": 8,
    "tomatoes": 16,
    "chocolate": 32,
    "pollen": 64,
    "cats": 128,
}


class Allergies:
    def __init__(self, score):
        self.score = score

    def allergic_to(self, item):
        return bool(allergies_values[item] & self.score)

    @property
    def lst(self):
        return [k for k, v in allergies_values.items() if self.allergic_to(k)]
