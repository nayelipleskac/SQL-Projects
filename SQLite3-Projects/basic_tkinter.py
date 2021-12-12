from tkinter import *
root =  Tk()
root.title('Hello world')

def clear():
    name_entry.delete(0, END)
def submit():
    a = name_entry.get()
    print(a)
    
def labelAndEntry(labelName,text):
    labelName = Label(root, text = text)
    labelName.pack()
    labelName = Entry(root)
    labelName.pack() 


top_label = Label(root, text = 'Please enter the following')
top_label.pack()

# labelAndEntry(first_name_label,'First Name')
# labelAndEntry('Last Name')
# labelAndEntry('Age')
# labelAndEntry('Grade')
# labelAndEntry('City')
first_name_label = Label(root, text = 'First Name')
first_name_label.pack()
first_name_entry = Entry(root)
first_name_entry.pack() 

name_label = Label(root, text = 'Last Name')
name_label.pack()
name_entry = Entry(root)
name_entry.pack() 

age_label = Label(root, text = 'Age')
age_label.pack()
age_entry = Entry(root)
age_entry.pack() 

grade_label = Label(root, text = 'Grade')
grade_label.pack()
grade_entry = Entry(root)
grade_entry.pack() 

city_label = Label(root, text = 'City')
city_label.pack()
city_entry = Entry(root)
city_entry.pack() 

# exit_button = Button(root, text = 'Exit', fg = 'red', command = exit)
# exit_button.pack(side = LEFT)
clear_button = Button(root, text = 'Clear', fg = 'blue', command = clear)
clear_button.pack(side = RIGHT)
submit_button = Button(root, text = 'Submit', fg = 'black', command = submit)
submit_button.pack(side = LEFT)
root.mainloop()
