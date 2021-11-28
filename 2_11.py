
def book_index(arr):
    index = ""
    for x in range(1, len(arr)-1):
        if arr[x]+1 == arr[x+1]:
            start = arr[x]
            print ("start ", start)
            while arr[x] +1 == arr [x+1]:
                x += 1
            end = arr[x]
            print ("end ", end)
            index += str(start)+  "-" + str(end)
            print('index', index)
        else:
            index += str(arr[x])
    return index
print(book_index([1,3,4,5,7,8,10]))


