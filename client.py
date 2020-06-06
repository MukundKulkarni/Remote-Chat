from socket import AF_INET, SOCK_STREAM
from threading import  Thread

import tkinter




top = tkinter.Tk()
top.title("iChat")
messages_frame = tkinter.Frame(top)
my_message = tkinter.StringVar()
my_message.set("Type your message here.")
scrollbar = tkinter.Scrollbar(messages_frame)

message_list = tkinter.Listbox(messages_frame, height = 30, width = 75, yscrollcommand = scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
message_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
message_list.pack()
messages_frame.pack()


entry_field = tkinter.Entry(top, textvariable=my_message, width=70)
entry_field.bind("<return>")
entry_field.pack(side=tkinter.LEFT, padx = 8)

send_button = tkinter.Button(top, text="Send")
send_button.pack(side=tkinter.RIGHT, pady=4)

top.protocol("WM_DELETE_WINDOW")


tkinter.mainloop()
