# Read the keywords from the file
a=[]
with open('C:\\Users\\pc\\Desktop\\upworl\\keys.txt', 'r') as f:
    a=f.readlines()
    a = [line.strip() for line in a]
print(len(a))
b=[]
c=[]
d=[]
ans=0
for i in a :
    if len(i)<2:
        a.remove(i)
print(len(a))
# Read the bios from the file
with open('C:\\Users\\pc\\Desktop\\upworl\\original.txt', 'r', encoding='utf8') as f:
    for i in f.readlines():
        b.append(i)
# Create a new list to store the strings that don't include keywords
filtered_strings = []

for string in b:
    if string[0]=='(':
        # Convert the string and keywords to lowercase for case-insensitivity
        lowercase_string = string.lower()
        lowercase_keywords = [keyword.lower() for keyword in a]

        # Check if the string includes any of the keywords
        for keyword in lowercase_keywords:
            key_index = lowercase_string.find(keyword)
            if keyword!='' and (key_index != -1) and (string[key_index-2]!='\\') and ((string[key_index-1] in [' ', '.',',',';',':','!','?','(',')',"'",'\n','\\','/','\t'] or ord(string[key_index-1]) >= 0x1F600 and ord(string[key_index-1]) <= 0x1F64F) and (string[key_index+len(keyword)] in [' ', '.',',',';',':','!','?','(',')',"'",'\n','\\','/','\t'] or ord(string[key_index+len(keyword)]) >= 0x1F600 and ord(string[key_index+len(keyword)]) <= 0x1F64F)):
                c.append([string,keyword])
                break
        else:
            d.append(string)
    else:
        d.append(string)
# Open the file in write mode

with open('C:\\Users\\pc\\Desktop\\upworl\\deleted.txt', 'w',encoding='utf8') as f:
    for string in c:
        # Write the string to a new line in the file
        s="[{}], keyword found : '{}'\n".format(string[0],string[1])
        f.write(s)

with open('C:\\Users\\pc\\Desktop\\upworl\\filtered.txt', 'w',encoding='utf8') as f:
    for string in d:
        # Write the string to a new line in the file
        f.write(string)