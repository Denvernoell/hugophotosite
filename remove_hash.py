import os

# print(os.getcwd())

os.chdir('static/img')
for decade in range(10, 70, 10):
    for f in os.listdir(f"./{decade}/"):

        try:
            # os.join(decade,f)
            print(os.join(decade, f.replace('#', '')))
            os.rename(os.join(decade, f), os.join(decade, f.replace('#', '')))

        except:
            pass
        # if f.find('#') != -1:
        #     print(f)
        #
