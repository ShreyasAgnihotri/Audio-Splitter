from pydub import AudioSegment
import os
import pandas as pd
import ffmpeg_handler as fh
from PIL import Image, ImageFont, ImageDraw
import textwrap

fh.check()


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
        # print(os.path.isdir(file_dest))
        if os.path.isdir(file_dest):
            newAudio.export(f'{file_dest}\\Q{counter}_{file_name}.'+audio_type, format=audio_type)
        else:
            os.makedirs(file_dest, exist_ok=False)
            newAudio.export(f'{file_dest}\\Q{counter}_{file_name}.'+audio_type, format=audio_type)
        counter += 1
        


def get_seconds(time):
    print('Time in hh:mm:ss:', time)
    hh, mm, ss = time.split(':')
    seconds = int(hh) * 3600 + int(mm) * 60 + int(ss) 
    return seconds * 1000



def draw_multiple_line_text(image, text, font, text_color, text_start_height):
    draw = ImageDraw.Draw(image)
    image_width, image_height = image.size
    y_text = text_start_height
    lines = textwrap.wrap(text, width=40)
    for line in lines:
        line_width, line_height = font.getsize(line)
        draw.text(((image_width - line_width) / 2, y_text), 
                  line, font=font, fill=text_color)
        y_text += line_height



def image(img_path,image_dest,file_name):
    my_image = Image.open(img_path)
    text_start_height = 1750
    myFont = ImageFont.truetype('C:/Windows/Fonts/LCALLIG.ttf', 65)
    draw_multiple_line_text(my_image, f"{file_name}?", myFont, (0,0,0), text_start_height)
    if os.path.isdir(image_dest):
        my_image.save(f"{image_dest}\\Q_{i+1}{file_name}.jpg")
    else:
        os.makedirs(image_dest, exist_ok=False)
        my_image.save(f"{image_dest}\\Q_{i+1}{file_name}.jpg")



while flag:
    format = input("Enter the format of your audio file: (mp3/wav/flac) ").lower()      
    if len(format)!=0:
        user_input = input("Enter the path of your file: ")
        excel_input = input("Enter path of the Excel File: ")
        img_path = input("Enter Path of the Image Template: ")
        df = pd.read_excel (f'{excel_input}', usecols = cols) 
        df = df.replace('\?','',regex=True) 
        temp = df.columns.values.tolist()
        # df1 = pd.read_excel(r'timestamps.xlsx',usecols = col )
        count_row = df.shape[0]
        file_dest = input("Enter the path to where audio should be exported: ")
        image_dest = input("Enter the path to where Image should be exported: ")
        for i in range(count_row):
            time1 = df.at[i,temp[1]]
            time2 = df.at[i,temp[2]]
            file_name = df.at[i,temp[0]]
            # file_name = df.replace('?','')
            # file_name = df1.at[i,'question']
            t1 = get_seconds(str(time1))
            t2 = get_seconds(str(time2))
            assert os.path.exists(user_input), "I did not find the file at, "+str(user_input)
            audio(t1,t2,user_input,format,file_name,file_dest)            
            image(img_path,image_dest,file_name)
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
