
def __dial_format__(apiKey, baseUrl: str, to: str, from_: str, callbackUrl: str) -> str:
    return f"{baseUrl}?apikey={apiKey}&to={to}&from={from_}&webhookurl={callbackUrl}"

def __hangup_format__(apiKey, baseUrl: str, sid: str) -> str:
    return f"{baseUrl}?apikey={apiKey}&callsid={sid}"