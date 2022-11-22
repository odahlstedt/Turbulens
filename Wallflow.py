
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


