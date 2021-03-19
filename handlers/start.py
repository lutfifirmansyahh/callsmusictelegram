from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from helpers.filters import command, other_filters, other_filters2


@Client.on_message(command("start") & other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 Haii Bagong! {message.from_user.first_name}!</b>

Gw Robot Pemutar Musik!,Di-Telegram Lu Bisa Dengerin Lagu!.

Silahkan Klik Kotak Dibawah Ini, Apabila Kurang Paham Bisa Dibantu Nanti!.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚒ Owner!", url="https://t.me/yangtagtolol"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/gcsampah"
                    ),
                    InlineKeyboardButton(
                        "Channel 🔈", url="https://t.me/channeldregs"
                ],
                [
                    InlineKeyboardButton(
                        "PANDUAN CARA MENGGUNAKAN BOT MUSIK", url="https://telegra.ph/ᴜᴘɪ-03-19"
                    )
                ]
            ]
        )
    )


@Client.on_message(command("start") & other_filters)
async def start2(_, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
