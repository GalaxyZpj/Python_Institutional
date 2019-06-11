text = "as it turned out our aRTHUR BElling was was to change every sunday we'd hurry along to and Jam ...".split()
print(text)
i1 = 0
text[0] = text[0].capitalize()    #3
while i1 < len(text):
    if len(text[i1]) != 1:
        if (text[i1][0] >= 'A' and text[i1][0] <= 'Z') and (text[i1][1] >= 'A' and text[i1][1] <= 'Z'):     #1
            text[i1] = text[i1].lower()
            text[i1] = text[i1].capitalize()
    if i1 < len(text)-1:
        if text[i1] == text[i1+1]:        #2
            text.pop(i1+1)
            i1 += 1
    s1 = text[i1][1:]
    s2 = text[i1][1:].upper()
    if text[i1][0] >= 'a' and s1 == s2:    #4
        text[i1] = text[i1].swapcase()
    if text[i1] == 'monday' or text[i1] == 'tuesday' or text[i1] == 'wednesday' or text[i1] == 'thursday' or text[i1] == 'friday' or text[i1] == 'saturday' or text[i1] == 'sunday':    #5
        text[i1] = text[i1].capitalize()
    i1 += 1

'''for x in text:
    if len(x) != 1:
        if (x[0] >= 'A' and x[0] <= 'Z') and (x[1] >= 'A' and x[1] <= 'Z'):     #1
            x = x.lower()
            x = x.capitalize()
    if i1 < len(text)-1:
        if x == text[i1+1]:        #2
            text.pop(i1+1)
            i1 += 1
    s1 = x[1:]
    s2 = x[1:].upper()
    if x[0] >= 'a' and s1 == s2:    #4
        x = x.swapcase()
    if x == 'monday' or x == 'tuesday' or x == 'wednesday' or x == 'thursday' or x == 'friday' or x == 'saturday' or x == 'sunday': #5
        x = x.capitalize()
    i1 += 1
'''

print(" ".join(text))
