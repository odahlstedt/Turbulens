#import matplotlib.pyplot as plt
num_relalizations = 10;
N =128;
u = np.zeros( (2, N, N))  
u_sum= np.zeros( (2, N, N)) 

x= np.arange(0,N)
Rxxf = np.zeros(N)
Ryyf = np.zeros(N)
Rxxg = np.zeros(N)
Ryyg = np.zeros(N)
urms = 0

for i in range(num_relalizations):
  u = Synthesis_Random2dIsotropic_Vector_or_Scalar(EnergySpectrum, N=N, L_0=1/4, eta_Kolmogorov=1/N, L_all=1)
  u_x = u[0, :, :]
  u_y = u[1, :, :]
  Rxxf += Autocorf(u_x)
  Ryyf += Autocorf(u_y)
  Rxxg += Autocorg(u_x)
  Ryyg += Autocorg(u_y)
 
for i in range(N):
  for j in range(N):
    urms += u_x[i][j]**2 + u_y[i][j]**2

urms = urms/2/N**2

print(urms)

Rxxf = Rxxf/num_relalizations
Ryyf = Ryyf/num_relalizations
Rxxg = Rxxg/num_relalizations
Ryyg = Ryyg/num_relalizations

g = (Rxxg + Ryyg) * urms/2

f = (Rxxf + Ryyf)*urms/2;

plt.plot(x/N, g )
plt.plot(x/N, f )

# annan fil
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

