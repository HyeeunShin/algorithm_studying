c_letter = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

text = input()

for i in c_letter:
        if i in text:
            text = text.replace(i, "*")
        
print(len(text))