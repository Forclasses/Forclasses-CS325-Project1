
#start with getting the text from the first file

file_path = "C:\CS325-Project1\input.txt"
# opening the file getting the results from said file and putting
# them in file_content
with open(file_path, 'r') as file:
    file_content = file.read()
#importing ollama and then sending file content to it so they can be
#answered
import ollama
response = ollama.chat(model='phi3:mini', messages=[
  {
    'role': 'user',
    'content': file_content,
  },
])
#print(response['message']['content'])#leaving this here for debugging

#sending the results from ollama to the output file 
output_file_path = "C:\CS325-Project1\output.txt"

with open(output_file_path, 'w') as file:
    file.write(response['message']['content'])
#this works wonderfully 

