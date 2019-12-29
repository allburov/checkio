#!/usr/bin/env checkio --domain=py run microwave-ovens
from datetime import timedelta


class Timer(timedelta):
    def __new__(cls, minutes=0, seconds=0):
        seconds = minutes * 60 + seconds
        seconds = min(90 * 60, seconds)
        seconds = max(0, seconds)
        self = timedelta.__new__(cls, seconds=seconds)
        return self

    @property
    def minutes(self):
        return self.seconds // 60

    def __str__(self):
        res = '{:02d}:{:02d}'.format(self.minutes, self.seconds % 60)
        return res

    def add_(self, period: str):
        t = int(period[:-1])
        if period.endswith('s'):
            return Timer(seconds=self.seconds + t)
        elif period.endswith('m'):
            return Timer(minutes=t, seconds=self.seconds)

    def del_(self, period: str):
        return self.add_(f'-{period}')

    @classmethod
    def get(cls, repr: str):
        minutes, seconds = map(int, repr.split(':'))
        return Timer(minutes=minutes, seconds=seconds)


assert str(Timer()) == "00:00"
assert str(Timer(minutes=90, seconds=00)) == "90:00"
assert str(Timer(minutes=100, seconds=00)) == "90:00"
assert str(Timer(minutes=-1, seconds=00)) == "00:00"

assert str(Timer(seconds=10).add_('10s')) == "00:20"
assert str(Timer(seconds=10).add_('10m')) == "10:10"

assert str(Timer(seconds=20).del_('10s')) == "00:10"
assert str(Timer.get("12:34")) == "12:34"


class MicrowaveBase:
    def __init__(self):
        self.time: Timer = Timer()

    def show_time(self):
        return str(self.time)


class Microwave1(MicrowaveBase):
    def show_time(self):
        repr = list(super().show_time())
        repr[0] = "_"
        return "".join(repr)


class Microwave2(MicrowaveBase):
    def show_time(self):
        repr = list(super().show_time())
        repr[-1] = "_"
        return "".join(repr)


class Microwave3(MicrowaveBase):
    pass


class RemoteControl:
    def __init__(self, inst: MicrowaveBase):
        self._inst = inst

    def set_time(self, repr):
        self._inst.time = Timer.get(repr)

    def add_time(self, time):
        self._inst.time = self._inst.time.add_(time)

    def del_time(self, time):
        self._inst.time = self._inst.time.del_(time)

    def show_time(self):
        return self._inst.show_time()


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    microwave_1 = Microwave1()
    microwave_2 = Microwave2()
    microwave_3 = Microwave3()

    remote_control_1 = RemoteControl(microwave_1)
    remote_control_1.set_time("01:00")

    remote_control_2 = RemoteControl(microwave_2)
    remote_control_2.add_time("90s")

    remote_control_3 = RemoteControl(microwave_3)
    remote_control_3.del_time("300s")
    remote_control_3.add_time("100s")

    assert remote_control_1.show_time() == "_1:00"
    assert remote_control_2.show_time() == "01:3_"
    assert remote_control_3.show_time() == "01:40"
    print("Coding complete? Let's try tests!")
