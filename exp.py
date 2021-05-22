from tkinter import *
from tkinter.ttk import *
import time
from tkinter import filedialog as fd


path = '/home/pramila/Desktop/cc/Major-Tasks/REMC-Pramila/electromantic'
import os
os.chdir(path)
if os.environ.get('DISPLAY','') == '':
    # print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')




ws = Tk(className="License Verification")

def quit(root):
        root.destroy()
def createNewWindow(msg="No File Selected"):
    newWindow = Toplevel(ws)
    newWindow.resizable(False, False)
    newWindow.title('Status')
    newWindow.geometry('400x110+350+250')
    if msg=="No File Selected":
        labell = Label(newWindow, text=msg, font=("Impact", 10, "italic"), foreground="black").place(x=130, y=20)
    elif msg== "You are Authenticated!":
        labell = Label(newWindow, text=msg, font=("Impact", 10, "italic"), foreground="black").place(x=95, y=20)
    elif msg == 'Not Authenticated! Upload Correct File':
        labell = Label(newWindow, text=msg, font=("Impact", 10, "italic"), foreground="black").place(x=35, y=20)
    okbtn = Button(
        newWindow, 
        text ='ok',
        command = lambda: quit(newWindow)
        ).place(x=144, y=60)





ws.resizable(False, False)
p1 = PhotoImage(file = 'licence.png')
ws.iconphoto(False, p1)
ws.title('License Verification')
ws.geometry('500x300+300+150')
bg = PhotoImage(file='background.png')
logo = PhotoImage(file='ELECTROMANTIC1.png')
cc_logo = PhotoImage(file="cc_logo.png")
bg_image = Label(ws, image=bg).place(x=0, y=0, relwidth=1, relheight=1)

s = Style()
s.configure('My.TFrame', background='white')


Frame_auth = Frame(ws, style='My.TFrame')
Frame_auth.place(x=25, y=10, height=270, width=350)
# bg_image2 = Label(Frame_auth, image=bg).place(x=0, y=0, relwidth=1, relheight=1)

   
# canvas = Canvas(Frame_auth, width = 452, height = 56)      
# canvas.pack()      
# img = PhotoImage(file="ELECTROMANTIC.png")      
# canvas.create_image(70, 30, anchor=NW, image=img)

title = Label(Frame_auth, image=logo, state="normal", foreground="white", background="blue").place(x=90, y=20)
title2 = Label(Frame_auth, text="Select Your Product Key", font=("Arial", 11), foreground="black", background="white").place(x=120, y=100)
footer =  Label(Frame_auth, image=cc_logo, state="normal", foreground="white", background="white").place(x=165, y=200)
# title2 = Label(Frame_auth, text="Upload License Text File Here", font=("Impact", 12), foreground="black").place(x=90, y=100)

flag = 0
file_path = None
counter = 0 

# message = ""
# pb1 = Label(Frame_auth, text=message, foreground='black', font=("Arial", 14))
# pb1.place(x=90, y=240)

def check_func():
    global file_path
    global counter
    if file_path is not None:
        with open (file_path) as f:
            lines = f.read().splitlines()
            counter+=1
        global flag
        if lines[0] == 'blah blah':
            flag = 1
        else:
            flag=0
    else:
        pass

def open_file():
    # global pb1
    # pb1.destroy()
    # pb1 = Label(Frame_auth, text="choosing a file..", foreground='black', background="white", font=("Arial", 11, "italic"))
    # pb1.place(x=170, y=170)
    global counter
    counter = 0
    global file_path
    file_path = fd.askopenfilename(filetypes=[('Text Files', '*.txt')])
    global flag
    if (file_path is not None) & (file_path is not ""):
        #title = Label(Frame_auth, text=file_path, font=("Impact", 5, "bold"), foreground="black").place(x=90, y=200)
        # pb1.destroy()
        # pb1 = Label(Frame_auth, text="Upload the File", foreground='black', font=("Arial", 11, "italic"))
        # pb1.place(x=170, y=170)
        flag = 0
        check_func()
        #str1 = "flag = {}".format(flag)
        #title = Label(Frame_auth, text=str1, font=("Impact", 5, "bold"), foreground="black").place(x=90, y=200)

