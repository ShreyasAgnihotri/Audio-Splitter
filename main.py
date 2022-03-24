from pydub import AudioSegment

counter = 0
flag = True

while flag:
    t1 = int(input("Enter the Starting time in seconds to split: "))
    t2 = int(input("Enter the Ending time in seconds to split: "))
    t1 = t1 * 1000 
    t2 = t2 * 1000
    newAudio = AudioSegment.from_wav("Sample.wav")
    newAudio = newAudio[t1:t2]
    newAudio.export(f'newSample{counter}.wav', format="wav")
    counter += 1
    choice = input("Do You want to continue Splitting: (Y/N) ").lower()
    if choice == "y":
        flag = True
    else:
        flag = False
