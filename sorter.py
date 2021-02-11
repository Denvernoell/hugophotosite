# cp .\Originals\*\*\*1[0-9]-*.JPG .\SortByDate3\10
import subprocess

for decade in range(20, 100, 10):
    myline = (
        fr"cp P:\11-Films\Originals\*\*\*{int(decade/10)}[0-9]-*.JPG P:\11-Films\SortByDate3\{decade}")
    # myline = fr"mkdir P:\11-Films\SortByDate3\{decade}"
    print(myline)
    subprocess.run(["powershell", "-Command", myline])
