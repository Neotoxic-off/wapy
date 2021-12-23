class Validate:
    def __init__(self):
        pass

    def validate(self, required):
        for value in required:
            if (required == None):
                return (False)
        return (True)
