#!/usr/bin/env python3

from api.settings import Settings
from api.call import Call
from tools.status import Status
from tools.validate import Validate
from tools.parser import Parser

class Wapy:
    def __init__(self):
        self.settings = Settings()
        self.call = Call()
        self.status = Status()
        self.validate = Validate()
        self.parser = Parser()

        self.requests = [
            self.settings.url.full
        ]

        self.core()

    def core(self):
        for request in self.requests:
            print("[request] {}".format(request))
            result = self.call.get(request, None)
            self.status.check(result)
            self.parse(result.text)

    def parse(self, content):
        self.parser.feed(content)

if (__name__ == "__main__"):
    Wapy()
