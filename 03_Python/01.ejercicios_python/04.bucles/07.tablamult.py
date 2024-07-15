def tabla_multi():
    for h in range (1,11):    
        for i in range(1, 11):
            resultado = lambda a,b: a * b
            print(f"{h} X {i} = {resultado(h, i)}  ", end="\t" )
            i += 1
        print("\n")
        h += 1

tabla_multi()
       

    