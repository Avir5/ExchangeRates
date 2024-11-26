from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests


def update_cryptocur_label(event):
    global name
    # Получаем полное название криптовалюты из словаря и обновляем метку
    code = combobox.get()
    name = currencies[code]
    currency_label.config(text=name)


def exchange():
    code = combobox.get()
    if code:
        try:
            response = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={name}&vs_currencies=usd")
            response.raise_for_status()
            data = response.json() #получаем словарь из ключа-значения

            if name.lower() in data.keys():
                exchange_rate = (data.get(name.lower())).get('usd')
                currency_name = currencies[code] #получаем название криптовалюты
                mb.showinfo("Курс обмена криптовалюты", f"Курс {exchange_rate} долларов за один {currency_name}")
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
"DOGE": "Dogecoin",
"ADA": "Cardano",
"TRX": "TRON",
"XLM": "Stellar",
"pDOTn": "Polkadot",
"LINK": "Chainlink"
}

# Создание графического интерфейса
window = Tk()
window.title("Курс обмена криптовалюты")
window.geometry("360x180")

Label(text="Выберите код криптовалюты:").pack(padx=10, pady=10)

combobox = ttk.Combobox(values=list(currencies.keys()))
combobox.pack(padx=10, pady=10)
combobox.bind("<<ComboboxSelected>>", update_cryptocur_label)

currency_label = ttk.Label()
currency_label.pack(padx=10, pady=10)

Button(text="Получить курс обмена к доллару", command=exchange).pack(padx=10, pady=10)

window.mainloop()
