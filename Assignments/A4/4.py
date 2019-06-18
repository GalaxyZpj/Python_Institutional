def word_freq(l):
    s = set(l)
    d = {}
    for x in s:
        d[x] = l.count(x)
    return d
l = list("aaaaabbbbcccdde")
print(word_freq(l))
s = word_freq(l)
word_freq = { 'a' : 5, 'b' : 4, 'c' : 3, 'd' : 2, 'e' : 1 }
if s == word_freq :
    print("Correct")
else :
    print("Wrong")
