import requests

class Call:
    def __init__(self):
        pass

    def get(self, url, headers):
        result = None

        try:
            result = requests.get(url, {headers: headers})
        except Exception as ex:
            print(ex)

        return (result)
