class CountryNotWhitelistedException(Exception):
    def __init__(self):
        super().__init__(f"The country you are trying to dial `from` or `to` is not whitelisted.")

class NonExistentCallException(Exception):
    def __init__(self, debug = False, callSid = ""):
        super().__init__(f"You cannot hang up a non-existent call or channel.{callSid if debug else ''}")