style = Style()
 
style.configure('TButton', background='blue', foreground="white")
# style.map('TButton', foreground=[('pressed', '#9c3d54'),
#                             ('active', '#e2703a')],
#                      background = [('active', '#fffff4')])
licensebtn = Button(
    Frame_auth, 
    text ='Choose',
    command = lambda: open_file()
    )
licensebtn.place(x=100, y=140)



def uploadFiles():
    global counter
    # global pb1
    # global message
    counter+=1
    # if counter > 1:
    #     msg="No File Selected"
    #     pb1.destroy()
    #     pb1 = Label(Frame_auth, text=message, foreground='black', font=("Arial", 11, "italic"))
    #     pb1.place(x=170, y=170)
    
    # pb1.destroy()
    # pb1 = Progressbar(
    #     Frame_auth, 
    #     orient=HORIZONTAL, 
    #     length=300, 
    #     mode='determinate'
    #     )
    # pb1.place(x=170, y=170)
    # for i in range(5):
    #     ws.update_idletasks()
    #     pb1['value'] += 20
    #     time.sleep(0.1)
    # pb1.destroy()
    if (flag == 1) & (counter > 1):
        message = "You are Authenticated!"
        createNewWindow(message)
        # pb1 = Label(Frame_auth, text=message, foreground='black', font=("Arial", 11, "italic"))
        # pb1.place(x=170, y=170)
    elif (flag==0) & (counter > 1):
        message = 'Not Authenticated! Upload Correct File'
        createNewWindow(message)
        # pb1 = Label(Frame_auth, text=message, foreground='black', font=("Arial", 11, "italic"))
        # pb1.place(x=170, y=170)
    else:
        message = "No File Selected"
        createNewWindow(message)
        

  
upld = Button(
    Frame_auth, 
    text='Upload',
    command=uploadFiles
    )
upld.place(x=225, y=140)


# upld.grid(row=7, columnspan=3, pady=10)

# licensebtn.grid(row=4, column=0, pady=10, sticky=W+E)




# def func():
#     with open ('/home/pramila/Desktop/cc/Major-Tasks/REMC-Pramila/exp.txt') as f:
#         lines = f.read().splitlines()
#     global flag
#     if lines[0] == 'blah blah':
#         flag = 1

# def uploadFiles():
#     pb1 = Progressbar(
#         ws, 
#         orient=HORIZONTAL, 
#         length=300, 
#         mode='determinate'
#         )
#     pb1.grid(row=5, columnspan=3, pady=20)
#     for i in range(5):
#         ws.update_idletasks()
#         pb1['value'] += 20
#         time.sleep(1)
#     pb1.destroy()
#     if flag == 1:
#         Label(ws, text='You are Authenticated!', foreground='black', font=("Arial", 14)).grid(row=6, columnspan=3, pady=10)
#     else:
#         Label(ws, text='Not Authenticated! Upload Correct File...', foreground='black', font=("Arial", 14)).grid(row=6, columnspan=3, pady=10)

    
# licensee = Label(
#     ws, 
#     text='Welcome Admin!',
#     font=("Impact", 11)
#     )
# licensee.grid(row=0, column=0, padx=10, pady=10)

# licensee2 = Label(
#     ws, 
#     text='Upload the license text file...',
#     font=("Impact", 11)
#     )
# licensee2.grid(row=2, column=0, padx=10, pady=10)

# licensebtn = Button(
#     ws, 
#     text ='Choose File', 
#     command = lambda: open_file()
#     ) 
# licensebtn.grid(row=4, column=0, pady=10, sticky=W+E)

# func()
# upld = Button(
#     ws, 
#     text='Upload Files', 
#     command=uploadFiles
#     )
# upld.grid(row=7, columnspan=3, pady=10)



ws.mainloop()


# style = Style()
 
# style.configure('TButton', font =
#                ('Arial', 14, 'bold'),
#                     borderwidth = '4', background='#fffff4')
# style.map('TButton', foreground=[('pressed', '#9c3d54'),
#                             ('active', '#e2703a')],
#                      background = [('active', '#fffff4')])
# import os
# path_x= os.getcwd()