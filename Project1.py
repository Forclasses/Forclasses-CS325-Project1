# code that needs to be done
# Need, to export strings from another file and put them into
#a slm then  take the output from that ansd put it into another
#file


#start with getting the text from the first file

file_path = "C:\CS325-Project1\input.txt"

with open(file_path, 'r') as file:
    file_content = file.read()
import ollama
response = ollama.chat(model='phi3:mini', messages=[
  {
    'role': 'user',
    'content': file_content,
  },
])
print(response['message']['content'])#leaving this here for debugging
#ollama_var= "ollama run phi3:mini"
#print(ollama_var)
#print(file_content) #making sure this functions

output_file_path = "C:\CS325-Project1\output.txt"

with open(output_file_path, 'w') as file:
    file.write(response['message']['content'])
#this works wonderfully 

#next step is to work out how to quirey phi3-mini and take that
#result and send it to output.txt...