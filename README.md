# EGbot - README
EGbot (Eric Gao's bot or Email Greetings bot) is a Linux-based project that functions as follows:
1. Listens to a mailbox using IMAP protocal and get the email body as a string
2. Uses the ChatterBot AI to generate a response towards the mail body
3. Send the AI's response back to the user using SMTP protocal

Dependencies are different depending on OS and python version. In most cases, ```chatterbot```, ```chatterbot_corpus```, and ```imapclient``` are needed.

The project was run on Ubuntu 18.0.4 LTS and python3.6.9. The default used server is 163.com (because the encryption isn't overly complicated). To run it, clone this repo and go to the root directory of the project and run ```./EGbot.sh``` in terminal.

Enjoy and feel free to send me qusetions and suggestions!
