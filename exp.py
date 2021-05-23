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
width = ws.winfo_screenwidth()
height = ws.winfo_screenheight()
res_x = 500 
res_y = 300
start = int((width/2) - (res_x/2))
end = int((height/2) - (res_y/2))
# '500x300+300+150'
electromantic_window_dim = str(res_x) + "x" + str(res_y) + "+" + str(start) + "+" + str(end)

def quit(root):
        root.destroy()
def createNewWindow(msg="No File Selected"):
    newWindow = Toplevel(ws)
    newWindow.resizable(False, False)
    global width
    global height
    global bg
    global start, res_x, end
    bg_image = Label(newWindow, image=bg).place(x=0, y=0, relwidth=1, relheight=1)
    new_window_w = 400
    new_window_h = 110
    start_n = int((start) + (res_x/2) - (new_window_w/2))
    end_n = int(end + (res_y/2) - (new_window_h/2))
    newwindow_dim = str(new_window_w) + "x" + str(new_window_h) + "+" + str(start_n) + "+" + str(end_n)
    newWindow.geometry(newwindow_dim)
    s = Style()
    s.configure('My.TFrame', background='white')
    Frame_2 = Frame(newWindow, style='My.TFrame')
    frame_2x = 5
    frame_2y = 10
    frame2_width = (new_window_w-20)
    frame2_height = (new_window_h-20)
    Frame_2.place(x=frame_2x, y=frame_2y, height=frame2_height, width=frame2_width)
    statimage_x = int((frame2_width/2)-(351/2))
    statimage_y = frame_2y 
    global na
    global a
    global ns
    if msg=="No File Selected":
        labell = Label(Frame_2, image=ns, state="normal", foreground="white", background="white").place(x=statimage_x, y=statimage_y)
    elif msg== "You are Authenticated!":
        labell = Label(Frame_2, image=a, state="normal", foreground="white", background="white").place(x=statimage_x, y=statimage_y)
    elif msg == 'Not Authenticated! Upload Correct File':
        labell = Label(Frame_2, image=na, state="normal", foreground="white", background="white").place(x=statimage_x, y=statimage_y)
    global button_width
    okbtn = Button(Frame_2, text ='OK',command = lambda: quit(newWindow)).place(x=int((frame2_width/2)-(button_width-20)/2), y=60, width=button_width-20, height=30)




ws.resizable(False, False)
p1 = PhotoImage(file = 'licence.png')
ws.iconphoto(False, p1)
ws.title('License Verification')
ws.geometry(electromantic_window_dim)
bg = PhotoImage(file='background.png')
logo = PhotoImage(file='ELECTROMANTIC1.png')
do_this = PhotoImage(file='Upload Your Product Key.png')
cc_logo = PhotoImage(file="cc_logo.png")
a = PhotoImage(file="You_are_authenticated.png")
na = PhotoImage(file="Not_Autheticated.png")
ns = PhotoImage(file="No File Selected.png")
bg_image = Label(ws, image=bg).place(x=0, y=0, relwidth=1, relheight=1)

s = Style()
s.configure('My.TFrame', background='white')


Frame_auth = Frame(ws, style='My.TFrame')
frame_x = 10
frame_y = 10
frame_width = (res_x-20)
frame_height = (res_y-20)

Frame_auth.place(x=frame_x, y=frame_y, height=frame_height, width=frame_width)
# bg_image2 = Label(Frame_auth, image=bg).place(x=0, y=0, relwidth=1, relheight=1)

   
# canvas = Canvas(Frame_auth, width = 452, height = 56)      
# canvas.pack()      
# img = PhotoImage(file="ELECTROMANTIC.png")      
# canvas.create_image(70, 30, anchor=NW, image=img)

image_x = int(frame_width/2 - 254/2)
image_y = int(frame_y + 10)

cc_logo_x = int(frame_width/2 - 102/2)
cc_logo_y = (frame_y + frame_height - 56 -10)

# text_width = 19.5*font_size
# text_x = int(frame_width/2 - text_width/2)
# text_y = int(image_y + 49+  20)

do_x = int(frame_width/2 - 203/2)
do_y = int(image_y + 49+  20)
title = Label(Frame_auth, image=logo, state="normal", foreground="white", background="black").place(x=image_x, y=image_y)
title2 = Label(Frame_auth, image=do_this, state="normal", foreground="white", background="white").place(x=do_x, y=do_y)
footer =  Label(Frame_auth, image=cc_logo, state="normal", foreground="white", background="white").place(x=cc_logo_x, y=cc_logo_y)
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
    global flag2
    if file_path is not None:
        with open (file_path) as f:
            lines = f.read().splitlines()
            counter+=1
            flag2='yes'
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
 
style.configure('TButton', background='white', foreground="black")
# style.map('TButton', foreground=[('pressed', '#9c3d54'),
#                             ('active', '#e2703a')],
#                      background = [('active', '#fffff4')])
dis=120
button_width = 100
licensebtn = Button(Frame_auth, 
    text ='Choose',
    command = lambda: open_file()
    )
licensebtn.place(x=frame_x+dis, y=140, width=button_width)

flag2="no"

def uploadFiles():
    global flag2
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
    if (flag == 1) & (counter > 1) & (flag2=='yes'):
        message = "You are Authenticated!"
        createNewWindow(message)
        # pb1 = Label(Frame_auth, text=message, foreground='black', font=("Arial", 11, "italic"))
        # pb1.place(x=170, y=170)
    elif (flag==0) & (counter > 1)& (flag2=='yes'):
        message = 'Not Authenticated! Upload Correct File'
        createNewWindow(message)
        # pb1 = Label(Frame_auth, text=message, foreground='black', font=("Arial", 11, "italic"))
        # pb1.place(x=170, y=170)
    else:
        message = "No File Selected"
        createNewWindow(message)
    
    flag2 = "no"
        

  
upld = Button(
    Frame_auth, 
    text='Upload',
    command=uploadFiles
    )
upld.place(x=(frame_x+frame_width-dis-button_width-20), y=140, width=button_width)


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