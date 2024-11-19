#Добавляем название базовой валюты

from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests
from setuptools.logging import configure


def update_b_label(event):
    # Получаем полное название базовой валюты из словаря и обновляем метку
    code = b_combobox.get()
    name = currencies[code]
    b_label.config(text=name)

def update_b2_label(event):
    # Получаем полное название второй базовой валюты из словаря и обновляем метку
    code = b2_combobox.get()
    name = currencies[code]
    b2_label.config(text=name)

def update_t_label(event):
    # Получаем полное название целевой валюты из словаря и обновляем метку
    code = t_combobox.get()
    name = currencies[code]
    t_label.config(text=name)

def exchange():
    target_code = t_combobox.get()
    base_code = b_combobox.get()
    base2_code = b2_combobox.get() #ДОБАВИЛ-1

    if target_code and base_code and base2_code: #ДОБАВИЛ-2
        try:
            response = requests.get(f'https://open.er-api.com/v6/latest/{base_code}')
            response.raise_for_status()

            data = response.json()

            if target_code in data['rates']:
                exchange_rate = data['rates'][target_code]
                base = currencies[base_code]
                target = currencies[target_code]
                mb.showinfo("Курс обмена", f"Курс {exchange_rate:.1f} {target} за 1 {base}")
            else:
                mb.showerror("Ошибка", f"Валюта {target_code} не найдена")
        except Exception as e:
            mb.showerror("Ошибка", f"Ошибка: {e}")
    else:
        mb.showwarning("Внимание", "Выберите коды валют")

# Словарь кодов валют и их полных названий
currencies = {
    "USD": "Американский доллар",
    "EUR": "Евро",
    "JPY": "Японская йена",
    "GBP": "Британский фунт стерлингов",
    "AUD": "Австралийский доллар",
    "CAD": "Канадский доллар",
    "CHF": "Швейцарский франк",
    "CNY": "Китайский юань",
    "RUB": "Российский рубль",
    "KZT": "Казахстанский тенге",
    "UZS": "Узбекский сум"
}

# Создание графического интерфейса
window = Tk()
window.title("Курс обмена валюты")
window.geometry("360x430")

Label(text="Базовая валюта:", font='Arial 9').pack(padx=10, pady=5)
b_combobox = ttk.Combobox(values=list(currencies.keys()))
b_combobox.pack(padx=10, pady=5)
b_combobox.bind("<<ComboboxSelected>>", update_b_label)

b_label = ttk.Label()
b_label.pack(padx=10, pady=5)

Label(text="").pack(padx=10, pady=5)

Label(text="Вторая базовая валюта:", font='Arial 9').pack(padx=10, pady=5)
b2_combobox = ttk.Combobox(values=list(currencies.keys()))
b2_combobox.pack(padx=10, pady=5)
b2_combobox.bind("<<ComboboxSelected>>", update_b2_label)

b2_label = ttk.Label()
b2_label.pack(padx=10, pady=5)

Label(text="").pack(padx=10, pady=5)

Label(text="Целевая валюта:", font='Arial 9').pack(padx=10, pady=5)
t_combobox = ttk.Combobox(values=list(currencies.keys()))
t_combobox.pack(padx=10, pady=5)
t_combobox.bind("<<ComboboxSelected>>", update_t_label)

t_label = ttk.Label()
t_label.pack(padx=10, pady=5)

Button(text="Получить курс обмена", font='Arial 9 bold', command=exchange).pack(padx=10, pady=30)

window.mainloop()