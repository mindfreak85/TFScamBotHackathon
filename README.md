# TFScamBotHackathon

## About
  This is a Hack for Deep Learning week 2022
  
  This telegram bot utilizes an AI model to try and detect scam messages to prevent users from falling victim to scams.
  The telegram bot as for now only accepts 1 message input from the user and it will return either a "Yes it is a scam" or "No it is not a scam".
  We used a telegram bot as telegram is growing among users and it is easy to use and implement in group chats etc. 
  For future development, we hope to be able to utilize this telegram bot to always be on 24/7 in a groupchat to determine if a particular user is sending scam    messages.

## Contributers
- Yong Chang Xin 
- Tan Wei Shan
- Howard Jek 
- Mohamed Umar
- Eiffel Yuen

## Models Used

1. 
2. 


## How to Use?

1. Create a virtual environment and install the dependecies in the requirements.txt file. 
2. Run app.py file in command prompt to run app
3. Expose local port 5000 to the internet by running ngrok http 5000 in another command prompt window.
4. Once flask app is alive, copy the url link into DialogFlow webhook to connect bot to the backend. In the webhook url, input "URL/webhook" with a webhook at the back
5. The telegram bot is ready to go

## References

- <https://chatbotslife.com/deploying-a-machine-learning-model-as-a-chatbot-part-1-d5dc9e8fa4ba>
- <https://chatbotslife.com/deploying-a-machine-learning-model-as-a-chatbot-part-2-20038a9b39ef>
- <>
