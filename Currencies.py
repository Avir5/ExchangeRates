from tkinter import *
from tkinter import messagebox as mb
import requests
from tkinter import ttk

#from Задания.холст import window


def exchange():
    code=combobox.get().upper()#получаем базовую валюту
    target=target_combobox.get().upper()#получаем целевую валюту
    if code and target:
        try:
            response=requests.get(f'https://open.er-api.com/v6/latest/{code}')
            data=response.json()
            if target in data['rates']:
                exchange_rate=data['rates'][target]
                base=popular_cur[code]
                cur_name=popular_cur[target]
                mb.showinfo('Курс обмена',
                            f'Курс: {exchange_rate:.2f} {cur_name} за 1 {base}.')
            else:
                mb.showerror('Ошибка', f'Валюта {target} не найдена')
        except Exception as e:
            mb.showerror('Ошибка', e)
    else:
        mb.showwarning('Внимание!', 'Вы не ввели код валюты.')


def update_label(event):
    code=combobox.get()
    name=popular_cur[code]
    cur_label['text']=name



#popular_cur = ["EUR", "JPY", "GBP", "AUD", "CAD", "CHF", "CNY", "RUB", "KZT", "UZS"]
popular_cur={"EUR": "Евро", "JPY": "Японская йена", "GBP": "Британский фунт стерлингов",
"AUD": "Австралийский доллар", "CAD": "Канадский доллар", "CHF": "Швейцарский франк",
"CNY": "Китайский юань", "RUB": "Российский рубль", "KZT": "Казахстанский тенге",
"UZS": "Узбекский сум"}

window=Tk()
window.title('Курс обмена валют')
window.geometry('400x150')

Label(text='Выберите код базовой валюты: ').pack()
combobox=ttk.Combobox(values=list(popular_cur.keys()))
combobox.pack()
combobox.bind('<<ComboboxSelected>>', update_label)

cur_label=Label(height=2)
cur_label.pack()

Label(text='Выберите код целевой валюты: ').pack()
target_combobox=ttk.Combobox(values=list(popular_cur.keys()))
target_combobox.pack()
target_combobox.bind('<<ComboboxSelected>>', update_label)

Button(text='Получить курс обмена', command=exchange).pack()

window.mainloop()