import JokerAPI


call = JokerAPI.client.create_outbound_call(
    apiKey = "<API_KEY>",
    to = "1111111",
    from_ = "22222",
    callbackUrl = "https://google.com"
)


call.hangup()