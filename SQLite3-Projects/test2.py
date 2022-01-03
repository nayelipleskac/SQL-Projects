# from tkinter import *
  
# root = Tk()
# root.geometry("300x300")
# root.title(" Q&A ")
  
# def Take_input():
#     INPUT = inputtxt.get("1.0", "end-1c")
#     print(INPUT)
#     if(INPUT == "120"):
#         Output.insert(END, 'Correct')
#     else:
#         Output.insert(END, "Wrong answer")
      
# l = Label(text = "What is 24 * 5 ? ")
# inputtxt = Text(root, height = 10,
#                 width = 25,
#                 bg = "light yellow")
  
# Output = Text(root, height = 5, 
#               width = 25, 
#               bg = "light cyan")
  
# Display = Button(root, height = 2,
#                  width = 20, 
#                  text ="Show",
#                  command = lambda:Take_input())
  
# l.pack()
# inputtxt.pack()
# Display.pack()
# Output.pack()
  
# mainloop()

import tkinter as tk
root = tk.Tk()
root.geometry("400x240")

def getTextInput():
    result=textExample.get("1.0",tk.END)
    print(result)

textExample=tk.Text(root, height=10)
textExample.pack()
btnRead=tk.Button(root, height=1, width=10, text="Read", 
                    command=getTextInput)

btnRead.pack()

root.mainloop()
