from pydub import AudioSegment
import os

flag = True

counter = 0
    

def mp3(t1,t2,user_input):
        global flag,counter
        newAudio = AudioSegment.from_mp3(user_input)
        newAudio = newAudio[t1:t2]
        newAudio.export(f'newSample{counter}.mp3', format="mp3")
        counter += 1
        choice = input("Do You want to continue Splitting: (Y/N) ").lower()
        if choice == "y":
            flag = True
        else:
            flag = False

def wav(t1,t2,user_input):
        global flag, counter
        newAudio = AudioSegment.from_wav(user_input)
        newAudio = newAudio[t1:t2]
        newAudio.export(f'newSample{counter}.wav', format="wav")
        counter += 1
        choice = input("Do You want to continue Splitting: (Y/N) ").lower()
        if choice == "y":
            flag =  True
        else:
            flag = False


while flag:
    
    format = input("Enter the format of your audio file: (mp3/wav) ").lower()
    if format == "mp3":
        user_input = input("Enter the path of your file: ")
        t1 = int(input("Enter the Starting time in seconds to split: "))
        t2 = int(input("Enter the Ending time in seconds to split: "))
        t1 = t1 * 1000 
        t2 = t2 * 1000
        assert os.path.exists(user_input), "I did not find the file at, "+str(user_input)
        mp3(t1,t2,user_input)
        
    elif format == "wav":
        user_input = input("Enter the path of your file: ")
        t1 = int(input("Enter the Starting time in seconds to split: "))
        t2 = int(input("Enter the Ending time in seconds to split: "))
        t1 = t1 * 1000 
        t2 = t2 * 1000
        assert os.path.exists(user_input), "I did not find the file at, "+str(user_input)
        wav(t1,t2,user_input)
        
    else:
        print("Invalid Format")
        flag = True
