from tkinter import *

window = Tk()
# You can add your widgets here
trackframe = LabelFrame(window,text="                                                                      Tweet Streak",font=("times new roman",15,"bold"),bg="#1DA1F2",fg="white",bd=0,relief=GROOVE,)
trackframe.place(x=0,y=0,width=800,height=30)
playbtn = Button(trackframe,text="PLAYSONG",width=10,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="pink").grid(row=0,column=0,padx=10,pady=5)



window.title('Hello StudyTonight')
window.geometry("800x500+400+120")
window.mainloop()