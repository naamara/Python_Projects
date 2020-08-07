from gtts import gTTS
'''This program allows a User to iput a text, and the text is converted to a Speech'''
import os
text = input('Enter the text you wish to Convert to Speech-->  ') #Allows a User to input a desired text to convert to Speech
language = 'en' #Sets th Language to English
convert = gTTS(text=text,lang=language,slow=False)
convert.save('User_text_to_Speech.mp3') #Saves the converted text to a directory
os.system('Start User_text_to_Speech.mp3') #Plays the converted text
