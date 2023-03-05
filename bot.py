TOKEN="5890177800:AAH6oZBKl5Bae84lUcTx1axaysKkOwPkVGA",


import telebot


import openai

# Define OpenAI API key 
openai.api_key = "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"

# Set up the model and prompt



bot = telebot.TeleBot("5890177800:AAH6oZBKl5Bae84lUcTx1axaysKkOwPkVGA", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Welcome to KIIT-CONNECT!!!")
 

@bot.message_handler(commands=['ai'])
def ChatGpt(message):
    print(message.text)
    text = message.text[4:]
    print(text)
    bot.reply_to(message,"Please Wait while Your response is being generated!!!")
    model_engine = "text-davinci-003"
    prompt = "Wap to add two numbers using python."
    completion = openai.Completion.create(
    engine=model_engine,
    prompt=text,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,)

    response = completion.choices[0].text
    bot.reply_to(message,response)
 
bot.infinity_polling()