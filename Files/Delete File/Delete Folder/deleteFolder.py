import os
if os.path.exists("myfolder Check In Files"): #Check if the file exists
  os.rmdir("myfolder Check In Files")
  print("Removed the folder!")
else:
  print("The folder does not exist! Make sure you spelled it correctly!")
