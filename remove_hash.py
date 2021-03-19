import os

# print(os.getcwd())

os.chdir('static/img')
for decade in range(10, 70, 10):
    for f in os.listdir(f"./{decade}/"):
        # print(f)
        try:
            os.replace(f, f.replace('#', ''))
        except:
            pass
        # if f.find('#') != -1:
        #     print(f)
        #
