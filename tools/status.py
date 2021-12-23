class Status:
    def __init__(self):
        self.log = "[status]"

    def check(self, result):
        status = {
            "200" : "found",
            "404" : "not found"
        }
    
        if (result != None):
            print("{}  {}".format(self.log, status["{}".format(result.status_code)]))
        else:
            print("{}  {}".format(self.log, "dead"))