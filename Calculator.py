import tkinter as tk
from tkinter import font

# Создание класса Calculator
class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Калькулятор")  # Установка заголовка главного окна
        master.geometry("300x320")  # Задание размеров главного окна
        master.resizable(False, False)  # Запрет изменения размера окна

        self.entry = tk.Entry(master)  # Создание поля ввода
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=78)  # Размещение поля ввода на сетке

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]  # Значения кнопок для размещения на калькуляторе

        menu_frame = tk.Frame(master)  # Создание контейнера для кнопок
        menu_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Размещение контейнера по центру окна

        button_font = font.Font(weight='bold')  # Создание шрифта для кнопок

        # Создание кнопок
        for i in range(len(buttons)):
            for j in range(len(buttons[i])):
                button = tk.Button(menu_frame, text=buttons[i][j], width=5, height=2,
                                   font=button_font)  # Создание кнопки
                button.grid(row=i, column=j, padx=5, pady=5, sticky="nsew")  # Размещение кнопки на сетке
                button.bind('<Button-1>', self.button_click)  # Привязка события нажатия кнопки к методу button_click

    def button_click(self, event):
        current = self.entry.get()  # Получение текущего значения из поля ввода
        text = event.widget.cget("text")  # Получение текста нажатой кнопки

        if text == '=':
            try:
                result = eval(current)  # Вычисление результата
                self.entry.delete(0, tk.END)  # Очистка поля ввода
                self.entry.insert(tk.END, str(result))  # Вставка результата в поле ввода
            except:
                self.entry.delete(0, tk.END)  # Очистка поля ввода
                self.entry.insert(tk.END, "Ошибка!")  # Вывод сообщения об ошибке
        else:
            self.entry.insert(tk.END, text)  # Добавление текста кнопки в поле ввода


if __name__ == '__main__':
    root = tk.Tk()  # Создание главного окна
    # Центрирование окна по центру экрана
    window_width = 300
    window_height = 320
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    calculator = Calculator(root)
    root.mainloop()
