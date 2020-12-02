import re


class PhoneNumber:
    def __init__(self, number):
        self.validate_number(number)
        self.area_code, self.exchange_code, self.subscriber_number = re.match(
            r"\+?1?\D*?([2-9]\d{2})\D*?([2-9]\d{2})\D*?(\d{4})\D*$", number
        ).groups()
        self.number = self.area_code + self.exchange_code + self.subscriber_number

    def pretty(self):
        return f"({self.area_code}) {self.exchange_code}-{self.subscriber_number}"

    def validate_number(self, number):
        m = re.match(r"\+?1?\D*?([2-9]\d{2})\D*?([2-9]\d{2})\D*?(\d{4})\D*$", number)
        if not m:
            raise ValueError("not a valid number!")
