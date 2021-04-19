import os
import shutil

# print(os.getcwd())

num_split = 100

os.chdir('static/img')

for decade in range(10, 70, 10):
    try:
        os.mkdir(f"{decade} split")
    except:
        pass
    mypath = f"./{decade}/"

    i = 0
    start_num = 1

    my_folders = {}
    my_folder = []

    for f in os.listdir(mypath):
        i += 1
        my_folder.append(f)

        # Check if divisible by 100
        if i % num_split == 0 or i == len(os.listdir(mypath)):
            end_num = i
            folder_name = (f"{start_num}-{end_num}")
            start_num = end_num + 1

            new_folder_path = (f"{decade} split/{folder_name}")
            try:
                os.mkdir(new_folder_path)
            except:
                pass

            for f in my_folder:
                shutil.copy(f"{mypath}/{f}", f"{new_folder_path}/{f}")
            my_folder = []
