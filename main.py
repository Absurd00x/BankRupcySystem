import tkinter as tk

HEIGHT = 600
WIDTH = 800
WINDOW_COLOUR_CODE = '#404040'

root = tk.Tk()

init_bg_image = tk.PhotoImage(file='background800x600.png')
init_bg_label = tk.Label(root, width=WIDTH, height=HEIGHT, image=init_bg_image)
init_bg_label.pack()

bg_image = tk.PhotoImage(file='background.png')
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

title1 = tk.Label(root, bg=WINDOW_COLOUR_CODE,
                  fg='white', text='Список пользователей')
title1.place(relx=0.017, relwidth=0.3, relheight=0.1)
title2 = tk.Label(root, bg=WINDOW_COLOUR_CODE,
                  fg='white', text='Информация о пользователе')
title2.place(relx=0.351, relwidth=0.3, relheight=0.1)
title3 = tk.Label(root, bg=WINDOW_COLOUR_CODE,
                  fg='white', text='Возможные операции')
title3.place(relx=0.685, relwidth=0.3, relheight=0.1)

tk.mainloop()
