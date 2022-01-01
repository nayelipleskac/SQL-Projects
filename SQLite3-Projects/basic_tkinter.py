from tkinter import *
from tkinter import messagebox
root =  Tk()
root.title('Social Medias')

# def clear():
#     first_name_entry.delete(0, END)
#     last_name_entry.delete(0, END)
#     age_entry.delete(0, END)
#     grade_entry.delete(0, END)
#     city_entry.delete(0, END)

# def submit():
#     a = first_name_entry.get()
#     b = last_name_entry.get()
#     c = age_entry.get()
#     d = grade_entry.get()
#     e = city_entry.get()

#     print(a, b, c, d, e)
    
# def labelAndEntry(labelName,text):
#     labelName = Label(root, text = text)
#     labelName.pack()
#     labelName = Entry(root)
#     labelName.pack() 


# title = Label(root, text = 'Please enter the following')
# title.grid(row = 0, column = 0, columnspan = 3)

# # labelAndEntry(first_name_label,'First Name')
# # labelAndEntry('Last Name')
# # labelAndEntry('Age')
# # labelAndEntry('Grade')
# # labelAndEntry('City')
# first_name_label = Label(root, text = 'First Name')
# first_name_label.grid(row = 1, column = 1)
# first_name_entry = Entry(root)
# first_name_entry.grid(row = 1, column = 2) 

# last_name_label = Label(root, text = 'Last Name')
# last_name_label.grid(row = 2, column = 1)
# last_name_entry = Entry(root)
# last_name_entry.grid(row = 2, column = 2) 

# age_label = Label(root, text = 'Age')
# age_label.grid(row = 3, column = 1)
# age_entry = Entry(root)
# age_entry.grid(row = 3, column = 2) 

# grade_label = Label(root, text = 'Grade')
# grade_label.grid(row = 4, column = 1)
# grade_entry = Entry(root)
# grade_entry.grid(row = 4, column = 2) 

# city_label = Label(root, text = 'City')
# city_label.grid(row = 5, column = 1)
# city_entry = Entry(root)
# city_entry.grid(row = 5, column = 2) 

# # exit_button = Button(root, text = 'Exit', fg = 'red', command = exit)
# # exit_button.pack(side = LEFT)
# clear_button = Button(root, text = 'Clear', fg = 'blue', command = clear)
# clear_button.grid(row = 6, column = 1)
# submit_button = Button(root, text = 'Submit', fg = 'black', command = submit)
# submit_button.grid(row = 6, column = 2)
# root.mainloop()

#exercise 2
# a = 'white'
# b = 'black'
# for rows in range(0,9,1):
#     for columns in range(0,9,1):
#         block = Label(root, bg = a, width = 3)
#         block.grid(row = rows, column = columns)
#         a,b = b,a
# root.mainloop()

##
# platforms = {'facebook': 'np1', 'snapchat': 'np2', 'instagram': 'np3', 'twitter': 'np4'}

# def displayOnLabel(key):
#     value = key + ': ', platforms[key]
#     Textlabel['text'] = value
#     m1 = messagebox.askquestion('congratulations', 'access granted to platform')

# Textlabel = Label(root, text = '')
# Textlabel.grid(row = 3, column = 1)

# facebook_button = Button(root, text = 'facebook', bg = 'blue',  command = displayOnLabel('facebook'))
# facebook_button.grid(row = 0, column = 0, columnspan = 1)

# snap_button = Button(root, text = 'snapchat', bg = 'yellow')
# snap_button.grid(row = 0, column = 1, columnspan = 1)

# instagram_button = Button(root, text = 'instagram', bg = 'red')
# instagram_button.grid(row = 1, column = 0, columnspan = 1)

# twitter_button = Button(root, text = 'twitter', bg = 'gray')
# twitter_button.grid(row = 1, column = 1, columnspan = 1)

# root.mainloop()

## variables

# name = StringVar()
# name_value = name.get()
# name.set('nayeli')

import random


def generateNum(num1, num2):
    start = num1
    end = num2
    generate_result = StringVar()
    # generate_result = random.randint(start, end)
    print(generate_result)

    result = StringVar()
    result.set(generate_result)
    result_label= Label(root, textvariable = result, bg = 'yellow')
    result_label.grid(row = 2, column = 2)
   

label = Label(root, text= 'Give me a range: ex: start-end')
label.grid(row = 1, column = 1)
label_entry = Entry(root)
label_entry.grid(row = 1, column = 2)
generate_button = Button(root, text= 'Generate', command = generateNum(10, 20))
generate_button.grid(row = 3, column = 2)



root.mainloop()