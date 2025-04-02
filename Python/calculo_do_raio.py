import math
pi = math.pi

def calc_raio (r):
  raio = 2 * pi * r
  return raio
  
r = int(input("Digite o valor do raio: "))
print (calc_raio(r))