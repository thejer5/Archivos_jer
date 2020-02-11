# resultado = lambda valor1, valor2 : valor1 / valor2
# value = resultado(20,4)
# print(value)

# formato = lambda question : '.......{}.......'.format(question)
# resultado = formato('[ ]')
# print(resultado)
# print(resultado)
# print(resultado)
# print(resultado)
# def verifier(value1, value2): ####VERIFICA SI CADA VALOR ES MAYOR A 0 Y SI NO RETORNA FALSE
#    return(value1 > 0 and value2 > 0)
# def multi(value1, value2):
#    if verifier(value1, value):#LLAMADO DE LA FUNCION
#       return(value1 * value2)
# result = verifier(9,7)
# print(result)
def division(v1, v2):
   def verifier(v1, v2):
      return v1 > 0 and v2 > 0
   return v1 / v2
result = division(50, 3)
print(result)
