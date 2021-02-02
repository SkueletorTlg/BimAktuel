# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# (c) Muhammed Furkan http://t.me/B_Azade


import json
import logging
import os

import requests
import wget
from KekikSpatula import BimAktuel
from telethon import TelegramClient, events
from telethon.sync import TelegramClient
from telethon.tl.custom import Button

from config import Config

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


bot = TelegramClient('bimbot', Config.APP_ID, Config.APP_HASH).start(
    bot_token=Config.BOT_TOKEN)


def bim_parse(num):
    bim = BimAktuel()
    veri = bim.gorsel()
    resp = json.loads(veri)
    tarih = resp['tarih']
    urunler = resp['veri']
    if num == "1":
        return _extracted_from_bim_15(urunler, 0, tarih)
    elif num == "2":
        return _extracted_from_bim_15(urunler, 1, tarih)
    elif num == "3":
        return _extracted_from_bim_15(urunler, 2, tarih)
    elif num == "4":
        return _extracted_from_bim_15(urunler, 3, tarih)
    elif num == "5":
        return _extracted_from_bim_15(urunler, 4, tarih)
    elif num == "6":
        return _extracted_from_bim_15(urunler, 5, tarih)
    elif num == "7":
        return _extracted_from_bim_15(urunler, 6, tarih)
    elif num == "8":
        return _extracted_from_bim_15(urunler, 7, tarih)


def _extracted_from_bim_15(urunler, arg1, tarih):
    urun_1_baslik = urunler[arg1]['urun_baslik']
    urun_1_gorsel = urunler[arg1]['urun_gorsel']
    urun_1_fiyat = urunler[arg1]['urun_fiyat']
    resim_1 = wget.download(urun_1_gorsel)
    return urun_1_baslik, urun_1_fiyat, resim_1, tarih


markup = bot.build_reply_markup(
    [
        [
            Button.inline(text='1️⃣', data="1"),
            Button.inline(text='2️⃣', data="2"),
            Button.inline(text='3️⃣', data="3"),
            Button.inline(text='4️⃣', data="4")
        ],
        [
            Button.inline(text='5️⃣', data="5"),
            Button.inline(text='6️⃣', data="6"),
            Button.inline(text='7️⃣', data="7"),
            Button.inline(text='8️⃣', data="8")
        ],
        [
            Button.url(text='👤 Dueño', url="t.me/DKzippO"),
            Button.url(text='📍 Otros bots', url="t.me/Bot de ayuda")
        ]
    ]
)


@bot.on(events.NewMessage(pattern="/start ?(.*)", func=lambda e: e.is_private))
async def start(event):
    x = await bot.send_message(
        event.chat_id,
        "Hola, con este bot conocerás varios canales de Telegram ❤",
        buttons=markup,
        file="./img/bim.mp4"
    )


