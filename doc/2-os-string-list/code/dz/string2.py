string = 'one-two-three-four'
string_separated = string.split("-")
print(';'.join(string_separated))

#string_2 = string.replace('-', ';')
#print(string_2)


#string_separated_capitalized = []


#for word in string_separated:
#    string_separated_capitalized.append(word.capitalize())



#string_3 = ";".join(string_separated_capitalized)
print(";".join(map(lambda item: item.capitalize(), string_separated)))


string_separated_numerated = []

for i in range(len(string_separated)):
    string_separated_numerated.append(str(i + 1) + " - " + string_separated[i])

string_4 = ";".join(string_separated_numerated)
print(string_4)
