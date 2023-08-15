import time
import os

print("Installing Redo...")
print("0%")
time.sleep(10)
print("10%")
time.sleep(5)
print("15%")
time.sleep(10)
print("20%")
time.sleep(5)
print("26%")
print("Installing DownUp...")
print("0%")
time.sleep(1)
print("25%")
time.sleep(1)
print("39%")
time.sleep(1)
print("100%")
print("Installing Redo...")
time.sleep(3)
print("32%")
time.sleep(3)
print("46%")
time.sleep(19)
print("100%")
print("Installing Redo Resources...")
time.sleep(5)
print("100%")

File_name = "Redo"

try:
    os.mkdir(File_name)
    print("Redo has been installed correctly, But need to install some files for execute Redo!.")
except FileExitsError:
    print("Sorry, But the file exists for install again, Thanks!.")
