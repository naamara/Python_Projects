"""
*****SpeechIT.py******

PURPOSE:This program is a "text-to-speech" program designed to breach the difficulty in reading by some persons due to circumstances,thus listening has become more convenient. This program is designed to accept an input from a user and converts the input into an audio file.

INTERFACE: The output of this program will be run on an MP3 compatible application of your choice.

FUNCTIONAL REQUIREMENTS: This program uses the input method to accept a text from a user. The program will be flexible enough to accept a raw input from the user or the user can upload an already existing file from the directory same as the file in execution. The gtts module helps to convert the text file into speech .The os module helps to read it into an MP3 file.when executed,the text turns into speech and saves as an mp3 file and can be listened from  any mp3 compatible application.

TEST VALUES: the program was tested and can accept user input.

EXPECTED RESULT: The Program is expected to return a .mp3 file which can be accessed from any mp3 application.

LIMITATIONS: The gtts module for "text-to-speech" conversion requires a network connection to the internet, without internet connection the program cannot be executed.
"""

# Import the required module for text to speech conversion 

from gtts import gTTS 
  
# This module is imported so that we can play the converted audio 

import os 

# a text that will welcome the user and intoduce the program

print("Hello welcome to SpeechIT!!\n we are here to help you convert your text into speech! \n Have Fun \n")


#call for input: here the user will be asked to selct whether he wants to type in text for conversion or he wants to import text from a directory.

choice = int(input("what kind of file do you want to   convert into mp3. \n enter 1 for raw user input\n enter 2 to import a .txt file: "))


#if the user chooses 1 as an input the function will call for a raw input from the user


if choice == 1:
	my_text = input("\nplease enter your text: ")
	
	
#if the user chooses 2, the function will call for a text file to be opened from a directory (same as where the __main__ file is saved)

elif choice ==2:
	filename = input("\nplease type the name of the .txt file you will like to open:  ")


	my_text = open(filename, "r").read().replace("\n"," ").strip()
 
  			
  # if the user chooses a wrong input the program will return an error message 			
else:
  	print("\nsorry you entered a wrong input!! \n try again, \n put 1 or 2 to proceed")
  		 
  	
# prompts user for Language in which you want to convert the file into

lang_choice = int(input("\nplease enter the language for conversion\n 1 for English\n 2 for french\n 3 for spain\n 4 for china\n 5 for Portuguese: "))

if lang_choice == 1:
	language = 'en'
	
elif lang_choice == 2:
	language = 'fr'
	
elif lang_choice == 3:
	language = 'es'
	
elif lang_choice == 4:
	language = 'ln'

elif lang_choice == 5:
	language = 'pt'

else:
	print ("\nyou've entered a wrong input\n please enter number 1 to 5 to proceed")
  
# Passing the text and language to the engine, here we have marked slow=False. Which tells the module that the converted audio should have a high speed 

file_output = gTTS(text=my_text, lang=language, slow=False) 
  
# Saving the converted audio in a mp3 file. Here the user will be asked to put a convinient name so that the old file will not be overwritten by the new one.

saver = input("\nplease enter a name for your audio file: ")

file_output.save(f"{saver}.mp3") 
  
# Playing the converted file 
os.system(f"mpg321 {saver}.mp3")

#an end note
print (f"\nThanks for choosing SpeechIT \n It was my pleasure to be of help\n your '{saver}.mp3' file have been saved in the same directory as SpeechIT\n Do call back next time")
