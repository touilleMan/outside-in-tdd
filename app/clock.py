import datetime


class Clock:

    def today_as_string(self):
        return self.today().strftime("%d/%m/%Y")

    def today(self):
        return datetime.date.today()
