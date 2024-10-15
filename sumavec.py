#Sumar vectores por elemento
def sumavec(vec1, vec2):
    vecfinal=[]
    for i in range(len(vec1)):
        suma=vec1[i]+vec2[i]
        vecfinal.append(suma)
    return vecfinal

vec1=[1,2,3,4]
vec2=[2,3,4,5]
print(sumavec(vec1, vec2))
