
# Uppgift 1
#--------------------------------------------------------
import sympy as sp
nu =1;
t = sp.symbols('x')

Rex = sp.symbols('Rex')

eq4 = ratio_momentumthickness* sp.sqrt(x/Rex)
first_order_derivative = eq4.diff(x)
print(2*first_order_derivative)

