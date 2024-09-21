# code that needs to be done
# Need, to export strings from another file and put them into
#a slm then  take the output from that ansd put it into another
#file


#start with getting the text from the first file

file_path = "C:\CS325-Project1\input.txt"

with open(file_path, 'r') as file:
    file_content = file.read()

print(file_content) #making sure this functions