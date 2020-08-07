#Building a music player

import os
from tkinter.filedialog import askdirectory
import pygame
from tkinter import*


root = Tk()
root.minsize(450,500) # this sets the size of the music player interface

listofsongs = []

v = StringVar()
songlabel = Label(root,textvariable = v,width = 25)

index = 0

def nextsong(event): # this enables the next button to funtion as expected when pressed
    global index
    index += 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()
    
def prevsong(event): # this enables the previous button to funtion as expected when pressed
    global index
    index -= 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()
    
def stopsong(event): #this enables the stop button to funtion as expected when pressed
    pygame.mixer.music.stop()
    v.set(" ")
    #return songname
    
def updatelabel():
    global index
    global songname
    v.set(listofsongs[index])
    return songname

def directory_chooser(): # this allows user to choose which directries to play songs from
    directory = askdirectory()
    os.chdir(directory)
    
    for files in os.listdir():
        if files.endswith(".mp3"): # this helps to pick only files with .mp3 only
            
    
            
            listofsongs.append(files)
            
    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    pygame.mixer.music.play()
    
    
directory_chooser()
    
label = Label(root,text = "Music Player")
label.pack

listbox = Listbox(root)
listbox.pack()

listofsongs.reverse()

for items in listofsongs:
    listbox.insert(0,items)

listofsongs.reverse()

nextbutton = Button(root,text = "Next Song") #creates the next button on the music playing interface
nextbutton.pack()

previousbutton = Button(root,text = "Previos Song") #creates the previous button on the music playing interface
previousbutton.pack()

stopbutton = Button(root,text = "Stop Song") #creates the stop button on the music playing interface
stopbutton.pack()
            
nextbutton.bind("<Button-1>",nextsong)
previousbutton.bind("<Button-1>",prevsong)
stopbutton.bind("<Button-1>",stopsong)

songlabel.pack()


root.mainloop()
