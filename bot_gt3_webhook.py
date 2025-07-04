import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot activo. Usa /prueba para ver el resumen.")

async def prueba(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = (
        "Resumen diario GT3 siniestrados:
"
        "- https://plc.auction/es/auction/from-de/porsche/911
"
        "- https://www.copart.com/lotSearchResults
"
        "- https://abetter.bid/en/car-finder/model-911/year-2013-2025?search_query=Porsche+911+
"
        "- https://m.mobile.de/auto/search.html?cn=DE&dam=true&ms=20100%3B28%3B%3B&od=up&ref=dsp&s=Car&sb=rel&vc=Car
"
        "- https://www.salvagemarket.co.uk/Search?searchText=porsche%20911
"
        "- https://www.autoscout24.es/lst/porsche/992/ve_gt3?cy=D%2CA%2CB%2CE%2CF%2CI%2CL%2CNL
"
        "- https://www.iaai.com/Search?url=fWKBIzm5vlJ9CQqZKqq7rtcwGIzX5ILavqfA30taAYA%3d
"
        "- https://www.iaai.com/VehicleDetail/42512601~US"
    )
    await update.message.reply_text(texto)

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("prueba", prueba))

    # Webhook en lugar de polling
    app.run_webhook(
        listen="0.0.0.0",
        port=10000,
        webhook_url=WEBHOOK_URL
    )

if __name__ == "__main__":
    main()