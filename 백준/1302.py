N  = int(input())

book_lst =[]
sell_lst=[]
for _ in range(N):
    book = input()
    if book in book_lst:
        sell_lst[book_lst.index(book)] +=1
    else:
        book_lst.append(book)
        sell_lst.append(1)



best = sell_lst.index(max(sell_lst))

print(best)
print(book_lst[best])