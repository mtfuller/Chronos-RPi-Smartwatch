class Listener:
    def __init__(self):
        self.s = ""

    def foo(self, data):
        print("hello")

    def foo2(self, data):
        print("hello2")

    def set_message(self, **kwargs):
        self.s = kwargs["msg"]

    def equals(self, msg):
        return msg == self.s