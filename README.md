# EGbot - README
EGbot (Eric Gao's bot or Email Greetings bot) is a Linux-based project that functions as follows:
1. Listens to a mailbox using IMAP protocal and get the email body as a string
2. Uses the ChatterBot AI to generate a response towards the mail body
3. Send the AI's response back to the user using SMTP protocal

Features:
1. It can listen to any incoming emails to your designated email account and reply to them like real humans (although you need Turing tests to determine that).
2. If you have sufficient storage space, train the bot with Ubuntu Corpus from ChatterBot API and generate more human-like conversations.
3. You can also train another bot to respond to the subject, instead of using the default one.
4. You can set default settings for the bot (such as its metacognition, response when feeling confused, etc.)
5. Customize where to find the mail body. This is different for different email servers, clients, etc.
6. You can pick any email service providers as long as they provide IMAP and SMTP services.

Dependencies are different depending on OS and python version. In most cases, ```chatterbot==1.1.0```, ```chatterbot_corpus```, and ```imapclient``` are needed.

The project was run on Ubuntu 18.0.4 LTS and python3.6.9. The default used server is 163.com. To run it, clone this repo and go to the root directory of the project and run ```./EGbot.sh``` in terminal.

Enjoy and feel free to send me qusetions and suggestions!

IMPORTANT: DO NOT USE IT FOR COMMERCIAL WITHOUT PERMISSION AND DO NOT USE IF FOR ILLEGAL PURPOSES IN ANY CASES!
