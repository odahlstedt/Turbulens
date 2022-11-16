
# 1
#-------------------------------------

#import matplotlib.pyplot as plt
num_relalizations = 10;
N =512;
u = np.zeros( (2, N, N))  
u_sum= np.zeros( (2, N, N)) 

x= np.arange(0,N)
Rxxf = np.zeros(N)
Ryyf = np.zeros(N)
Rxxg = np.zeros(N)
Ryyg = np.zeros(N)
urms = 0

for i in range(num_relalizations):
  u = Synthesis_Random2dIsotropic_Vector_or_Scalar(EnergySpectrum, N=N, L_0=1/4, eta_Kolmogorov=1/N *2, L_all=1)
  u_x = u[0, :, :]
  u_y = u[1, :, :]
  Rxxf += Autocorf(u_x)
  Ryyf += Autocorf(u_y)
  Rxxg += Autocorg(u_x)
  Ryyg += Autocorg(u_y)

print(u)

 
for i in range(N):
  for j in range(N):
    urms += u_x[i][j]**2 + u_y[i][j]**2

urms = urms/2/N**2


Rxxf = Rxxf/num_relalizations
Ryyf = Ryyf/num_relalizations
Rxxg = Rxxg/num_relalizations
Ryyg = Ryyg/num_relalizations

print(Rxxf) # stämmer gå i-xled
print(Rxxg) # gå i y-led
print(Ryyf) # har Ryyg  gå i -yled
print(Ryyg) # gå i x-led

g = (Rxxg + Ryyg) * urms/2
f = (Rxxf + Ryyf)*urms/2;


plt.plot(x/N, g,'r', label='g(r)')
plt.plot(x/N, f , 'b', label='f(r)')
plt.legend();

# 1
#---------------------------------------------------------------------------------------------------------------
def Autocorf(u):
  R = np.zeros(N)
  for dj in range(N):
   R[dj] = np.sum( [np.sum(u[:,j]*u[:,np.mod(j+dj,N)] ) for j in range(N) ] ) /np.sum( u**2)   
  return R

def Autocorg(u):
  R = np.zeros(N)
  for dj in range(N):
   R[dj] = np.sum( [np.sum(u[j,:]*u[np.mod(j+dj,N),:] ) for j in range(N) ] ) /np.sum( u**2)   
  return R


# 2
#---------------------------------------------------------------------------------------------------------------
intf =np.trapz(f, dx = 1/128)

intg = np.trapz(g, dx =1/128)

print(intf)
print(intg)
print(intf/intg)

# 3
#---------------------------------------------------------------------------------------------------------------
from numpy import diff
dx = 1
df = diff(diff(f))/dx
dg = diff(diff(g))/dx

lamda_f = (-1/2*df[0])**(-1/2)
lamda_g = (-1/2*dg[0])**(-1/2) 

# 4
#---------------------------------------------------------------------------------------------------------------
E11 = rfftn(Rxxf)
x= np.arange(0,len(E11))
print(len(E11))
plt.loglog(x, E11)

print(lamda_g/lamda_f)
