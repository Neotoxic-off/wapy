from tools.validate import Validate

class Url:
    def __init__(self, protocol, domain):
        self.validate = Validate()

        self.protocol = protocol
        self.domain = domain
        self.full = None

        self.set_full()

    def set_protocol(self, value):
        if (self.validate.validate([value]) == True):
            if (type(value) is str):
                self.protocol = value

    def set_domain(self, value):
        if (self.validate.validate([value]) == True):
            if (type(value) is str):
                self.domain = value

    def set_full(self):
        if (self.validate.validate([self.protocol, self.domain]) == True):
            self.full = "{}://{}".format(
                self.protocol,
                self.domain
            )


