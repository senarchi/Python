# import os



# if __name__ == '__main__':
#     print("Welcome to my World!!")
#     speak = input("Enter what you want to speak: ")
#     command=speak
#     print(command)
#     os.system(command)

import pyttsx3


# if __name___ == '__main__':
text_to_speech = pyttsx3.init()
while(True):
        word = input("Enter your command: ")
        if word == 'q':
            break
        text_to_speech.say(word)
        text_to_speech.runAndWait()