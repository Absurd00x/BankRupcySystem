import tkinter as tk

HEIGHT = 600
WIDTH = 800
LIGHT_BLUE_CODE = '#05FAEA'

root = tk.Tk()

bg_image = tk.PhotoImage(file='background.png')
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# Хочу, чтобы изначально окно открывалось в размере 800х600
init_bg_image = tk.PhotoImage(file='background-800x600.png')
init_bg_image = tk.Label(root, height=HEIGHT, width=WIDTH, image=init_bg_image)
init_bg_image.place(relwidth=1, relheight=1)

frame1 = tk.Frame(root, bg=LIGHT_BLUE_CODE)
frame1.place(relx=0.017, relwidth=0.3, relheight=0.1)
frame2 = tk.Frame(root, bg='#FA0000')
frame2.place(relx=0.351, relwidth=0.3, relheight=0.1)
frame3 = tk.Frame(root, bg='#00FA00')
frame3.place(relx=0.685, relwidth=0.3, relheight=0.1)

tk.mainloop()
