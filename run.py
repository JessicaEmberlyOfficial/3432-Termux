import os
os.system("clear")
question = input("(l)aunch, or (i)nstall?: ")
if question == "l":
  os.system("python " + os.getcwd() + "/tools.py")
if question == "i":
  os.system("python " + os.getcwd() + "/installer.py")