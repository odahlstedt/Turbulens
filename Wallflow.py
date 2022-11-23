
# Uppgift 1
#--------------------------------------------------------
import sympy as sp
nu =1;
t = sp.symbols('x')

Rex = sp.symbols('Rex')

eq4 = ratio_momentumthickness* sp.sqrt(x/Rex)
first_order_derivative = eq4.diff(x)
print(2*first_order_derivative)

# Uppgift 2
#--------------------------------------------------------
from numpy import diff
x = np.linspace(1,7, 101)
x2 = np.linspace(1,7, 100)

dx = 1
diff_u_blasius = diff(u_blasius[i_plt])

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(1, 1, 1)
ax.plot(x ,   u_blasius[i_plt]/U0, 'k', label= '$U/U_0$')
ax.plot(x2 ,  diff_u_blasius/diff_u_blasius[0], '--k', label= '$ \u03C4 / \u03C4_W $' )
ax.legend()
ax.set_xlabel('$y/ \delta_X  $')
#ax.set_ylabel(r'$k(\kappa,\infty)/k \;,\; \epsilon(0,\kappa)/\epsilon$')
ax.set_title('Normalized velocity and shear-stress profiles from Blasius solution')

# Uppgift 3
#--------------------------------------------------------
dx = 1
div = np.zeros(100)
x = np.linspace(1,100, 100)
i =0;
i_plt = 80
for i in range(100):
  diff_u_blasius = u_blasius[i_plt, i] - u_blasius[i_plt, i+1] 
  diff_v_blasius = v_blasius[i_plt, i] - v_blasius[i_plt +1, i] 
  div[i] = diff_u_blasius + diff_v_blasius

print(div)

plt.plot(x, div)


# Uppgift 4
#--------------------------------------------------------
import math

U_0 = np.zeros(100)
wake = np.zeros(100)
law_of_wall = np.zeros(100)
x = np.linspace(0.001,1.001, 100)
i =0;
k=0.41
B=5.2
PI=0.5
Re=10000;
for i in range(100):
 law_of_wall[i]=(1/k)*sym.log(Re**0.8*x[i])+5.2
 wake[i]=(0.5/0.41)*2*sym.sin((3.14/2)*x[i])**2

u_bar = law_of_wall  + wake
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.plot(x, u_bar, 'r', label= '$ sum $')
ax.plot(x, law_of_wall, 'y', label= 'log law')
ax.plot(x, wake, 'b', label= 'wake contribution')

ax.legend()
ax.set_xlabel('$y/ \delta_X  $')
#ax.set_ylabel(r'$k(\kappa,\infty)/k \;,\; \epsilon(0,\kappa)/\epsilon$')
#ax.set_title('Normalized velocity and shear-stress profiles from Blasius solution')

# Uppgift 5
#--------------------------------------------------------
Cf = np.zeros(100)
Re = np.linspace(2000,100000, 100)
i =0;
k=0.41
B=5.2
PI=0.5
for i in range(100):
 Cf[i] = 2*((1/k)*sym.log(Re[i]**0.8)+5.2+(0.5/0.41)*2)**(-2)
 
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(Re, Cf)
ax.set_xlabel('Re')
ax.set_ylabel('$C_f$')
ax.set_title('$C_f$ (Re)')


# Ett sätt att lösa intergral på
#--------------------------------------------------------
from scipy.integrate import quad

def u(y):
  return (1/k)*sym.log(Re**0.8*y)+5.2 + (0.5/0.41)*2*sym.sin((3.14/2)*y)**2

def integrand(y):
    return 1-u(y)/U_0 
delta = quad(integrand, 0, 1)

def integrand(y):
    return u(y)/U_0 * (1-u(y)/U_0 )
theta = quad(integrand, 0, 1)


