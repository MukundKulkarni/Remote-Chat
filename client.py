from socket import AF_INET, SOCK_STREAM, socket
from threading import  Thread

import tkinter


def receive():
    while True:
        try:
            msg = client_socket.recv(BUFF_SIZE).decode("utf8")
            message_list.insert(tkinter.END, msg)
        except OSError:
            break

def send(event=None):
    msg = my_message.get()
    my_message.set("")
    client_socket.send(bytes(msg, "utf8"))
    if msg == '{EXIT}':
        client_socket.close()
        top.quit()


def on_closing(event=None):
    my_message.set('{EXIT}')
    send()


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
entry_field.bind("Enter", send)
entry_field.pack(side=tkinter.LEFT, padx = 8)

send_button = tkinter.Button(top, text="Send", command=send)
send_button.pack(side=tkinter.RIGHT, pady=4)

top.protocol("WM_DELETE_WINDOW", on_closing)



HOST = input("Enter host: ")
PORT = input("Port: ")

if not PORT:
    PORT = 33000
else:
    PORT = int(PORT)


BUFF_SIZE = 1024
ADDRS = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDRS)

receive_thread = Thread(target = receive)
receive_thread.start()
tkinter.mainloop()
