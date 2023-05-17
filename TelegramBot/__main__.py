from TelegramBot import bot
from TelegramBot.logging import LOGGER
from pyrogram import Client,filters,CallbackQueryHandler
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
group = -1001728546352
channel = -1001962326301

@bot.on_message(filters.command("test"))
def test(Client, message):
    # Create the callback game button
    callback_game_button = InlineKeyboardButton(
        "Play Game",
        callback_game="your_game_callback_data"
    )

    # Create an inline keyboard markup with the callback game button
    keyboard = InlineKeyboardMarkup([[callback_game_button]])
    post = bot.send_message(
            chat_id=channel,
            text="Hello! Please click the button below:",
            reply_markup=keyboard
        )
@bot.on_callback_query()
def handle_callback_game(client, callback_query):
    # Get the callback game data
    callback_game_data = callback_query.game_short_name
    post = bot.send_message(
        chat_id=channel,
        text=callback_game_data,
        reply_markup=keyboard
    )
    # Handle the game logic based on the callback data
    # ...

    # Answer the callback query to close the game
    callback_query.answer()

LOGGER(__name__).info("client successfully initiated....")
if __name__ == "__main__":
    bot.run()
