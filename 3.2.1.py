I = [1, 4, 1, 6, "hello", "a", 5, "hello"]
X = []
for i in I:
    if I.count(i)>1 and X.count(i) == 0:
        X.append(i)
print(X)
    
    

