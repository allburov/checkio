#!/home/aburov/venvs/checkio-venv/bin/checkio --domain=py run dialogues

# The modern world is filled with means of communication - the social networks, messengers, phone calls, SMS etc.But sometimes in every communication channel a flaw can be detected and in the moments like that you think to yourself: "I should create my own messenger which won’t have problems like this one".
# In this mission you’ll get your chance.
# Your task is to create a Chat class which could help a Human(name) and Robot(serial_number) to make a conversation. This class should have a few methods:
# connect_human()- connects human to the chat.
# connect_robot()- connects robot to the chat.
# show_human_dialogue()- shows the dialog as the human sees it - as simple text.
# show_robot_dialogue()- shows the dialog as the robot perceives it - as the set of ones and zeroes. To simplify the task, just replace every vowel ('aeiouAEIOU') with "0", and the rest symbols (consonants, white spaces and special signs like ",", "!", etc.) with "1".
# Dialog for the human should be displayed like this:
# (human name) said: message text
# (robot serial number): message text
# For the robot:
# (human name) said: 11100100011
# (robot serial number) said: 100011100101
# Interlocutors should have asend()method for sending messages to the dialog.
# In this mission you could use theMediatordesign pattern.
# 
# Example:
# chat = Chat()
# karl = Human("Karl")
# bot = Robot("R2D2")
# chat.connect_human(karl)
# chat.connect_robot(bot)
# karl.send("Hi! What's new?")
# bot.send("Hello, human. Could we speak later about it?")
# chat.show_human_dialogue() == """Karl said: Hi! What's new?
# R2D2 said: Hello, human. Could we speak later about it?"""
# chat.show_robot_dialogue() == """Karl said: 101111011111011
# R2D2 said: 10110111010111100111101110011101011010011011"""
# 
# 
# 
# Input:Interlocutors and the text of messages.
# 
# Output:A dialog (the multiline string).
# 
# Precondition:2 interlocutors.
# 
# 
# END_DESC

import re
from typing import Optional

VOWELS = "aeiou"


class Chater(object):
    def __init__(self, name):
        self.name = name
        self.chat: Optional[Chat] = None

    def send(self, message):
        self.chat.add_message(self, message)

    @staticmethod
    def translate(message):
        return message


class Human(Chater):
    pass


class Robot(Chater):
    @staticmethod
    def translate(message):
        one = 'aeiouAEIOU'
        message = re.sub(rf'[^{one}]', '1', message)
        message = re.sub(rf'[{one}]', '0', message)
        return message


class Chat:
    def __init__(self):
        self.chaters = []
        self.messages = []

    def connect(self, chater: Chater):
        self.chaters.append(chater)
        chater.chat = self

    def add_message(self, chater, message):
        self.messages.append((chater, message))

    def connect_human(self, human: Human):
        self.connect(human)

    def connect_robot(self, bot: Robot):
        self.connect(bot)

    def show(self, chatercls):
        translate = chatercls.translate
        str_ = "\n".join([f"{chater.name} said: {translate(message)}" for chater, message in self.messages])
        return str_

    def show_human_dialogue(self):
        return self.show(Human)

    def show_robot_dialogue(self):
        return self.show(Robot)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert Robot.translate("Hi! What's new?") == "101111011111011"
    assert Robot.translate("0") == "1"
    assert Robot.translate("1") == "1"

    chat = Chat()
    karl = Human("Karl")
    bot = Robot("R2D2")
    chat.connect_human(karl)
    chat.connect_robot(bot)
    karl.send("Hi! What's new?")
    bot.send("Hello, human. Could we speak later about it?")
    assert chat.show_human_dialogue() == """Karl said: Hi! What's new?
R2D2 said: Hello, human. Could we speak later about it?"""
    assert chat.show_robot_dialogue() == """Karl said: 101111011111011
R2D2 said: 10110111010111100111101110011101011010011011"""

    print("Coding complete? Let's try tests!")