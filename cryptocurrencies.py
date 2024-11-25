from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests

#name=None

def update_cryptocur_label(event):
    global name
    # Получаем полное название криптовалюты из словаря и обновляем метку
    code = combobox.get()
    name = currencies[code]
    currency_label.config(text=name)
    #name=name.lower()
    print('Lower name:',name)

def exchange():
    #nonlocal name
    code = combobox.get()
    if code:
        try:
            #response = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids=m{name}&vs_currencies=usd")
            response = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
            #https://api.coingecko.com/api/v3/simple/price?ids=%7Bcrypto_code%7D&vs_currencies=%7Bbase_code%7D
            #https://api.coingecko.com/api/v3/coins/list
            response.raise_for_status()
            print('Статус:',response)

            data = response.json()
            print("data:",data)
            print('name_after_data',name)
            #print('Name and Code:', data[0][code])
            #for key_data, (b, c) in enumerate(data.items()):
            #tuple_data=data.items()
            #print('Tuple_data:',tuple_data)
            if name in data[name.lower().values()]:
                print(name)
                exchange_rate = data[name][usd]
                print(exchange_rate)
                currency_name = currencies[code]  # currencies.get(code, code)
                print(currency_name)
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
