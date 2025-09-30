# O Python possui uma função no módulo math que permite a comparação aproximada
#entre números de ponto flutuante.

import math

a = math.isclose(10 / 3, 3.3, rel_tol=0.1)
print(a)

b = math.isclose(10 / 3, 3.3, rel_tol=0.01)
print(b)

c = math.isclose(10 / 3, 3.4, rel_tol=0.1)
print(c)

# Em que o parâmetro opcional rel_tol é a diferença relativa aceita entro os 
#dois números. No caso, 0.1 representa 10%, 0.01, 1% e assim por diante. O valor
#padrão é 10^-9 (1e-09 em notação científica)