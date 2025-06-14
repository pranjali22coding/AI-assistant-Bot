# from tkinter import *
# from PIL import Image, ImageTk
# import speech_to_text
# import action

# def ask():
#     ask_val = speech_to_text.speech_to_text()
#     bot_val = action.Action(ask_val)
#     text.insert(END, "Me --> " + ask_val + "\n")
#     if bot_val:
#         text.insert(END, "Bot <-- " + str(bot_val) + "\n")
#     if bot_val == "ok sir":
#         root.destroy()

# def send():
#     send_val = entry.get()
#     bot_val = action.Action(send_val)
#     text.insert(END, "Me --> " + send_val + "\n")
#     if bot_val:
#         text.insert(END, "Bot <-- " + str(bot_val) + "\n")
#     if bot_val == "ok sir":
#         root.destroy()

# def del_text():
#     text.delete("1.0", "end")

# root = Tk()
# root.title("Doraemon Assistant")
# root.geometry("550x675")
# root.resizable(False, False)
# root.config(bg="#FAF16E")

# frame = Frame(root, bg="#FAF16E", padx=20, pady=20)
# frame.pack(expand=True)

# text_label = Label(frame, text="Doraemon Assistant", font=("Comic Sans MS", 14, "bold"), bg="#FA9999")
# text_label.pack(pady=(0, 20))

# img = Image.open("doraemon_cute.jpg").resize((250, 250))
# photo = ImageTk.PhotoImage(img)
# image_label = Label(frame, image=photo, bg="#FAF16E")
# image_label.pack(pady=(0, 20))

# text = Text(frame, font=("Courier", 10, "bold"), bg="#FA9999", height=6, width=35)
# text.pack()

# entry = Entry(root, justify=CENTER)
# entry.place(x=150, y=500, width=250, height=30)

# Button(root, text="ASK", bg="#FFFFFF", pady=16, padx=40, borderwidth=3, relief=SOLID, command=ask).place(x=60, y=545)
# Button(root, text="SEND", bg="#FFFFFF", pady=16, padx=40, borderwidth=3, relief=SOLID, command=send).place(x=210, y=545)
# Button(root, text="DELETE", bg="#FFFFFF", pady=16, padx=40, borderwidth=3, relief=SOLID, command=del_text).place(x=360, y=545)

# root.mainloop()

from tkinter import *
from PIL import Image, ImageTk
import speech_to_text
import action

def ask():
    ask_val = speech_to_text.speech_to_text()

    if not ask_val:
        text.insert(END, "Me --> (No speech detected)\n")
        return

    text.insert(END, "Me : " + ask_val + "\n")

    bot_val = action.Action(ask_val)
    if bot_val:
        text.insert(END, "Doraemon : " + str(bot_val) + "\n")
        if bot_val == "ok sir":
            root.destroy()


def send():
    send_val = entry.get()
    if send_val.strip() == "":
        return
    bot_val = action.Action(send_val)
    text.insert(END, "Me --> " + send_val + "\n")
    if bot_val:
        text.insert(END, "Bot <-- " + str(bot_val) + "\n")
        if bot_val == "ok sir":
            root.destroy()

def del_text():
    text.delete("1.0", END)

# GUI Window Setup
root = Tk()
root.title("Doraemon Assistant")
root.geometry("550x650")
root.resizable(False, False)
root.configure(bg="#FAF16E")

# Title
title = Label(root, text="Doraemon Assistant", font=("Comic Sans MS", 18, "bold"), bg="#FA9999", pady=10)
title.pack(pady=10)

# Doraemon Image
try:
    image = Image.open("doraemon_cute.jpg").resize((250, 250))
    photo = ImageTk.PhotoImage(image)
    img_label = Label(root, image=photo, bg="#FAF16E")
    img_label.image = photo  # prevent garbage collection
    img_label.pack()
except Exception as e:
    error_label = Label(root, text="(Image Not Found)", font=("Arial", 12), bg="#FAF16E", fg="red")
    error_label.pack(pady=10)

# Chat Box
text = Text(root, font=("Courier", 10, "bold"), bg="#FA9999", height=8, width=50)
text.pack(pady=10)

# Entry Box
entry = Entry(root, font=("Arial", 12), justify=CENTER)
entry.pack(pady=10, ipady=5, ipadx=5)

# Buttons Frame
btn_frame = Frame(root, bg="#FAF16E")
btn_frame.pack(pady=10)

Button(btn_frame, text="ASK", bg="#FFFFFF", padx=30, pady=10, command=ask).grid(row=0, column=0, padx=10)
Button(btn_frame, text="SEND", bg="#FFFFFF", padx=30, pady=10, command=send).grid(row=0, column=1, padx=10)
Button(btn_frame, text="DELETE", bg="#FFFFFF", padx=30, pady=10, command=del_text).grid(row=0, column=2, padx=10)

# Start GUI
root.mainloop()
