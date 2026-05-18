import os
import logging
from flask import Flask
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# =========================
# CONFIG
# =========================
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_LINK = "https://t.me/niftypulse2411"
ADMIN_1 = "https://t.me/Nifty_Pulse_01"
ADMIN_2 = "https://t.me/Finz8435"

TREND_LINK = "https://www.investing.com/technical/technical-summary"
DERIVATIVES_LINK = "https://www.nseindia.com/option-chain"
VOLATILITY_LINK = "https://www.nseindia.com/products-services/indices-india-vix"
INSTITUTION_LINK = "https://www.moneycontrol.com/stocks/marketstats/fii-dii-activity"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# Small Flask app for hosting platforms that expect a web port
web_app = Flask(__name__)

@web_app.route("/")
def home():
    return "NIFTY PULSE Bot is running ✅"


WELCOME_TEXT = """👋 Welcome to NIFTY PULSE Bot!

This bot provides:
✔️ Premium Pulse Strategy
✔️ Market Tools & Indicators
✔️ Trend, OI, Volatility & FII Analysis

Select an option below."""

PULSE_TEXT = """⚡ <b>PULSE PREMIUM ACCESS</b>

Built for disciplined traders who focus on quality setups, not noise.

🔷 <b>PULSE FRAMEWORK (5 CONFIRMATIONS)</b>

🅿️ Price Action Structure
🆄 Unusual OI Shift
🅻 Institutional Flow Tracking
🆂 Sector Strength Confirmation
🅴 Event Risk Awareness

📊 <b>WHAT YOU GET IN PREMIUM</b>

🔹 High-probability CE/PE setups
🔹 Breakout & reversal zones
🔹 Smart money tracking
🔹 Defined entry, target & SL
🔹 Time-based exit strategy

📌 <b>TRADING PRINCIPLE</b>

No overtrading. No emotional decisions.
Only structured execution.

🚀 Trade Smart. Stay Consistent."""

TOOLS_TEXT = """🛠 <b>Analysis Tools Menu</b>

Choose a tool below:"""


def main_menu_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("⚡ Pulse Strategy", callback_data="pulse")],
        [InlineKeyboardButton("🛠 Analysis Tools", callback_data="tools")],
        [InlineKeyboardButton("📢 Join Channel", url=CHANNEL_LINK)],
        [
            InlineKeyboardButton("👨‍💼 Admin 1", url=ADMIN_1),
            InlineKeyboardButton("👨‍💼 Admin 2", url=ADMIN_2),
        ],
    ])


def back_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("⬅️ Back to Main Menu", callback_data="back_main")]
    ])


def tools_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📈 Trend Analysis Tools", url=TREND_LINK)],
        [InlineKeyboardButton("📊 Derivatives Tools / Option Chain", url=DERIVATIVES_LINK)],
        [InlineKeyboardButton("⚠️ Volatility & Risk Tools", url=VOLATILITY_LINK)],
        [InlineKeyboardButton("🏦 Institutional Activity Tools", url=INSTITUTION_LINK)],
        [InlineKeyboardButton("⬅️ Back to Main Menu", callback_data="back_main")],
    ])


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(WELCOME_TEXT, reply_markup=main_menu_keyboard())


async def pulse_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(PULSE_TEXT, parse_mode="HTML", reply_markup=back_keyboard())


async def tools_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(TOOLS_TEXT, parse_mode="HTML", reply_markup=tools_keyboard())


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == "pulse":
        await query.edit_message_text(PULSE_TEXT, parse_mode="HTML", reply_markup=back_keyboard())

    elif query.data == "tools":
        await query.edit_message_text(TOOLS_TEXT, parse_mode="HTML", reply_markup=tools_keyboard())

    elif query.data == "back_main":
        await query.edit_message_text(WELCOME_TEXT, reply_markup=main_menu_keyboard())


def run_bot() -> None:
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN environment variable is missing.")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("pulse", pulse_command))
    app.add_handler(CommandHandler("tools", tools_command))
    app.add_handler(CallbackQueryHandler(button_handler))

    logger.info("Bot started...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    run_bot()
