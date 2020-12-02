class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds

    def on_earth(self):
        period_days = 365.25
        return self.calculate_years(period_days)

    def on_mercury(self):
        period_days = 0.2408467 * 365.25
        return self.calculate_years(period_days)

    def on_venus(self):
        period_days = 0.61519726 * 365.25
        return self.calculate_years(period_days)

    def on_mars(self):
        period_days = 1.8808158 * 365.25
        return self.calculate_years(period_days)

    def on_jupiter(self):
        period_days = 11.862615 * 365.25
        return self.calculate_years(period_days)

    def on_saturn(self):
        period_days = 29.447498 * 365.25
        return self.calculate_years(period_days)

    def on_uranus(self):
        period_days = 84.016846 * 365.25
        return self.calculate_years(period_days)

    def on_neptune(self):
        period_days = 164.79132 * 365.25
        return self.calculate_years(period_days)

    def calculate_years(self, period):
        return round(self.seconds / (period*24*60*60), 2)
