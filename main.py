from pydub import AudioSegment
import os

flag = True #initialising flag value to True

counter = 0 #initialising counter to 0
    

def mp3(t1,t2,user_input):                                  #function for spliiting audio file which is in mp3 format
        global flag,counter
        newAudio = AudioSegment.from_mp3(user_input)        #AudioSegment is a class in pydub library which imports the audio file from given path
        newAudio = newAudio[t1:t2]                          #splits the audio in the given start and end points
        newAudio.export(f'newSample{counter}.mp3', format="mp3")  #exports the new splitted audio file with name newsample
        counter += 1                                        #increments counter after each iteration. for eg: file name after 2 iterations would be newSample0,newSample1 etc where 0,1 are counters
        choice = input("Do You want to continue Splitting: (Y/N) ").lower()     #user input for continuation of splitting
        if choice == "y":
            flag = True                                     #stays in the while loop if splitting needs to be continued
        else:
            flag = False                                    #comes out of the while loop and exits the program

def wav(t1,t2,user_input):                              #works similarly except for that it is for the .wav format of the audio file 
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
    
    format = input("Enter the format of your audio file: (mp3/wav) ").lower()       #user input for format of the audio file
    if format == "mp3":
        user_input = input("Enter the path of your file: ")                         #user input for entering the destination of the audio file
        t1 = int(input("Enter the Starting time in seconds to split: "))            #user input for starting time of the split in seconds
        t2 = int(input("Enter the Ending time in seconds to split: "))              #user input for ending time of the split in seconds
        t1 = t1 * 1000                                                              #converting the start time to milliseconds
        t2 = t2 * 1000                                                              #converting the start time to milliseconds
        assert os.path.exists(user_input), "I did not find the file at, "+str(user_input)  #checks if the path exists, if not returns false with the written statement
        mp3(t1,t2,user_input)                                                       #calls mp3 function       
        
    elif format == "wav":
        user_input = input("Enter the path of your file: ")
        t1 = int(input("Enter the Starting time in seconds to split: "))
        t2 = int(input("Enter the Ending time in seconds to split: "))
        t1 = t1 * 1000 
        t2 = t2 * 1000
        assert os.path.exists(user_input), "I did not find the file at, "+str(user_input)
        wav(t1,t2,user_input)                                                   #calls wav function
        
    else:
        print("Invalid Format")
        flag = True
