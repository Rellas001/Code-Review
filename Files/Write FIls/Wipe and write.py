f = open("writeText.txt", "w")#W STANDS FOR WIPE(it does not) BUT THATS WHAT IT DOES!
f.write("Reset Content")
f.close()

#open and read the file after the appending:
f = open("writeText.txt", "r")
print("writeText's content:")
print("-- "+ f.read() + " --")
