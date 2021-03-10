import tkinter as tk
from tkinter import *
from tkinter import ttk  
from automailer import *
from NEW_RADAR import *

def sel1():
    
    selection = "You selected Python as a course "

    btn1 = Button(root, text = 'Send Mail to Students !', bd = '5',command =send_mail_student  )
    btn1.pack(side = 'top',ipadx =5 , ipady =5 , padx =5 , pady =5)

    btn2 = Button(root, text = 'Send Mail to Faculty !', bd = '5', command =send_data_to_teacher )
    btn2.pack(side = 'top',ipadx =5 , ipady =5 , padx =5 , pady =5)    
    label.config(text = selection)
 

