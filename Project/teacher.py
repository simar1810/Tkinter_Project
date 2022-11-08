from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox



class Login:
    def __init__(self,root):
        self.root=root
        
        #basic window
        self.root.title("HOME")
        self.root.geometry("1520x900+0+0")
        
        #Background Image

        self.bg = ImageTk.PhotoImage(file="Images/bg.png")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

       

        

        #Regd Frame
        frame1=Frame(self.root,bg="white")
        frame1.place(x=400,y=100,width=700,height=500)

        #Elements in frame
        title=Label(frame1,text="Teacher's Pannel" , font=("time new roman",20,"bold"),bg= "white" ,fg ="green").place(x=260,y=30)

        admin=Button(frame1,text ="Class-IX",font=("time new roman",20),bd=0,cursor="hand2",command=self.class9).place(x=50,y=150)
        teacher=Button(frame1,text ="Class-X",font=("time new roman",20),bd=0,cursor="hand2",command=self.class10).place(x=220,y=150)
        student=Button(frame1,text ="Class-XI",font=("time new roman",20),bd=0,cursor="hand2",command=self.class11).place(x=400,y=150)
        student=Button(frame1,text ="Class-XII",font=("time new roman",20),bd=0,cursor="hand2",command=self.class12).place(x=550,y=150)

       
    def class9(self):
        print("This is 9")
    def class10(self):
        print("This is 10")
    def class11(self):
        print("This is 11")
    def class12(self):
        print("This is 12")
 

root=Tk()

obj=Login(root)

root.mainloop()
