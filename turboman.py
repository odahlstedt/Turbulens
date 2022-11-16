num_relalizations = 2;
N =4;
u = np.zeros( (2, N, N))  
u_sum= np.zeros( (2, N, N)) 

u+u_sum

for i in range(num_relalizations):
  u = Synthesis_Random2dIsotropic_Vector_or_Scalar(EnergySpectrum, N=N, L_0=1/4, eta_Kolmogorov=1/10000, L_all=1)
  u_sum = u_sum + u;

u_average = u_sum/num_relalizations

u_x = u_average[0, :, :]
u_y = u_average[1, :, :]

u_x1 = u_x[0,:];

Rxxf = Autocorf(u_x)
Ryyf = Autocorf(u_y)

Rxxg = Autocorg(u_x)
Ryyg = Autocorg(u_y)


print(Rxxf)
print('----------------------------------------------------------------')
print(Ryyf)
print('----------------------------------------------------------------')
print(Rxxg)
print('----------------------------------------------------------------')
print(Ryyg)

print(u_x)
print('----------------------------------------------------------------')
print(u_y)
print('----------------------------------------------------------------')

