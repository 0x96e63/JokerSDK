from requests import get
from ..enums import *
from ..format import __dial_format__, __hangup_format__
from typing import Any
from ..exceptions import exceptions

class outbound_calls:
    def __init__(self, apiKey: str) -> None:
        self.apiKey = apiKey
    
    def create_call(self, to: str, from_: str, callbackUrl: str) -> list[bool, dict[Any]]:
        apiResponse = get(__dial_format__(self.apiKey, endpoint.Enums.DIAL, to, from_, callbackUrl)).json()
        if apiResponse['status'] == response.Enums.STATUS_FAILED and apiResponse['context'] == response.Enums.COUNTRY_NOT_WHITELISTED:
            raise exceptions.CountryNotWhitelistedException()
        else:
            return True, apiResponse


    def hangup_call(self) ->Any:
        if not self.sid[0]:
            raise exceptions.NonExistentCallException()
        return get(__hangup_format__(self.apiKey, endpoint.Enums.HANGUP, self.sid[1]))