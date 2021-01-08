#Welcome to my notepad app
import tkinter
from PIL import Image ,ImageTk
from tkinter import StringVar , IntVar , scrolledtext , END ,messagebox,filedialog

#Define window
root = tkinter.Tk()
root.title("Notepad")
root.iconbitmap('pad.ico')
root.geometry('600x600')
root.resizable(0,0)

#Define fonts and colours 
text_color = "#fffacd"
menu_color = "#dbd9db"
root_color = "#6c809a"
root.config(bg = root_color)

#Define function

def change_font(event):
    """change the given font based on drop option"""
    if font_option.get() == "none":
        my_font = (font_family.get(), font_size.get())
    else:
        my_font = (font_family.get(), font_size.get() , font_option.get())
    
    #change the font style
    input_text.config(font = my_font)



def new_note():
    """create a new note which essentially clears the screen"""
    #use a message box to ask for a new note

    question  = messagebox.askyesno("New Note" , "Soch le bsdk , delete ho jaega note to mujh se mat boliyeo baad me")
    if question == 1:
        #Scrolled widgets starting index is 1.0 not 0.
        input_text.delete("1.0" , END)


def close_note():
    """closes the note which essentially quit"""
    #Use a messagebox to ask to close
    question = messagebox.askyesno("Close Note" , "Are you sure you want to close the note")
    if question == 1:
        root.destroy()

def save_note():
    """Save the given note first three lines are saved as font-family ,font size and font option"""
    #use a file dialog to get location nd name of where /what to save thef file as
    save_name = filedialog.asksaveasfilename(initialdir = "./", title = "Save Note" , filetypes = (("Text Files" , "*.txt") ,("All Files" , "*.*") ))
    with open(save_name ,'w')as f:
        #first three lines of save file are font_family , font_size and font_option . font size must be a string not n int
        f.write(font_family.get() + "\n")
        f.write(str(font_size.get()) + "\n")
        f.write(font_option.get() + "\n")
        
        #Rewrite remaining text in the field to the file
        f.write(input_text.get("1.0" , END))


def open_note():
    """open a previous save note"""
    #use file dialog to add location and directory of fie
    open_name = filedialog.askopenfilename(initialdir = "./" , title = "Open note" , filetypes = (("Text Files" , "*.txt") ,("All Files" , "*.*") ))
    with open(open_name , 'r')as f:
        #Clear the current text
        input_text.delete("1.0" , END)

        #first three line of font family , font size and font option......yOU must strip the new line char at the end of each line
        font_family.set(f.readline().strip())
        font_size.set(int(f.readline().strip()))
        font_option.set(f.readline().strip())

        change_font(1)

        text = f.read()
        input(text.insert("1,0" , text))




#Define layout
#DEfine frames

menu_frame = tkinter.Frame(root , bg = menu_color)
text_frame = tkinter.Frame(root , bg = text_color)
menu_frame.pack(padx = 5 , pady = 5)
text_frame.pack(padx = 5 , pady = 5)


#Layout formating for menu frame

#create the menu new , open , save , close , font , font size , font option

new_Image = ImageTk.PhotoImage(Image.open('new.png'))
new_button = tkinter.Button(menu_frame , image = new_Image , command = new_note)
new_button.grid(row =0 , column = 0  ,padx = 5 , pady = 5)

open_image = ImageTk.PhotoImage(Image.open('open.png'))
open_button = tkinter.Button(menu_frame , image = open_image , command = open_note)
open_button.grid(row =0 , column = 1  ,padx = 5 , pady = 5)

save_image = ImageTk.PhotoImage(Image.open('save.png'))
save_button = tkinter.Button(menu_frame , image = save_image , command = save_note)
save_button.grid(row =0 , column = 2 ,padx = 5 , pady = 5)

close_image = ImageTk.PhotoImage(Image.open('close.png'))
close_button = tkinter.Button(menu_frame , image = close_image , command = close_note)
close_button.grid(row =0 , column = 3  ,padx = 5 , pady = 5)

#create a list of font to use

families = ['Terminal', 'Modern', 'Script', 'Courier', 'Arial', 'Calibri', 'Cambria',
'Georgia', 'MS Gothic', 'SimSun', 'Tahoma', 'Times New Roman', 'Verdana', 'Wingdings']


font_family = StringVar()
font_family_drop = tkinter.OptionMenu(menu_frame , font_family , *families , command = change_font)
font_family.set('Terminal')
font_family_drop.config(width = 16)
font_family_drop.grid(row = 0 , column = 4  ,padx =5 , pady = 5)
#set the width

size = [8, 10, 12, 14, 16, 20, 24, 32, 48, 64, 72, 96]
font_size = IntVar()
font_size_drop = tkinter.OptionMenu(menu_frame ,font_size , *size , command = change_font)
font_size.set(12)

font_size_drop.config(width = 2)
font_size_drop.grid(row = 0 , column = 5 , padx = 5 , pady =5)

option = ['none' , 'bold' , 'italic']
font_option = StringVar()
font_option_drop = tkinter.OptionMenu(menu_frame , font_option , *option , command = change_font)
font_option.set('none')
font_option_drop.config(width = 5)
font_option_drop.grid(row = 0 ,column = 6  ,padx  =5, pady = 5)

#Layout for the text frame
my_font = font_family.get() , font_size.get()

#create the input text as  yoy scroll through the text field

input_text = tkinter.scrolledtext.ScrolledText(text_frame ,width = 1000 , height = 100, bg = text_color , font = my_font)
input_text.pack()






#run the main loop

root.mainloop()

