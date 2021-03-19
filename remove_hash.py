import os

# print(os.getcwd())

os.chdir('static/img')
for decade in range(10, 70, 10):
    mypath = f"./{decade}/"
    for f in os.listdir(mypath):

        # try:
        #     # os.join(decade,f)
        #     print(os.join(decade, f.replace('#', '')))
        #     os.rename(os.join(decade, f), os.join(decade, f.replace('#', '')))

        # except:
        #     pass
        if f.find('#') != -1:
            print(os.path.join(mypath, str(f)))
            os.rename(os.path.join(mypath, f), os.path.join(
                mypath, f.replace('#', '')))
        #
