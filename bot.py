import os
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")

# ----- Menus -----
MAIN_MENU = ReplyKeyboardMarkup(
    [
        [KeyboardButton("📺 YT Premium Guide")],
        [KeyboardButton("🎁 YT Free Trial / Offers")],
        [KeyboardButton("🧾 Report Templates")],
        [KeyboardButton("🧰 Tools"), KeyboardButton("ℹ️ INFO")],
        [KeyboardButton("⬅️ Back"), KeyboardButton("🏠 Main Menu")],
    ],
    resize_keyboard=True
)

TOOLS_MENU = ReplyKeyboardMarkup(
    [
        [KeyboardButton("📝 Caption Ideas"), KeyboardButton("#️⃣ Hashtag Ideas")],
        [KeyboardButton("🧾 Text Formatter"), KeyboardButton("🔗 Link Tips")],
        [KeyboardButton("⬅️ Back"), KeyboardButton("🏠 Main Menu")],
    ],
    resize_keyboard=True
)

REPORT_MENU = ReplyKeyboardMarkup(
    [
        [KeyboardButton("🎵 TikTok Report"), KeyboardButton("📸 Instagram Report")],
        [KeyboardButton("▶️ YouTube Report")],
        [KeyboardButton("⬅️ Back"), KeyboardButton("🏠 Main Menu")],
    ],
    resize_keyboard=True
)

# Track last menu for Back button
def set_last_menu(context, name: str):
    context.user_data["last_menu"] = name

def get_last_menu(context):
    return context.user_data.get("last_menu", "MAIN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    set_last_menu(context, "MAIN")
    await update.message.reply_text("Main Menu 👇", reply_markup=MAIN_MENU)

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    t = (update.message.text or "").strip()

    # Main menu controls
    if t in ("/start", "🏠 Main Menu"):
        set_last_menu(context, "MAIN")
        await update.message.reply_text("Main Menu 👇", reply_markup=MAIN_MENU)
        return

    if t == "⬅️ Back":
        last = get_last_menu(context)
        # Go back to MAIN always for simplicity
        set_last_menu(context, "MAIN")
        await update.message.reply_text("Back ✅", reply_markup=MAIN_MENU)
        return

    # Main options
    if t == "ℹ️ INFO":
        set_last_menu(context, "MAIN")
        await update.message.reply_text(
            "✅ This is a helper bot with clean menus.\n"
            "YouTube Premium guide, report templates, and tools available.",
            reply_markup=MAIN_MENU
        )
        return

    if t == "🧰 Tools":
        set_last_menu(context, "MAIN")
        await update.message.reply_text("Tools Menu 👇", reply_markup=TOOLS_MENU)
        return

    if t == "🧾 Report Templates":
        set_last_menu(context, "MAIN")
        await update.message.reply_text("Report Menu 👇", reply_markup=REPORT_MENU)
        return

    if t == "📺 YT Premium Guide":
        set_last_menu(context, "MAIN")
        await update.message.reply_text(
            "📺 YouTube Premium Guide:\n"
            "1) YouTube app খুলে Profile চাপো\n"
            "2) Get YouTube Premium\n"
            "3) Plan select (Individual/Family/Student)\n"
            "4) Payment method choose করে Confirm ✅",
            reply_markup=MAIN_MENU
        )
        return

    if t == "🎁 YT Free Trial / Offers":
        set_last_menu(context, "MAIN")
        await update.message.reply_text(
            "🎁 Free Trial/Offers:\n"
            "• Trial সব account এ থাকে না (eligibility লাগে)\n"
            "• YouTube → Get Premium এ গিয়ে offer থাকলে দেখাবে\n"
            "• না থাকলে: Family/Student plan consider করতে পারো ✅",
            reply_markup=MAIN_MENU
        )
        return

    # Tools
    if t == "📝 Caption Ideas":
        await update.message.reply_text(
            "Caption Ideas:\n"
            "• 'New upload ✅ Support needed!'\n"
            "• 'Stay consistent. Stay focused.'\n"
            "• 'Rangpurian vibes 🔥'",
            reply_markup=TOOLS_MENU
        )
        return

    if t == "#️⃣ Hashtag Ideas":
        await update.message.reply_text(
            "#hashtags:\n#bangladesh #rangpur #cyber #contentcreator #team",
            reply_markup=TOOLS_MENU
        )
        return

    if t == "🧾 Text Formatter":
        await update.message.reply_text(
            "Text Formatter (simple):\n"
            "Send a line, I will return it in a clean format (next update এ auto বানাবো).",
            reply_markup=TOOLS_MENU
        )
        return

    if t == "🔗 Link Tips":
        await update.message.reply_text(
            "Link Tips:\n"
            "• Official links use করো\n"
            "• Suspicious short links avoid করো\n"
            "• Bio link short & clean রাখো ✅",
            reply_markup=TOOLS_MENU
        )
        return

    # Report templates (safe)
    if t == "🎵 TikTok Report":
        await update.message.reply_text(
            "TikTok Report Template:\n"
            "This content violates TikTok’s rules by promoting harmful or misleading activity. "
            "Please review and take action.",
            reply_markup=REPORT_MENU
        )
        return

    if t == "📸 Instagram Report":
        await update.message.reply_text(
            "Instagram Report Template:\n"
            "This account is posting abusive or harassing content. Please review under the "
            "Harassment & Bullying policy and take action for safety.",
            reply_markup=REPORT_MENU
        )
        return

    if t == "▶️ YouTube Report":
        await update.message.reply_text(
            "YouTube Report Template:\n"
            "This video violates YouTube policies by encouraging harmful or deceptive behavior. "
            "Please review and remove/limit it as appropriate.",
            reply_markup=REPORT_MENU
        )
        return

    # Default
    await update.message.reply_text("Menu থেকে একটা option চাপো 🙂", reply_markup=MAIN_MENU)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))
    app.run_polling()

if __name__ == "__main__":
    main()
