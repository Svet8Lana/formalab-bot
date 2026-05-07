#!/usr/bin/env python3
"""
FormaLab Telegram Bot
Бот для игры "Лепи и Оживляй!" от FormaLab
"""

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# ── ТОКЕН ──────────────────────────────────────────
TOKEN = "8663260845:AAGO9maKW1jMuWhCMzbow1a1EK-gnn8qOFU"

# ── URL игры (после публикации на Netlify) ──────────
GAME_URL = "https://formalab-game.netlify.app"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# ── /start ─────────────────────────────────────────
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    name = user.first_name or "Творец"

    text = (
        f"👋 Привет, {name}!\n\n"
        f"Добро пожаловать в *FormaLab* 🎨\n\n"
        f"_Руками — человек впервые говорит миру о себе._\n"
        f"_Это только начало. Куда придёшь — решаешь ты. 🌍_\n\n"
        f"Здесь ты научишься лепить персонажей из воздушного пластилина FormaLab "
        f"по пошаговым иллюстрациям — и соберёшь свою коллекцию!\n\n"
        f"Выбери что хочешь сделать 👇"
    )

    keyboard = [
        [InlineKeyboardButton("🎮 Играть — Лепи и Оживляй!", web_app=WebAppInfo(url=GAME_URL))],
        [InlineKeyboardButton("📦 Моя коллекция", callback_data="collection")],
        [InlineKeyboardButton("🛒 Купить пластилин на Ozon", url="https://ozon.ru")],
        [InlineKeyboardButton("📱 Канал FormaLab", url="https://t.me/formalab_clay")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(text, parse_mode='Markdown', reply_markup=reply_markup)


# ── /play ──────────────────────────────────────────
async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🎮 *Лепи и Оживляй!*\n\n"
        "Выбери персонажа и следуй пошаговым иллюстрациям.\n"
        "Слепи — и он войдёт в твою коллекцию! ✨\n\n"
        "🐱 Котёнок Мяу — Легко\n"
        "🐸 Лягушка Ква — Легко\n"
        "🦊 Лисичка Рыжик — Средне\n"
        "🐼 Панда Бао — Средне\n"
        "🦄 Единорог Луна — 🔒 Купи набор\n"
        "🐉 Дракон Огник — 🔒 Купи набор\n"
    )
    keyboard = [
        [InlineKeyboardButton("🚀 Запустить игру!", web_app=WebAppInfo(url=GAME_URL))],
        [InlineKeyboardButton("🛒 Разблокировать всех — купить на Ozon", url="https://ozon.ru")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(text, parse_mode='Markdown', reply_markup=reply_markup)


# ── /collection ────────────────────────────────────
async def collection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "📦 *Твоя коллекция*\n\n"
        "🐱 Котёнок Мяу — ✅ Собран\n"
        "🐸 Лягушка Ква — 🔒 Не слеплена\n"
        "🦊 Лисичка Рыжик — 🔒 Не слеплена\n"
        "🐼 Панда Бао — 🔒 Не слеплена\n"
        "🦄 Единорог Луна — 🔒 Купи набор\n"
        "🐉 Дракон Огник — 🔒 Купи набор\n"
        "🦋 Бабочка — 🔒 Купи набор\n"
        "🐢 Черепаха — 🔒 Купи набор\n"
        "🦁 Лев — 🔒 Купи набор\n"
        "🐙 Осьминог — 🔒 Купи набор\n"
        "🦖 Динозавр — 🔒 Купи набор\n"
        "🌈 Радуга — 🔒 Купи набор\n\n"
        "_Собери всех 12 персонажей! Каждый набор FormaLab открывает новых._"
    )
    keyboard = [
        [InlineKeyboardButton("🎮 Слепить ещё!", web_app=WebAppInfo(url=GAME_URL))],
        [InlineKeyboardButton("🛒 Купить набор на Ozon", url="https://ozon.ru")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(text, parse_mode='Markdown', reply_markup=reply_markup)


# ── /promo ─────────────────────────────────────────
async def promo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🎁 *Твой промокод*\n\n"
        "Используй при заказе на Ozon:\n\n"
        "```LEPIM10```\n\n"
        "✅ Скидка *10%* на любой набор FormaLab\n"
        "⏰ Действует до конца месяца\n\n"
        "_Слепи персонажа — получи новый промокод!_"
    )
    keyboard = [
        [InlineKeyboardButton("🛒 Применить на Ozon", url="https://ozon.ru")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(text, parse_mode='Markdown', reply_markup=reply_markup)


# ── /about ─────────────────────────────────────────
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🎨 *О FormaLab*\n\n"
        "_Руками — человек впервые говорит миру о себе._\n"
        "_Это только начало. Куда придёшь — решаешь ты. 🌍_\n\n"
        "FormaLab — воздушный пластилин нового поколения:\n\n"
        "✅ 36 ярких цветов\n"
        "✅ Не липнет к рукам\n"
        "✅ Высыхает за 24 часа\n"
        "✅ Нетоксичный, без глютена\n"
        "✅ Бесплатное приложение навсегда\n"
        "✅ 100+ персонажей в коллекции\n\n"
        "🌐 formalab.art"
    )
    keyboard = [
        [InlineKeyboardButton("🛒 Купить на Ozon", url="https://ozon.ru")],
        [InlineKeyboardButton("🌐 Наш сайт", url="https://formalab.art")],
        [InlineKeyboardButton("📱 Канал FormaLab", url="https://t.me/formalab_clay")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(text, parse_mode='Markdown', reply_markup=reply_markup)


# ── CALLBACK ───────────────────────────────────────
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "collection":
        await collection(update, context)


# ── MAIN ───────────────────────────────────────────
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("play", play))
    app.add_handler(CommandHandler("collection", collection))
    app.add_handler(CommandHandler("promo", promo))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("🚀 FormaLab бот запущен!")
    print("Команды: /start /play /collection /promo /about")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()
