
from tkinter import * #библиотека для создания приложений с графическим интерфейсом
from tkinter import ttk #содержит классы более стилизованных и современных виджетов
from tkinter import messagebox as mb #для создания окон сообщений в Tkinter на Python
import requests #библиотека, которая упрощает работу с HTTP-запросами

def update_cryptocur_label(event):
    '''ф-ция, получает из поля выбора combobox код криптовалюты и её полное название из словаря для обновления метки'''
    global name #объявление глобальной переменной NAME для видимости во всём коде программы
    code = combobox.get() #присваивание переменной кода криптовалюты из поля выбора COMBOBOX методом GET
    name = currencies[code] #присваивание переменной названия криптовалюты из словаря по индексу CODE
    currency_label.config(text=name) #обновление текста метки - название криптовалюты


def exchange():
    '''ф-ция, выполняет запрос к API сайта coingecko.com для получения курса выбранной пользователем криптовалюты и
        выводит в информационное всплывающее окно её название и цифровое значение к доллару'''
    code = combobox.get() #присваивание переменной кода криптовалюты из поля выбора COMBOBOX методом GET
    if code: #условие для проверки - сделал ли пользователь выбор кода криптовалюты в поле COMBOBOX
        try: #обработка исключения при выплонении запроса к сайту
            #перемен.присваив.результат, выполн.с помощью метода REQUESTS.GET. Метод предназн.для получения данных из различных веб-ресурсов
            response = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={name}&vs_currencies=usd")
            response.raise_for_status() #метод возвращает объект HTTPError при возникновении ошибки во время процесса запроса
            data = response.json() #перемен.присваив.словарь - ключ-значение (метод возвращает JSON-объект полученного результата)

            if name.lower() in data.keys(): #условие для проверки - содержит ли перемен.DATA название криптовалюты из перемен.NAME
                exchange_rate = (data.get(name.lower())).get('usd') #перемен.присваив. цифровое значение курса криптовалюты
                currency_name = currencies[code] #перемен.присваив. название криптовалюты
                #метод использ.для отображения некоторой информации, в конкретном случае для отображ.названия и курса криптовалюты
                mb.showinfo("Курс обмена криптовалюты", f"Курс {exchange_rate} долларов за один {currency_name}")
            else:
                mb.showerror("Ошибка", f"Валюта {code} не найдена")
        except Exception as e:
            mb.showerror("Ошибка", f"Ошибка: {e}")
    else:
        mb.showwarning("Внимание", "Выберите код криптовалюты")

#словарь кодов криптовалют и их полных названий
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
"LINK": "Chainlink",
"BNB": "Binance Coin"
}

#блок для создания графического интерфейса
window = Tk()
window.title("Курс обмена криптовалюты")
window.geometry("360x180")

#ВИДЖЕТЫ (предназначение)
#создание текстой метки и вывода статического текста
Label(text="Выберите код криптовалюты:").pack(padx=10, pady=10)
                                    #метод задаёт видимость элемента в окне, упорядочивает
                                    #виджеты по горизонтали или вертикали позволяет задать
                                    #внешние (padx и pady) отступы

#создание выпадающего списка, для выбора одного из элементов списка
combobox = ttk.Combobox(values=list(currencies.keys()))
combobox.pack(padx=10, pady=10)
combobox.bind("<<ComboboxSelected>>", update_cryptocur_label)

#создание текстой метки и вывода статического текста
currency_label = ttk.Label()
currency_label.pack(padx=10, pady=10)

#создание кнопки, command параметр указывает функцию вызываемую при нажатии на кнопку
Button(text="Получить курс обмена к доллару", command=exchange).pack(padx=10, pady=10)

#метод, который запускает главный цикл обработки событий,
#постоянно обновляя и отображая интерфейс пользователю
window.mainloop()
