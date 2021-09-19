def yoEstoyViendo (materias):
    lista = materias.split(",")
    c = 0
    for x in lista:
        x = "Yo estoy viendo " + x
        lista[c]=x
        c+=1
    return lista
    
print (yoEstoyViendo("Inglés,Física,Sociales,Historia,Programación"))