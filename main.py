from tkinter import *
from tkinter.ttk import *
  
root = Tk()
root.geometry("800x500")
   
w = Label(root, text ='GeeksForGeeks',
          font = "50") 

photo1 = PhotoImage(file = r".\images\twitter.png")
photo2 = PhotoImage(file = r".\images\dead-removebg-preview.png") 
# Resizing image to fit on button
photoimage1 = photo1.subsample(20,20)
photoimage2 = photo2.subsample(15,15)
Button(root, text = 'Click Me !', image = photoimage1,
                    compound = LEFT).pack(side = RIGHT)
Button(root, text = 'Click Me not !', image = photoimage2,
                    compound = LEFT).pack(side = RIGHT)
   
w.pack()
   

   
root.mainloop()