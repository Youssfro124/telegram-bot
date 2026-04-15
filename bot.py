# -*- coding: utf-8 -*-
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

ADMIN_USERNAME = "m16zinkou"
TOKEN = os.getenv("TELEGRAM_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prenom = update.effective_user.first_name or "toi"

    keyboard = [
        [
            InlineKeyboardButton("💎 Acheter un VIP", callback_data="buy_vip"),
            InlineKeyboardButton(
                "🛡️ Contacter un admin",
                url=f"https://t.me/{ADMIN_USERNAME}",
            ),
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    message = (
        f"🙋 Salut {prenom} , Pour quelle raison tu nous contactes ?\n\n"
        "Choisis une option ci-dessous :"
    )

    await update.message.reply_text(message, reply_markup=reply_markup)


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "buy_vip":
        keyboard = [
            [
                InlineKeyboardButton(
                    "🛡️ Contacter un admin",
                    url=f"https://t.me/{ADMIN_USERNAME}",
                )
            ]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.message.reply_text(
            "Très bon choix, tu seras pas déçu ! 🔥\n\n"
            "💳 Voici nos différents moyens de paiements :\n\n"
            "1️⃣ RIB : IT84 C036 6901 6002 0403 3742 101\n"
            "(Mettez n'importe quel destinataire)\n\n"
            "2️⃣ Paypal : Sarah.lb9999@gmail.com\n\n"
            "💬 Une fois fait, contacter un admin pour lui envoyer la preuve du virement",
            reply_markup=reply_markup
        )


def main():
    if not TOKEN:
        print("❌ Erreur : TELEGRAM_TOKEN introuvable.")
        return

    print("🤖 Bot en cours d'exécution...")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    app.run_polling()


if __name__ == "__main__":
    main()
