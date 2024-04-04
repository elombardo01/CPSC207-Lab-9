#Emme and Allison
#Lab 9 part B

cpsc = {"Lombardo":"Emma", "Lopez":"Abigail", "Aguirre":"Anastacia", "Macrowski":"Allison", "Eidelbes":"Sydney", "Burns":"Therese", "Guo":"Mandy", "Patin":"Samantha", "Antimo":"Viviana", "Newton":"Abigail", "Ward":"Elise", "Bradley":"Leena"}  

def histogram(word):
    d = dict()
    for char in word:
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1
    return d


print(histogram(cpsc.values()))
