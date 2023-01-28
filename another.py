import os
import re
import chardet

#remove emojis and escape characters from the file before entering it here , using .replace() method and using emoji module 
# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the "keys.txt" file
keys_file = os.path.join(script_dir, 'keys.txt')
original_file=os.path.join(script_dir,'original.txt')
with open(original_file, 'rb') as f:
    result = chardet.detect(f.read())

with open(keys_file, 'rb') as f:
    result1 = chardet.detect(f.read())


def check(text, keyword):
    pattern = r"(?:\b|[^\w'])" + keyword.lower() + r"(?:\b|[^\w'])"

    match= re.search(pattern, text.lower())
    if match :
        return True
    return False

# Read the keywords from the file
a=[] #keyword list
#file should exist in a folder named upwork on the desktop , and named keys.txt
with open(keys_file, 'r', encoding=result1['encoding'], errors='ignore') as f:
    a=f.readlines()
    a = [line.strip() for line in a]



b=[] #original text list
c=[] #deleted lines with keywords found list
d=[] #list containing the filtered lines 
print("script is running , please wait ...")


for i in a :
    #if the line is empty in the keys file we just remove it
    if len(i)==0:
        a.remove(i)


# Read the bios from the file
#file should exist in a folder named upwork on the desktop , and named original.txt
with open(original_file, 'r', encoding=result['encoding'], errors='ignore') as f:
    b = f.readlines()

#the main filtering program
for string in b:
    #line that includes users starts with a '('
    if string[0]=='(':
        # Convert the string and keywords to lowercase for case-insensitivity
        lowercase_string = string.lower()
        lowercase_keywords = [keyword.lower() for keyword in a]

        # Check if the string includes any of the keywords and some more verification that the keywords is either surrounded by a combination of emojis , space or punctuation
        for keyword in lowercase_keywords:
            if keyword!='' and check(lowercase_string,keyword):
                c.append([string,keyword])
                break
            
        else:
            #adding the filtered lines to a list named d
            print(string+'\n')
            d.append(string)
    else:
        d.append(string)


with open(os.path.join(script_dir,'deleted.txt'), 'w',encoding='utf8') as f:
    for string in c:
        # Write the string to a new line in the file
        s="[{}], keyword found : '{}'\n".format(string[0],string[1])
        f.write(s)

with open(os.path.join(script_dir,'filtered.txt'), 'w',encoding='utf8') as f:
    for string in d:
        # Write the string to a new line in the file
        f.write(string)


print('\nScript is done ..\ncheck filtered.txt and deleted.txt files .')


#Now that the DB is filtered ,we reserve it and put the emojis back in the lines that still exist in the DB the program should be fairly easy .

