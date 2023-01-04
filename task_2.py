def unique(data):
    
    lista = []
    zbior = set() 

    for x in data:
        if x not in zbior:
            lista.append(x)
            zbior.add(x)



    return lista
