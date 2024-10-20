from tkinter import*
root =  Tk()
root.title("pookie")
root.geometry("550x450")
root.resizable(False, False)
root.config(bg="pink")

frame = LabelFrame(root, padx= 130, pady= 50, borderwidth= 8, relief= "sunken")
frame.config(bg="Beige")
frame.grid(row = 0, column= 1, padx= 55, pady= 10)

text_label = Label(frame, text="AI Desktop Assistant :)", font=("times new roman", 12, "bold", "italic"), bg="beige")
text_label.grid(row = 0, column = 0, padx = 10, pady = 10)

text= Text(root, font=('candara 10 bold italic'), bg="beige")
text.grid(row=2, column=0)
text.place(x = 100, y = 200, width=375, height=100)

entry= Entry(root, justify=CENTER, bg="beige")
entry.place(x = 135, y = 325, width = 300, height = 45)





root.mainloop()