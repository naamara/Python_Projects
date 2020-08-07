#PROJECT BRIEF 'READ CAREFULLY'
# A MUSIC PLAYER THAT PROMPT USER TO SELECT A MUSIC FOLDER ON THE PC DIRECTORY
# ALSO ENABLE USER TO ADD A MUSIC FILE TO THE ALREADY PLAYING PLAYLIST
# ENALBLE USER TO PLAY, STOP, PAUSE AND PAUSE CURRENTLY PLAYING MUSIC
# ALLOW USER TO SET VOLUME
# PROJECT BY AKINNAYAJO AKINTAYO(SNP_201027)



from tkinter import filedialog
import tkinter as tkr
import pygame
import os
import pathlib

# music window
player = tkr.Tk()
player.title("Music Player")
player.minsize(width=300,height=300)
try: #should incase you dont the icon on Your PC
    player.iconbitmap("C:/Users/User/Desktop/jpg/music logo.ico")
except:
    pass

#SONGLIST
SongList = []
#index = 0

#choose directory
directory= filedialog.askdirectory()
os.chdir(directory)
for files in os.listdir(directory):
    index = 0
    if files.endswith(".mp3"):
        SongList.append(files)

        print(files)

#OPEN FUCTION
def Open():
    file = filedialog.askopenfilename(initialdir="/", title="Open A File", filetype=(("mp3", "*.mp3"), ("All Files", "*.*")))
    Music_list.insert(index+1, file)

    print(file)

#BROWSE A MUSIC
OpenFile = tkr.LabelFrame(player, text= "Open A File")
OpenFile.pack()
OpenFileButton= tkr.Button(OpenFile, text="Browse Files",command = Open)


#pygame init
pygame.init()
pygame.mixer.init()

def PlayMusic():
    pygame.mixer.music.load(Music_list.get(tkr.ACTIVE))
    pygame.mixer.music.play()
    v.set(Music_list.get(tkr.ACTIVE))
    pygame.mixer.music.set_volume(VolumeLevel.get())
    pygame.mixer.music.set_volume(60)
    #print(VolumeLevel.get())

def PauseMusic():
    pygame.mixer.music.pause()

def Unpause():
    pygame.mixer.music.unpause()

def StopMusic():
    pygame.mixer.music.stop()

def Exit_player():
    pygame.mixer.music.stop()

def Volume():
    pygame.mixer.music.set_volume()
    pygame.mixer.music.get_volume()




Music_Player = tkr.Label(player, text="Music Playlist")
Music_Player.pack()

v = tkr.StringVar()
MusicTitle= tkr.Label(player, textvariable=v)

Music_list = tkr.Listbox(player, highlightcolor="blue", selectmode=tkr.SINGLE)
Music_list.pack()
for items in SongList:
    index=0
    Music_list.insert(0, items)
    index+=1



#Buttons
PlayButton = tkr.Button(player,text= "Play Music", command= PlayMusic)
PauseButton = tkr.Button(player, text= "Pause Music", command= PauseMusic)
StopButton = tkr.Button(player, text= "Stop Music", command= StopMusic)
UnpauseButton = tkr.Button(player,text = "Unpause Music", command=Unpause)

#volume input
VolumeLevel = tkr.Scale(player, from_=0.0, to_=100.0,
                                             orient = tkr.HORIZONTAL, resolution = 1.0)
#Apply Widget
OpenFileButton.pack()
Music_Player.pack()
Music_list.pack()
MusicTitle.pack()
PlayButton.pack()
PauseButton.pack()
UnpauseButton.pack()
StopButton.pack()
VolumeLevel.pack()
#MusicPlayer.pack()



player.mainloop()