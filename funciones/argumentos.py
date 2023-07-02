#calcular el promedio 

def promedio(*args):#tupla
    return sum(args)/len(args)

#resultado=promedio([10,50,4,3,5,2,3,])
resultado=promedio(10,50,4,3,5,2,3)
print(resultado)



def combinacio(p1,p2,*args, p4=500):
    print(p1,p2,args,p4)
    
combinacio(10,20,30,4,56,p4=1000)



#kwargs -> diccionarios
def usuarios(**kwargs):
    print(kwargs)
    print(type(kwargs))
    
usuarios (eduardo=[10,10,10],fernando=[2,432,1,3])

def combinacion(*args,**kwargs):
    print(kwargs)
    print(args)
    
combinacion(1,2,3,4,5,cody=True,curso='python')