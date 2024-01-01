import tkinter as tk

root = tk.Tk()
root.geometry("300x230")
calculation = ""

def addToCalculation(symbol):
    global calculation
    calculation += str(symbol)
    textResult.delete(1.0, "end")
    textResult.insert(1.0, calculation)

def clearInputs():
    global calculation
    calculation = ""
    textResult.delete(1.0, "end")

def evaluateCalculation():
    global calculation
    try:
        result = str(eval(calculation))
        calculation = result
        textResult.delete(1.0, "end")
        textResult.insert(1.0, calculation)
    except Exception as e:
        clearInputs()
        textResult.delete(1.0, "end")
        textResult.insert(1.0, "Error")

textResult = tk.Text(root, height=2, width=16, font=("Arial", 24))
textResult.grid(columnspan=4)

# Rest of your code for buttons...
button1=tk.Button(root,text="1",command=lambda:addToCalculation(1),width=5,bg="cadetblue1")
button1.grid(row=2,column=0)
button2=tk.Button(root,text="2",command=lambda:addToCalculation(2),width=5,bg="bisque1")
button2.grid(row=2,column=1)
button3=tk.Button(root,text="3",command=lambda:addToCalculation(3),width=5,bg="hotpink3")
button3.grid(row=2,column=2)
button4=tk.Button(root,text="4",command=lambda:addToCalculation(4),width=5,bg="cadetblue1")
button4.grid(row=3,column=0)
button5=tk.Button(root,text="5",command=lambda:addToCalculation(5),width=5,bg="bisque1")
button5.grid(row=3,column=1)
button6=tk.Button(root,text="6",command=lambda:addToCalculation(6),width=5,bg="hotpink3")
button6.grid(row=3,column=2)
button7=tk.Button(root,text="7",command=lambda:addToCalculation(7),width=5,bg="cadetblue1")
button7.grid(row=4,column=0)
button8=tk.Button(root,text="8",command=lambda:addToCalculation(8),width=5,bg="bisque1")
button8.grid(row=4,column=1)
button9=tk.Button(root,text="9",command=lambda:addToCalculation(9),width=5,bg="hotpink3")
button9.grid(row=4,column=2)
button0=tk.Button(root,text="0",command=lambda:addToCalculation(0),width=5,bg="bisque1")
button0.grid(row=5,column=1)
buttonbracOpen=tk.Button(root,text="(",command=lambda:addToCalculation("("),width=5,bg="bisque1")
buttonbracOpen.grid(row=5,column=0)
buttonbracClose=tk.Button(root,text=")",command=lambda:addToCalculation(")"),width=5,bg="bisque1")
buttonbracClose.grid(row=5,column=2)

buttonPlus=tk.Button(root,text="+",command=lambda:addToCalculation("+"),width=5,bg="yellow")
buttonPlus.grid(row=2,column=3)
buttonMinus=tk.Button(root,text="-",command=lambda:addToCalculation("-"),width=5,bg="yellow")
buttonMinus.grid(row=3,column=3)
buttonInto=tk.Button(root,text="*",command=lambda:addToCalculation("*"),width=5,bg="yellow")
buttonInto.grid(row=4,column=3)
buttonDivision=tk.Button(root,text="/",command=lambda:addToCalculation("/"),width=5,bg="yellow")
buttonDivision.grid(row=5,column=3)
buttonEqual = tk.Button(root, text="=", command=evaluateCalculation, width=14, bg="Green")
buttonEqual.grid(row=8, column=2, columnspan=2)

buttonClear = tk.Button(root, text="C", command=clearInputs, width=14, bg="red")
buttonClear.grid(row=8, column=0, columnspan=2)

root.mainloop()
