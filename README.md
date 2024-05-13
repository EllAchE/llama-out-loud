# llama-out-loud

This is a POC built for the Meta LLama3 h4ckathon! You'll see some shortcuts made to get this working in 24 hours 😁

Because Meta Raybans don't expose an SDK, we got creative to pass the input into our system. If recreating on iOS:
- Start a live stream from your glasses to your phone
- Create a shortcut that takes screenshots on a 5s interval and hits a post endpoint (matching the IP & port of your flask server on the same network)
- Run the shortcut in the background

Image data will then be posted to an endpoint you can consume from! The image data will be stored and then applied when voice activation/gestures (gestures not supported in MVP) trigger actions.

Thanks to the organizers of the meta llama 3 h4ckathon!