@bot.on(events.CallbackQuery())
async def callback(event):
    if event.data.decode("utf-8") == "1":
        await event.answer('Cargando, no tomará mucho tiempo :)', alert=True)
        sonuc = bim_parse(event.data.decode("utf-8"))
        sonuc_baslik = sonuc[0]
        sonuc_fiyat = sonuc[1]
        sonuc_img = sonuc[2]
        sonuc_tarih = sonuc[3]
        msg = f"**MonsterCine**\n\n**Temática:** Películas 🍿 \n**<a href="https://t.me/joinchat/WLIHhSTSuLH-37FC">Toca aquí para ingresar.</a>** "
        mssg = await bot.send_message(
            event.sender_id,
            msg,
            file="./img/Monstercine.jpg",
            buttons=markup
        )
        os.remove("./img/Monstercine.jpg")

    if event.data.decode("utf-8") == "2":
        await event.answer('Cargando, no tomará mucho tiempo :)', alert=True)
        sonuc = bim_parse(event.data.decode("utf-8"))
        sonuc_baslik = sonuc[0]
        sonuc_fiyat = sonuc[1]
        sonuc_img = sonuc[2]
        sonuc_tarih = sonuc[3]
        msg = f"**Perversión**\n\n**Temática:** Contenido Hot 😏 \n**<a href="https://t.me/joinchat/AAAAAEnE4Zk-whY6W9PRRw">Toca aquí para ingresar.</a>** "
        mssg = await bot.edit_message(
            event.sender_id,
            event.query.msg_id,
            msg,
            file="./img/Perversion.jpg",
            buttons=markup
        )
        os.remove("./img/Perversion.jpg")

    if event.data.decode("utf-8") == "3":
        await event.answer('Cargando, no tomará mucho tiempo :)', alert=True)
        sonuc = bim_parse(event.data.decode("utf-8"))
        sonuc_baslik = sonuc[0]
        sonuc_fiyat = sonuc[1]
        sonuc_img = sonuc[2]
        sonuc_tarih = sonuc[3]
        msg = f"**MonsterBinners**\n\n**Temática:** Cuentas premiums gratis 🎁 \n**<a href="https://t.me/joinchat/SDpWL08FxJsH_lbg">Toca aquí para ingresar.</a>** "
        mssg = await bot.edit_message(
            event.sender_id,
            event.query.msg_id,
            msg,
            file="./img/Monsterbinners.jpg",
            buttons=markup
        )
        os.remove("./img/Monsterbinners.jpg")

    if event.data.decode("utf-8") == "4":
        await event.answer('Cargando, no tomará mucho tiempo :)', alert=True)
        sonuc = bim_parse(event.data.decode("utf-8"))
        sonuc_baslik = sonuc[0]
        sonuc_fiyat = sonuc[1]
        sonuc_img = sonuc[2]
        sonuc_tarih = sonuc[3]
        msg = f"**MusicSpec8D**\n\n**Temática:** Música en 8D 🎧 \n**<a href="http://t.me/MusicSpec8D">Toca aquí para ingresar.</a>** "
        mssg = await bot.edit_message(
            event.sender_id,
            event.query.msg_id,
            msg,
            file="./img/Musicspec8d.jpg",
            buttons=markup
        )
        os.remove("./img/Musicspec8d.jpg")

    if event.data.decode("utf-8") == "5":
        await event.answer('Cargando, no tomará mucho tiempo :)', alert=True)
        sonuc = bim_parse(event.data.decode("utf-8"))
        sonuc_baslik = sonuc[0]
        sonuc_fiyat = sonuc[1]
        sonuc_img = sonuc[2]
        sonuc_tarih = sonuc[3]
        msg = f"**{sonuc_tarih} f"**GatitosDepresión**\n\n**Temática:** Gatitos que curan tu depresión 😹 \n**<a href="http://t.me/GatitosDepresion">Toca aquí para ingresar.</a>** "
        mssg = await bot.edit_message(
            event.sender_id,
            event.query.msg_id,
            msg,
            file="./img/Gatitosdepresion.jpg",
            buttons=markup
        )
        os.remove("./img/Gatitosdepresion.jpg")

    if event.data.decode("utf-8") == "6":
        await event.answer('Cargando, no tomará mucho tiempo :)', alert=True)
        sonuc = bim_parse(event.data.decode("utf-8"))
        sonuc_baslik = sonuc[0]
        sonuc_fiyat = sonuc[1]
        sonuc_img = sonuc[2]
        sonuc_tarih = sonuc[3]
        msg = f"**Bots de Ayuda**\n\n**Temática:** Bots creados por <a href="http://t.me/DKzippO">Skueletor</a> 🤖 \n**<a href="http://t.me/MusicSpec8D">Toca aquí para ingresar.</a>** "
        mssg = await bot.edit_message(
            event.sender_id,
            event.query.msg_id,
            msg,
            file="./img/Botsdeayuda.jpg",
            buttons=markup
        )
        os.remove("./img/Botsdeayuda.jpg")

    if event.data.decode("utf-8") == "7":
        await event.answer('Cargando, no tomará mucho tiempo :)', alert=True)
        sonuc = bim_parse(event.data.decode("utf-8"))
        sonuc_baslik = sonuc[0]
        sonuc_fiyat = sonuc[1]
        sonuc_img = sonuc[2]
        sonuc_tarih = sonuc[3]
        msg = f"**Planeta Curioso**\n\n**Temática:** Curiosidades 🔎 \n**<a href="http://t.me/PlanetaaCurioso">Toca aquí para ingresar.</a>** "
        mssg = await bot.edit_message(
            event.sender_id,
            event.query.msg_id,
            msg,
            file="./img/Planetacurioso.jpg",
            buttons=markup
        )
        os.remove("./img/Planetacurioso.jpg")

    if event.data.decode("utf-8") == "8":
        await event.answer('Cargando, no tomará mucho tiempo :)', alert=True)
        sonuc = bim_parse(event.data.decode("utf-8"))
        sonuc_baslik = sonuc[0]
        sonuc_fiyat = sonuc[1]
        sonuc_img = sonuc[2]
        sonuc_tarih = sonuc[3]
        msg = f"**Instagramer**\n\n**Temática:** Memes 🤣 \n**<a href="http://t.me/Instagramer_la">Toca aquí para ingresar.</a>** "
        mssg = await bot.edit_message(
            event.sender_id,
            event.query.msg_id,
            msg,
            file="./img/Instagramer.jpg",
            buttons=markup
        )
        os.remove("./img/Instagramer.jpg")


bot.start()
bot.run_until_disconnected()
