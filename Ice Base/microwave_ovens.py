#!/usr/bin/env checkio --domain=py run microwave-ovens

# https://py.checkio.org/mission/microwave-ovens/

# There is a lunch place at your work with the 3 microwave ovens (Мicrowave1, Мicrowave2, Мicrowave3), which are the subclasses of the MicrowaveBase class. Every microwave can be controlled by a RemoteControl. The RemoteControl uses the next commands:
# 
# set_time("xx:xx"), where "xx:xx" - time in minutes and seconds, which shows how long the food will be warming up. For example: set_time("05:30");
# add_time("Ns"),add_time("Nm"), where N - the number of seconds("s") or minutes("m"), which should be added to the current time;
# del_time("Ns"),del_time("Nm"), where N - the amount of the seconds("s") or minutes("m"), which should be subtracted from the current time;
# show_time()- shows the current time for the microwave.
# 
# The default time is 00:00. The time can't be less than 00:00 or greater than 90:00, even if add_time or del_time causes it.
# 
# Your task is to create a few classes - one for the MicrowaveBase, three for the three different microwaves, and one for the RemoteControl - just as described above. The RemoteControl will have 1 parameter - an instance of the Microwave (for example, RemoteControl(microwave_1), where microwave_1 = Microwave1()) that shows which Microwave should be controlled by the current RemoteControle.Only the third oven works properly and shows the full time. The other two have some flaws with their displays - the first shows '_' instead of the first digit and the second does the same with the last digit. They show time like this:
# microwave_1 = Microwave1()
# microwave_2 = Microwave2()
# microwave_3 = Microwave3()
# 
# RemoteControl(microwave_1).show_time() == "_0:00"
# RemoteControl(microwave_2).show_time() == "00:0_"
# RemoteControl(microwave_3).show_time() == "00:00"
# 
# In this mission you could use theBridgedesign pattern. Its main task is -  to decouple an abstraction from its implementation so that the two can vary independently.
# 
# Example:
# microwave_1 = Microwave1()
# microwave_2 = Microwave2()
# microwave_3 = Microwave3()
# 
# remote_control_1 = RemoteControl(microwave_1)
# remote_control_1.set_time("01:00")
# 
# remote_control_2 = RemoteControl(microwave_2)
# remote_control_2.add_time("90s")
#     
# remote_control_3 = RemoteControl(microwave_3)
# remote_control_3.del_time("300s")
# remote_control_3.add_time("100s")
#     
# remote_control_1.show_time() == "_1:00"
# remote_control_2.show_time() == "01:3_"
# remote_control_3.show_time() == "01:40"
# 
# 
# 
# Input:methods of the RemoteControl class and time.
# 
# Output:time on the display of the microwave.
# 
# Precondition:00:00<= time<= 90:00
# 
# 
# END_DESC

class MicrowaveBase:
    pass

class Microwave1(MicrowaveBase):
    pass

class Microwave2(MicrowaveBase):
    pass

class Microwave3(MicrowaveBase):
    pass

class RemoteControl:
    pass


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

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