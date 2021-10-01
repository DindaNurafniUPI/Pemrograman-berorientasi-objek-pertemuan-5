
class bahasa:

    def say_hello(self):
        print('halo')

class French:
    def say_hello(self):
        print('salut')
class english:
    def say_hello(self):
        print('Hello')

def intro(lang):
    lang.say_hello()

pers1 = bahasa()
pers2 = French()
pers3 = english()

intro(pers1)
intro(pers2)
intro(pers3)