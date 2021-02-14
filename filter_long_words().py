def filter_long_words(a,n):
    l=[]
    for i in a:
        if len(i)>n:
            l.append(i)

    print(l)



lst=['asd','sdad','sdas','werwer']
n=3
filter_long_words(lst,n)

