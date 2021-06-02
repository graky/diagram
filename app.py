import tkinter
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg)
import matplotlib.pyplot as plt

window = tkinter.Tk()
window.geometry('1360x768')
window.title("Курсовая Гребенкин")


def diagram_create():
    diagram_window = tkinter.Toplevel(window)
    diagram_window.title('Кольцевая параметрическая секторная диаграмма')
    diagram_window.geometry('800x600')
    main_frame = tkinter.Frame(diagram_window)
    main_frame.pack(fill=tkinter.BOTH, expand=1)
    my_canvas = tkinter.Canvas(main_frame)
    my_canvas.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    diagran_frame = tkinter.Frame(my_canvas)
    my_canvas.create_window((0, 0), window=diagran_frame, anchor="nw")
    diagram_name = main_entry.get()
    par_val_dict = {
        par_entry1.get(): val_entry1.get(),
        par_entry2.get(): val_entry2.get(),
        par_entry3.get(): val_entry3.get(),
        par_entry4.get(): val_entry4.get(),
        par_entry5.get(): val_entry5.get(),
        par_entry6.get(): val_entry6.get(),
        par_entry7.get(): val_entry7.get(),
        par_entry8.get(): val_entry8.get(),
        par_entry9.get(): val_entry9.get(),
        par_entry10.get(): val_entry10.get(), }
    del_list = []

    def get_str(val):
        flag = False
        for lit in val:
            if lit not in '0123456789':
                flag = True
        return flag

    for key in par_val_dict.keys():
        if key == '' or get_str(par_val_dict[key]):
            del_list.append(key)
    for key_del in del_list:
        del par_val_dict[key_del]
    plt.figure(figsize=(6, 6))
    plt.pie([int(val) for val in par_val_dict.values()], labels=par_val_dict.keys())
    my_circle = plt.Circle((0, 0), 0.7, color='white')
    p = plt.gcf()
    p.gca().add_artist(my_circle)

    canvas = FigureCanvasTkAgg(p, master=diagran_frame)
    canvas.draw()
    name = tkinter.Label(diagran_frame, text=diagram_name, width=50, )
    name.grid(column=0, row=0, padx=100)
    canvas.get_tk_widget().grid(row=1, column=0, sticky='e')


main_info = tkinter.Label(window, text='Введите название диаграммы', width=50, )
main_info.grid(column=0, row=0, pady=0)
main_entry = tkinter.Entry(window, width=50)
main_entry.grid(column=0, row=1, )


par_1 = tkinter.Label(window, text='Введите название первого парамметра', width=50, justify='left')
par_1.grid(column=0, row=2)
par_2 = tkinter.Label(window, text='Введите название второго парамметра', width=50, justify='left')
par_2.grid(column=0, row=3)
par_3 = tkinter.Label(window, text='Введите название третьего парамметра', width=50, justify='left')
par_3.grid(column=0, row=4)
par_4 = tkinter.Label(window, text='Введите название четвертого парамметра', width=50, justify='left')
par_4.grid(column=0, row=5)
par_5 = tkinter.Label(window, text='Введите название пятого парамметра', width=50, justify='left')
par_5.grid(column=0, row=6)
par_6 = tkinter.Label(window, text='Введите название шестого парамметра', width=50, justify='left')
par_6.grid(column=0, row=7)
par_7 = tkinter.Label(window, text='Введите название седьмого парамметра', width=50, justify='left')
par_7.grid(column=0, row=8)
par_8 = tkinter.Label(window, text='Введите название восьмого парамметра', width=50, justify='left')
par_8.grid(column=0, row=9)
par_9 = tkinter.Label(window, text='Введите название девятого парамметра', width=50, justify='left')
par_9.grid(column=0, row=10)
par_10 = tkinter.Label(window, text='Введите название десятого парамметра', width=50, justify='left')
par_10.grid(column=0, row=11)
par_entry1 = tkinter.Entry(window, width=50)
par_entry1.grid(column=2, row=2)
par_entry2 = tkinter.Entry(window, width=50)
par_entry2.grid(column=2, row=3)
par_entry3 = tkinter.Entry(window, width=50)
par_entry3.grid(column=2, row=4)
par_entry4 = tkinter.Entry(window, width=50)
par_entry4.grid(column=2, row=5)
par_entry5 = tkinter.Entry(window, width=50)
par_entry5.grid(column=2, row=6)
par_entry6 = tkinter.Entry(window, width=50)
par_entry6.grid(column=2, row=7)
par_entry7 = tkinter.Entry(window, width=50)
par_entry7.grid(column=2, row=8)
par_entry8 = tkinter.Entry(window, width=50)
par_entry8.grid(column=2, row=9)
par_entry9 = tkinter.Entry(window, width=50)
par_entry9.grid(column=2, row=10)
par_entry10 = tkinter.Entry(window, width=50)
par_entry10.grid(column=2, row=11)
val_1 = tkinter.Label(window, text='Введите значение первого парамметра', width=50, justify='left')
val_1.grid(column=4, row=2)
val_2 = tkinter.Label(window, text='Введите значение второго парамметра', width=50, justify='left')
val_2.grid(column=4, row=3)
val_3 = tkinter.Label(window, text='Введите значение третьего парамметра', width=50, justify='left')
val_3.grid(column=4, row=4)
val_4 = tkinter.Label(window, text='Введите значение четвертого парамметра', width=50, justify='left')
val_4.grid(column=4, row=5)
val_5 = tkinter.Label(window, text='Введите значение пятого парамметра', width=50, justify='left')
val_5.grid(column=4, row=6)
val_6 = tkinter.Label(window, text='Введите значение шестого парамметра', width=50, justify='left')
val_6.grid(column=4, row=7)
val_7 = tkinter.Label(window, text='Введите значение седьмого парамметра', width=50, justify='left')
val_7.grid(column=4, row=8)
val_8 = tkinter.Label(window, text='Введите значение восьмого парамметра', width=50, justify='left')
val_8.grid(column=4, row=9)
val_9 = tkinter.Label(window, text='Введите значение девятого парамметра', width=50, justify='left')
val_9.grid(column=4, row=10)
val_10 = tkinter.Label(window, text='Введите значение десятого парамметра', width=50, justify='left')
val_10.grid(column=4, row=11)
val_entry1 = tkinter.Entry(window, width=10)
val_entry1.grid(column=6, row=2)
val_entry2 = tkinter.Entry(window, width=10)
val_entry2.grid(column=6, row=3)
val_entry3 = tkinter.Entry(window, width=10)
val_entry3.grid(column=6, row=4)
val_entry4 = tkinter.Entry(window, width=10)
val_entry4.grid(column=6, row=5)
val_entry5 = tkinter.Entry(window, width=10)
val_entry5.grid(column=6, row=6)
val_entry6 = tkinter.Entry(window, width=10)
val_entry6.grid(column=6, row=7)
val_entry7 = tkinter.Entry(window, width=10)
val_entry7.grid(column=6, row=8)
val_entry8 = tkinter.Entry(window, width=10)
val_entry8.grid(column=6, row=9)
val_entry9 = tkinter.Entry(window, width=10)
val_entry9.grid(column=6, row=10)
val_entry10 = tkinter.Entry(window, width=10)
val_entry10.grid(column=6, row=11)

create_diagram = tkinter.Button(window, text='Создать диаграмму', command=diagram_create, )
create_diagram.grid(column=2, row=12)

window.mainloop()
