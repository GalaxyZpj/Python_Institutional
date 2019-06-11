text = "How much wood would a woodchuck chuck If a woodchuck could chuck wood? He  would  chuck ,  he  would ,  as  much  as  he  could , And  chuck  as  much  as  a  woodchuck  would If  a  woodchuck  could  chuck  wood."
count = 0
i = 0
while True:
    i = text.find('wood', i+1)
    if i == -1: break
    if ord(text[i + 4]) not in range(ord('a'), ord('z')):
        count += 1
    i += 1
print(count)
