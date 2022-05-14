import os
import subprocess

def dir_list_folder(head_dir, dir_name):
    outputList = []
    for root, dirs, files in os.walk(head_dir):
        for d in dirs:
            if d.upper() == dir_name.upper():
                outputList.append(os.path.join(root, d))
    return outputList
def set_path(cwd,bat_path):
    bat_script = cwd + r"\setpath.bat"
    myBat = open(bat_script, "w+")
    myBat.write(r'for /f "usebackq tokens=2,*" %%A in (`reg query HKCU\Environment /v path`) do set my_user_path=%%B')
    myBat.write("\n")
    myBat.write(r'if exist "' + bat_path + r'" setx path "' + bat_path + r';%my_user_path%"')
    myBat.close()
    subprocess.call([bat_script])
def check():
    cwd = os.getcwd()
    loc = cwd + "\\ffmpeg"   
    bat_path = "\n".join(dir_list_folder(loc, 'bin'))
    if bat_path in os.environ["Path"]:
        return True
    else:
        set_path(cwd,bat_path)     
        print("Please Restart the System")
        
    