#Импортируем необходимые для работы программы библиотеки
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests
from future.utils import raise_


def update_b_label(event):
    '''ф-ция для получения полного названия базовой валюты из словаря currencies и обновления метки'''
    code = b_combobox.get()
    name = currencies[code]
    b_label.config(text=name)


def update_b2_label(event):
    '''ф-ция для получения полного названия 2-й базовой валюты из словаря currencies и обновления метки'''
    code = b2_combobox.get()
    name = currencies[code]
    b2_label.config(text=name)


def update_t_label(event):
    '''ф-ция для получения полного названия целевой валюты из словаря currencies и обновления метки'''
    code = t_combobox.get()
    name = currencies[code]
    t_label.config(text=name)

def exchange():
    '''ф-ция для выполнения запроса к ресурсу с курсами валют и вывода курсов валют, выбраных пользователем, в окно messagebox'''
    target_code = t_combobox.get() #присваивание переменной названия целевой валюты
    base_code = b_combobox.get() #присваивание переменной названия базовой валюты
    base2_code = b2_combobox.get() #присваивание переменной названия 2-й базовой валюты

    if target_code and base_code and base2_code:
        #проверка, на заполнение пользователем, всех полей для выбора валют
        try: #блок для обработки исключения
            #присвоение переменным результа get запроса по выбраной валюте, а также статуса успешности запроса
            response = requests.get(f'https://open.er-api.com/v6/latest/{base_code}')
            response.raise_for_status()
            response2 = requests.get(f'https://open.er-api.com/v6/latest/{base2_code}')
            response2.raise_for_status()

            #присваивание переменным результата преобразования JSON-данных в Python-словарь
            data = response.json()
            data2 = response2.json()

            if target_code in data['rates']:
                #присваивание переменной курса базовой валюты по отношению к целевой валюте
                exchange_rate = data['rates'][target_code]
                base = currencies[base_code] #присваивание переменной названия базовой валюты
                #присваивание переменной курса 2-й базовой валюты по отношению к целевой валюте
                exchange2_rate = data2['rates'][target_code]
                base2 = currencies[base2_code] #присваивание переменной названия второй базовой валюты
                target = currencies[target_code] #присваивание переменной названия целевой валюты
                #вывод в информационное окно, выбранных пользователем, курсов валют по отношению к целевой валюте
                mb.showinfo("Курсы обмена", f"Курс {exchange_rate:.1f} {target} за 1 {base}\n\n"
                            f"Курс {exchange2_rate:.1f} {target} за 1 {base2}")
            else:
                #вывод в информационное окно, сообщения об ошибке выбора валюты
                mb.showerror("Ошибка", f"Валюта {target_code} не найдена")
        except Exception as e:
            mb.showerror("Ошибка", f"Ошибка: {e}")
    else:
        #вывод в информационное окно предупреждения о необходимости выбора кода валюты
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

#Блок меток, полей выбора валют и кнопка для вызова функции exchange
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

#функция бесконечного цикла окна для ожидания любого взаимодействия с пользователем
window.mainloop()