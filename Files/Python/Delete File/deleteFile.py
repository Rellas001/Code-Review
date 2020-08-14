import os
if os.path.exists("demofile.txt"): #Check if the file exists
  os.remove("demofile.txt")
  print("Removed the file!")
else:
  print("The file does not exist! Make sure you spelled it correctly!")
