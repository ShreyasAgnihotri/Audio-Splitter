from pydub import AudioSegment
import os

flag = True #initialising flag value to True

counter = 0 #initialising counter to 0
    
def audio(t1,t2,user_input,audio_type):                              #works similarly except for that it is for the .wav format of the audio file 
        global flag, counter
        if audio_type=="mp3":
            newAudio = AudioSegment.from_mp3(user_input)
        elif audio_type=="wav":
            newAudio = AudioSegment.from_mp3(user_input)
        else:
            newAudio = AudioSegment.from_file(user_input,format)
        newAudio = newAudio[t1:t2]
        newAudio.export(f'newSample{counter}.'+audio_type, format=audio_type)
        counter += 1
        choice = input("Do You want to continue Splitting: (Y/N) ").lower()
        if choice == "y":
            flag =  True
        else:
            flag = False


while flag:
    format = input("Enter the format of your audio file: (mp3/wav/flac) ").lower()       #user input for format of the audio file
    if len(format)!=0:
        user_input = input("Enter the path of your file: ")
        t1 = int(input("Enter the Starting time in seconds to split: "))
        t2 = int(input("Enter the Ending time in seconds to split: "))
        t1 = t1 * 1000 
        t2 = t2 * 1000
        assert os.path.exists(user_input), "I did not find the file at, "+str(user_input)
        audio(t1,t2,user_input,format)                                                   #calls wav function
        
    else:
        print("Invalid Format")
        flag = True
