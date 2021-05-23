from tkinter import *
from tkinter import filedialog
import tkinter.messagebox
import os
from pygame import mixer

root = Tk()

mixer.init()  # initialize the music

root.title("Melody")
# change the icon
#root.iconbitmap("music player.ico")

root.geometry("800x800")


def browse_file():
    global filename
    filename = filedialog.askopenfilename()
    print(filename)
    statusbar["text"] = "Browsing the file"


def About_us_massagebox():
    tkinter.messagebox.showinfo(
        "About Melody", "Melody is a simple music player developed by Kalindu Thathsara")
    statusbar["text"] = "Showing a message"


def help_massagebox():
    tkinter.messagebox.showinfo(
        "Help", "Please click on the \"file\" tab. Then click on open cascade. After that select a song that you want and click on the play button")


the_super_frame = Frame(root)
the_super_frame.pack(padx='200', pady='100')

menubar = Menu(root)
root.config(menu=menubar)
submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=submenu)
submenu.add_command(label="Open", command=browse_file)
submenu.add_command(label="Exit", command=root.destroy)

submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=submenu)
submenu.add_command(label="Help", command=help_massagebox)
submenu.add_command(label="About Us", command=About_us_massagebox)

label = Label(the_super_frame, text="Melody", font="10")
label.pack(pady="15")

length_frame = Frame(the_super_frame)
length_frame.pack(pady="10")

the_frame = Frame(the_super_frame, relief=RAISED)
the_frame.pack()


def play_music():
    global paused

    if paused:
        mixer.music.unpause()
        statusbar["text"] = "Music resumed"
        paused = FALSE
    else:
        try:
            mixer.music.load(filename)
            mixer.music.play()
            statusbar["text"] = "Music is playing  :-  " + \
                " " + os.path.basename(filename)
            label1 = Label(length_frame, text="File length :- 00:00")
            label1.grid(row=2, column=2)

        except:
            tkinter.messagebox.showerror("Melody could not find the file",
                                         "Melody could not find the file.Please check again")


def stop_music():
    mixer.music.stop()
    statusbar["text"] = "Music is stooped"


paused = FALSE


def pause_music():
    global paused
    paused = TRUE
    mixer.music.pause()
    statusbar["text"] = "Music is paused"


def set_volium(val):
    volium = float(val) / 100
    mixer.music.set_volume(volium)


muted = FALSE


def mute_music():
    global muted
    if muted:
        mixer.music.set_volume(45)
        volium_button.config(image=volium_photo)
        scale.set(45)
        muted = FALSE

    else:
        mixer.music.set_volume(0)
        volium_button.config(image=mute_photo)
        scale.set(0)
        muted = TRUE


def rewind_music():
    try:
        mixer.music.play()
        statusbar["text"] = "Rewinding Music"
    except:
        tkinter.messagebox.showerror("Please select a file to play",
                                     "Melody you have not selected a file to play. Please select a file")


photo = PhotoImage(file='play.png')
play_button = Button(the_frame, image=photo, command=play_music, bg="orange")
play_button.grid(row=0, column=0, padx='10')

photo2 = PhotoImage(file='stop.png')
stop_button = Button(the_frame, image=photo2, command=stop_music, bg="orange")
stop_button.grid(row=0, column=1, padx='10')

photo3 = PhotoImage(file='pause.png')
pause_button = Button(the_frame, image=photo3,
                      command=pause_music, bg="orange")
pause_button.grid(row=0, column=2, padx='10')

the_bottom_frame = Frame(root, relief=RAISED)
the_bottom_frame.pack(pady='50')

rewind_photo = PhotoImage(file='rewind-2.png')
rewind_button = Button(
    the_bottom_frame, image=rewind_photo, command=rewind_music)
rewind_button.grid(row=2, column=0)

mute_photo = PhotoImage(file='001-mute.png')
volium_photo = PhotoImage(file='002-volume.png')
volium_button = Button(
    the_bottom_frame, image=volium_photo, command=mute_music)
volium_button.grid(row=2, column=1, padx='10')

scale = Scale(the_bottom_frame, to=100, command=set_volium, orient=HORIZONTAL)
scale.set(45)
scale.grid(row=2, column=2, padx='10')

statusbar = Label(root, text="Welcome to Melody", relief=SUNKEN, anchor=SW)
statusbar.pack(side=BOTTOM, fill=X)


root.mainloop()
