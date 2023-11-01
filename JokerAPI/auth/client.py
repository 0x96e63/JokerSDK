from ..endpoints import outbound_calls

"""
# `create_outbound_call` class to initiate an outbound call.
------------------------------------------------------------
```
JokerObject = create_outbound_call(
    apiKey = "<APIKEY>": Default
    *arg, **kwargs: Required
    >   to: str ~ The phone number to dial.
        from_: str ~ The phone number to dial `to` from.
        callbackUrl: str ~ Any webserver to handle live callbacks to.
)
"""
class create_outbound_call(outbound_calls):
    """
    Main initiator for the `create_outbound_call` class.

    Parameters.
    ----------------------------------------------------
    `apiKey` > The API Key to use the SDK.

    *args > Required arguments to initiate a outbound call.

    **kwargs > Not required key word arguments which may be used in the future.


    `self.sid`: list[int] or list[int, str] 
        > Index 0 representing the status of the call (if it is live or not.): Static

        > Index 1 representing the SID of a channel if Index 0 is True (live).
    """
    def __init__(self, apiKey: str = "<API_KEY>", *args, **kwargs) -> None:
        self.sid: list[int] | list[int, str] = [False, None]
        super().__init__(apiKey)
        self.__dial__(*args, *kwargs)
    
    """
    'Private' `__dial__` function which is called whenever the class is initiated. 
    """
    def __dial__(self, to, from_, callbackUrl) -> str:
        self.sid[0], self.sid[1] = self.create_call(to, from_, callbackUrl)
    
    """
    The `hangup` function to hangup a live channel.
    """
    def hangup(self) -> None:
        return self.hangup_call