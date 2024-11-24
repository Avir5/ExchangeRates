from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests

def update_cryptocur_label(event):
    # Получаем полное название криптовалюты из словаря и обновляем метку
    code = combobox.get()
    name = currencies[code]
    currency_label.config(text=name)

def exchange():
    code = combobox.get()

    if code:
        try:
            response = requests.get('https://open.er-api.com/v6/latest/USD')
            response.raise_for_status()

            data = response.json()

            if code in data['rates']:
                exchange_rate = data['rates'][code]
                currency_name = currencies[code] # currencies.get(code, code)
                mb.showinfo("Курс обмена", f"Курс к доллару: {exchange_rate:.1f} {currency_name} за 1 доллар")
            else:
                mb.showerror("Ошибка", f"Валюта {code} не найдена")
        except Exception as e:
            mb.showerror("Ошибка", f"Ошибка: {e}")
    else:
        mb.showwarning("Внимание", "Выберите код криптовалюты")

# Словарь кодов валют и их полных названий
currencies = {
"BTC": "Bitcoin",
"ETH": "Ethereum",
"USDT": "Tether",
"SOL": "Solana",
"BNB": "Binance Coin",
"XRP": "XRP",
"DOGE": "Dogecoin",
"USDC": "U.S. Dollar Coin",
"ADA": "Cardano",
"TRX": "TRON",
"USD": "Американский доллар"
}

# Создание графического интерфейса
window = Tk()
window.title("Курс обмена криптовалюты к доллару")
window.geometry("360x180")

Label(text="Выберите код криптовалюты:").pack(padx=10, pady=10)

combobox = ttk.Combobox(values=list(currencies.keys()))
combobox.pack(padx=10, pady=10)
combobox.bind("<<ComboboxSelected>>", update_cryptocur_label)

currency_label = ttk.Label()
currency_label.pack(padx=10, pady=10)

Button(text="Получить курс обмена к доллару", command=exchange).pack(padx=10, pady=10)

window.mainloop()
