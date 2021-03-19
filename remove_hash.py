import os

# print(os.getcwd())

os.chdir('static/img')
for decade in range(10, 70, 10):
    mypath = f"./{decade}/"
    for f in os.listdir(mypath):

        if f.find('#') != -1:
            print(os.path.join(mypath, str(f)))
            os.replace(os.path.join(mypath, f), os.path.join(
                mypath, f.replace('#', '')))
    # print('\n'*10)
        # if f.find('#') != -1:
        #     print(os.path.join(mypath, str(f)))
