alfabeto = [chr(i) for i in range(ord('a'), ord('z') + 1)]
for i in range(len(alfabeto),1,-1):
    if i % 3 == 0:
        alfabeto.pop(i-1)
    
print(alfabeto)
