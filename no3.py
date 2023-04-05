word = input()
k=0
for i in word:
    if i == 'ф':
        print("Ого! Это редкое слово!")
        k+=1
        exit()

if k == 0: print("Эх, это не очень редкое слово...")