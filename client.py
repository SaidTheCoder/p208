import socket
from threading import Thread
from tkinter import *
from tkinter import ttk


PORT  = 8080
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096


name = None
listbox =  None
textarea= None
labelchat = None
text_message = None




# Boilerplate Code
def receiveMessage():
    global SERVER
    global BUFFER_SIZE

    while True:
        chunk = SERVER.recv(BUFFER_SIZE)
        try:
            if("tiul" in chunk.decode() and "1.0," not in chunk.decode()):
                letter_list = chunk.decode().split(",")
                listbox.insert(letter_list[0],letter_list[0]+":"+letter_list[1]+": "+letter_list[3]+" "+letter_list[5])
                print(letter_list[0],letter_list[0]+":"+letter_list[1]+": "+letter_list[3]+" "+letter_list[5])
            else:
                textarea.insert(END,"\n"+chunk.decode('ascii'))
                textarea.see("end")
                print(chunk.decode('ascii'))
        except:
            pass

# Teacher Activity
def showClientsList():
    pass

# Prevoius class code
# Here we ended the last class
def connectToServer():
    pass


def openChatWindow():

    print("\n\t\t\t\tIP MESSENGER")

    #Client GUI starts here
    window=Tk()

    window.title('Messenger')
    window.geometry("300x300")

    global name
    global listbox
    global textarea
    global labelchat
    global text_message
    global filePathLabel

    selectlabel = Label(window, text= "select song", font = ("Calibri",10))
    selectlabel.place(x=2, y=1)

    name = Entry(window,width =30,font = ("Calibri",10))
    name.place(x=120,y=8)
    name.focus()

    # connectserver = Button(window,text="Connect to Chat Server",bd=1, font = ("Calibri",10))
    # connectserver.place(x=350,y=6)

    # separator = ttk.Separator(window, orient='horizontal')
    # separator.place(x=0, y=35, relwidth=1, height=0.1)

    labelusers = Label(window, text= "Active Users", font = ("Calibri",10))
    labelusers.place(x=10, y=50)

    listbox = Listbox(window,height = 10,width = 39,activestyle = 'dotbox', font = ("Calibri",10))
    listbox.place(x=10, y=18)

    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight = 1,relx = 1)
    scrollbar1.config(command = listbox.yview)

    # Student Activity 1
    playButton=Button(window,text="play",bd=1, font = ("Calibri",10))
    playButton.place(x=30,y=200)

    # Bolierplate Code
    Stop=Button(window,text="stop",bd=1, font = ("Calibri",10))
    Stop.place(x=200,y=200)

    # Teacher Activity
    download=Button(window,text="donwload",bd=1, font = ("Calibri",10))
    download.place(x=435,y=160)

    upload = Label(window, text= "upload", font = ("Calibri",10))
    upload.place(x=4, y=280)

    # textarea = Text(window, width = 67,height = 6,font = ("Calibri",10))
    # textarea.place(x=10,y=200)

    # scrollbar2 = Scrollbar(textarea)
    # scrollbar2.place(relheight = 1,relx = 1)
    # scrollbar2.config(command = listbox.yview)

    # attach=Button(window,text="Attach & Send",bd=1, font = ("Calibri",10))
    # attach.place(x=10,y=305)

    # text_message = Entry(window, width =43, font = ("Calibri",12))
    # text_message.pack()
    # text_message.place(x=98,y=306)

    # send=Button(window,text="Send",bd=1, font = ("Calibri",10))
    # send.place(x=450,y=305)

    # filePathLabel = Label(window, text= "",fg= "blue", font = ("Calibri",8))
    # filePathLabel.place(x=10, y=330)

    window.mainloop()


def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))


    # Boilerlate Code
    receive_thread = Thread(target=receiveMessage)               #receiving multiple messages
    receive_thread.start()

    openChatWindow()

setup()
