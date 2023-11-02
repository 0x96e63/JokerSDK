JokerSDK
========
JokerSDK is a flexible and user-friendly Python library wrapping around [Joker](https://jokerapi.co/)'s Voice API.

## Key Features
 - Creating outbound voice calls.
 - Playing audio/text into live calls.
 - Gathering DTMF with audio/text from live calls.
 - Transferring recipients from Leg A to Leg B.
 - Sending DTMF into a live call.

## Requirements
 - Python >= 3.10

## To do
 - Fix type hints.
 - Redo docs, add docs.
 - Integrate callback class.

Guide - How to install JokerSDK
-------------------------------
JokerSDK via PyPi:
``` console
$ pip install JokerSDK
```
Or, if you wish to download it directly from this repository:
``` console
$ python setup.py install
```

JokerSDK - Usage
----------------

Create an outbound call
-----------------------
``` python
import JokerAPI

call = JokerAPI.client.create_outbound_call(
    apiKey = "API_KEY", # Your API Key, this can be found on site.
    to = "1234567890", # The number to call.
    from_ = "1987654321", # The number to call `to` from.
    callbackUrl = "https://my.callbackserver.xyz/JokerSDK/callbacks" # A web server to send all callbacks to.
)
```

Object attributes
-----------------
```python
import JokerAPI

call = JokerAPI.client.create_outbound_call(
    apiKey = "API_KEY", # Your API Key, this can be found on site.
    to = "1234567890", # The number to call.
    from_ = "1987654321", # The number to call `to` from.
    callbackUrl = "https://my.callbackserver.xyz/JokerSDK/callbacks" # A web server to send all callbacks to.
)

callSid = call.sid # Access the SID of the call.
retrieved = call.__retrieve__ # Boolean to check if the call has been retrieved or not.
staticStatus = call._sid # A static status indicating if the call has been terminated. This is inferred and does not reflect the actual state of the call.
```

Play audio into a call.
-----------------------
``` python
import JokerAPI

call = JokerAPI.client.create_outbound_call(
    apiKey = "API_KEY", # Your API Key, this can be found on site.
    to = "1234567890", # The number to call.
    from_ = "1987654321", # The number to call `to` from.
    callbackUrl = "https://my.callbackserver.xyz/JokerSDK/callbacks" # A web server to send all callbacks to.
)

call.play_audio(
    audioUrl = "https://my.cdnserver.xyz/JokerSDK/audio.wav" # A web server which holds the audio file to play.
)
```

Play text into a call.
----------------------
``` python
import JokerAPI

call = JokerAPI.client.create_outbound_call(
    apiKey = "API_KEY", # Your API Key, this can be found on site.
    to = "1234567890", # The number to call.
    from_ = "1987654321", # The number to call `to` from.
    callbackUrl = "https://my.callbackserver.xyz/JokerSDK/callbacks" # A web server to send all callbacks to.
)

call.play_text(
    text = "This is an example phrase of in what will be presented into a live call/channel", # A phrase which JokerAPI will synthesise.
    voice = "ai3-en-US-Madison" # The voice name of in which JokerAPI will synthesise with.
)
```

Gathering DTMF whilst playing Audio
-----------------------------------
``` python
import JokerAPI

call = JokerAPI.client.create_outbound_call(
    apiKey = "<API_KEY>", # Your API Key, this can be found on site.
    to = "1234567890", # The number to call.
    from_ = "1987654321", # The number to call `to` from.
    callbackUrl = "https://my.callbackserver.xyz/JokerSDK/callbacks" # A web server to send all callbacks to.
)

call.gather_dtmf_with_audio(
    audioUrl = "https://my.cdnserver.xyz/JokerSDK/audio.wav", # A web server which holds the audio file to play.
    maxDigits = 5 # The amount of digits which will be captured before calling back.
)
```

Gathering DTMF whilst playing Text
----------------------------------
``` python
import JokerAPI

call = JokerAPI.client.create_outbound_call(
    apiKey = "<API_KEY>", # Your API Key, this can be found on site.
    to = "1234567890", # The number to call.
    from_ = "1987654321", # The number to call `to` from.
    callbackUrl = "https://my.callbackserver.xyz/JokerSDK/callbacks" # A web server to send all callbacks to.
)

call.gather_dtmf_with_text(
    text = "This is an example phrase of in what will be presented into a live call/channel", # A phrase which JokerAPI will synthesise.
    voice = "ai3-en-US-Madison", # The voice name of in which JokerAPI will synthesise with.
    maxDigits = 5 # The amount of digits which will be captured before calling back.
)
```

Send DTMF tones
---------------
``` python
import JokerAPI

call = JokerAPI.client.create_outbound_call(
    apiKey = "<API_KEY>", # Your API Key, this can be found on site.
    to = "1234567890", # The number to call.
    from_ = "1987654321", # The number to call `to` from.
    callbackUrl = "https://my.callbackserver.xyz/JokerSDK/callbacks" # A web server to send all callbacks to.
)

call.send_dtmf(
    input_ = "1234" # Digits to Send DTMF tones to Leg B(to) from.
)
```

Finally, hang up the call.
--------------------------
``` python
import JokerAPI

call = JokerAPI.client.create_outbound_call(
    apiKey = "<API_KEY>", # Your API Key, this can be found on site.
    to = "1234567890", # The number to call.
    from_ = "1987654321", # The number to call `to` from.
    callbackUrl = "https://my.callbackserver.xyz/JokerSDK/callbacks" # A web server to send all callbacks to.
)
```

## Contributing
 - Feel free to contribute by opening issues or sending pull requests.

## License
This project is licensed under the GPL-3.0 license - see the LICENSE file for details.
