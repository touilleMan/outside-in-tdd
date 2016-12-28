import datetime

from app.clock import Clock


class TestClockShould:
    def test_return_todays_date_in_dd_mm_yyyy_format(self):
        clock = TestableClock()
        date = clock.today_as_string()
        assert date == "24/04/2015"


class TestableClock(Clock):
    def today(self):
        return datetime.date(2015, 4, 24)
