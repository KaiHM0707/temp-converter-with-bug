from tkinter import *

def convert():
    temp_cel = Cel_input.get()
    if temp_cel.replace(".", "", 1).isdigit():
        temp_fare = (float(temp_cel) * 9/5) + 32
        answer.config(text="Celsius to Fahrenheit: "+ str(temp_fare))
    else:
        error.place(x=150,y=300)





a = Tk()
a.title("Celsius converter")
a.geometry("500x500")
a.configure(background="gray")



Head = Label(a, text="Celsius to Fahrenheit", bg="gray", font=15)
Head.pack(side=TOP)

input_result = Label(a, text="Tempature you want to convert:", bg="gray").place(x=20, y=150)
Cel_input = Entry(a, width=30).place(x=200,y=150)

error = Label(a, text="that input was invalid", fg="red", bg="gray")#.place(x=150,y=300)
answer = Label(a, text="Tempature in Fahrenheit =         ", width=40, height=2, bg="gray").place(x=50,y=250)

conversion = Button(a,text="Convert tempatures", bg="lightgreen", width=40, height=3, command=convert).place(x=100,y=380)


a.mainloop()




























