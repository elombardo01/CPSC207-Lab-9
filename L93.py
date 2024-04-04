#Emme and Allison
#Lab 9 part C

cpsc_names = ["Emma","Lombardo","Abigail","Lopez","Anastacia","Aguirre","Allison","Macrowski","Sydney","Eidelbes","Therese","Burns","Mandy","Guo","Samantha","Patin","Viviana","Antimo","Abigail","Newton","Elise","Ward","Leena","Bradley"]

def frequency(cpsc_names):
    d=dict()
    for word in cpsc_names[1::2]:
        char = word[0]
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1
    return d

print(frequency(cpsc_names))
