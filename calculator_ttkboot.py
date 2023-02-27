
# main model code 
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window(themename='superhero')
root.title('soham\'s calculator')
root.iconbitmap("D:\mycode\images\cal.ico")
root.resizable(False,False)

# style widget
mystyle = ttk.Style()
mystyle.configure('success.Outline.TButton',font=('Helvetica',25))

# functions 
eqution =''

# this display the enterd int on screen
def cal(num):
    global eqution
    eqution += str(num)
    var.set(eqution)

# this calculate the eqution
def total():
    # error comes it display the except message
    try:
        global eqution
        result = str(eval(eqution))
        var.set(result)
        eqution=''
    except:
        var.set('ERROR')
        eqution=''

# this clear the screen 
def clear():
    global eqution
    eqution=''
    var.set(eqution)
    
# entry widget
var = ttk.StringVar()
ebox = ttk.Entry(root,bootstyle='success',width=16,font=('Helvetica',30),textvariable=var)
ebox.grid(row=0,column=1,columnspan=5,pady=10)

# buttons
bt1 =ttk.Button(root,text='7',bootstyle='success',width=4,style='success.Outline.TButton',command=lambda : cal('7'))
bt2 =ttk.Button(root,text='8',bootstyle='success',width=4,style='success.Outline.TButton',command=lambda : cal('8'))
bt3 =ttk.Button(root,text='9',bootstyle='success',width=4,style='success.Outline.TButton',command=lambda : cal('9'))
bt4 =ttk.Button(root,text='/',bootstyle='success',width=4,style='success.Outline.TButton',command=lambda : cal('/'))
bt5 =ttk.Button(root,text='4',bootstyle='success',width=4,style='success.Outline.TButton',command=lambda : cal('4'))
bt6 =ttk.Button(root,text='5',bootstyle='success',width=4,style='success.Outline.TButton',command=lambda : cal('5'))
bt7 =ttk.Button(root,text='6',bootstyle='success',width=4,style='success.Outline.TButton',command=lambda : cal('6'))
bt8 =ttk.Button(root,text='x',bootstyle='success',width=4,style='success.Outline.TButton',command=lambda : cal('*'))
bt9 =ttk.Button(root,text='1',bootstyle='success',width=4,style='success.Outline.TButton',command=lambda : cal('1'))
bt10 =ttk.Button(root,text='2',bootstyle='success',width=4,style='success.Outline.TButton',command=lambda : cal('2'))
bt11=ttk.Button(root,text='3',bootstyle='success',width=4,style='success.Outline.TButton',command=lambda : cal('3'))
bt12=ttk.Button(root,text='-',bootstyle='success',width=4,style='success.Outline.TButton',command=lambda : cal('-'))
bt13=ttk.Button(root,text='c',bootstyle='success',width=4,style='success.Outline.TButton',command=clear)
bt14=ttk.Button(root,text='0',bootstyle='success',width=4,style='success.Outline.TButton',command=lambda : cal('0'))
bt15=ttk.Button(root,text='+',bootstyle='success',width=4,style='success.Outline.TButton',command=lambda : cal('+'))
bt16=ttk.Button(root,text='=',bootstyle='success',width=4,style='success.Outline.TButton',command=total)

bt1.grid(row=1,column=1,padx=2,pady=(5,2))
bt2.grid(row=1,column=2,padx=2,pady=(5,2))
bt3.grid(row=1,column=3,padx=2,pady=(5,2))
bt4.grid(row=1,column=4,padx=2,pady=(5,2))
bt5.grid(row=2,column=1,padx=2,pady=2)
bt6.grid(row=2,column=2,padx=2,pady=2)
bt7.grid(row=2,column=3,padx=2,pady=2)
bt8.grid(row=2,column=4,padx=2,pady=2)
bt9.grid(row=3,column=1,padx=2,pady=2)
bt10.grid(row=3,column=2,padx=2,pady=2)
bt11.grid(row=3,column=3,padx=2,pady=2)
bt12.grid(row=3,column=4,padx=2,pady=2)
bt13.grid(row=4,column=1,padx=2,pady=2)
bt14.grid(row=4,column=2,padx=2,pady=2)
bt15.grid(row=4,column=3,padx=2,pady=2)
bt16.grid(row=4,column=4,padx=2,pady=2)

root.mainloop()