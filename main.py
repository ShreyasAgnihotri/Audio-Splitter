from pydub import AudioSegment
import os
import pandas as pd
cols = [1,2,3]
# col = [2]
counter = 1
flag = True 
    
def audio(t1,t2,user_input,audio_type,file_name,file_dest):                              
        global flag, counter
        if audio_type=="mp3":
            newAudio = AudioSegment.from_mp3(user_input)
        elif audio_type=="wav":
            newAudio = AudioSegment.from_wav(user_input)
        else:
            newAudio = AudioSegment.from_file(user_input,format)
        newAudio = newAudio[t1:t2]
        # file_name = input("Enter the new name for the audio file: ")
        newAudio.export(f'{file_dest}\\Q{counter}_{file_name}.'+audio_type, format=audio_type)
        counter += 1
        


def get_seconds(time):
    print('Time in hh:mm:ss:', time)
    hh, mm, ss = time.split(':')
    seconds = int(hh) * 3600 + int(mm) * 60 + int(ss) 
    return seconds * 1000



while flag:
    format = input("Enter the format of your audio file: (mp3/wav/flac) ").lower()      
    if len(format)!=0:
        user_input = input("Enter the path of your file: ")
        excel_input = input("Enter path of the Excel File: ")
        df = pd.read_excel (f'{excel_input}', usecols = cols) 
        df = df.replace('\?','',regex=True) 
        # df1 = pd.read_excel(r'timestamps.xlsx',usecols = col )
        count_row = df.shape[0]
        file_dest = input("Enter the path to where audio should be exported: ")
        for i in range(count_row):
            time1 = df.at[i,'start time']
            time2 = df.at[i,'end time']
            file_name = df.at[i,'question']
            t1 = get_seconds(str(time1))
            t2 = get_seconds(str(time2))
            assert os.path.exists(user_input), "I did not find the file at, "+str(user_input)
            audio(t1,t2,user_input,format,file_name,file_dest)
            if i + 2 > count_row:
                print("The Splitting of the current Audio File is done.")
                choice = input("Do You want to continue Splitting: (Y/N) ").lower()
                if choice == "y":
                    flag =  True
                else:
                    flag = False
                    break
            else:
                choice = input("Do You want to continue Splitting: (Y/N) ").lower()
                if choice == "y":
                    flag =  True
                else:
                    flag = False
                    break

    else:
        print("Invalid Format")
        flag = True
