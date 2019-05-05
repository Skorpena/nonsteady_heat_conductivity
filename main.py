import time as t
import numpy as np
import implementation as imp
import heatProperties as hP
import geometryProperties as gP
import constants as c


start = t.time()

#coeffs for the canonical system of equation
alfa = gP.N * [0]
beta = gP.N * [0]

#interim coeffs for the 'tau' upper value restriction: tau <= h**2/(2*a) 
A0 = gP.N * [0]
A1 = gP.N * [0]

a = len(imp.layers) * [0] #tempConductivity array

h = [c.s[0]/c.n, c.s[1]/c.n] #spatial pitch
T = gP.N*[c.T_initial]
T_bulk = []
tau_ = len(imp.layers) * [0] #interim array needed for 'tau' estimation

time = 0 #total time
tau = c.tau #time pitch
timeArray = [] #total time array needed for the output plots

while time <= c.TIME:
    timeArray.append(time)
    T_bulk += T 
    for i in range(gP.N):
        j = 0 if i < c.n else 1
        

        alfa[0] = 1/(1+imp.layers[0].Bi(T[0],0))
        beta[0] = imp.layers[0].Bi(T[0],0)*c.T_heat/(1+imp.layers[0].Bi(T[0],0))

        a0 = imp.layers[0].tempConduct(T[i])
        a1 = imp.layers[1].tempConduct(T[i])

        ai = imp.layers[j].heatConduct(T[i])/(h[j]**2)
        bi = (2*imp.layers[j].heatConduct(T[i])/(h[j]**2)+imp.layers[j].density
             *imp.layers[j].heatCapac(T[i])/tau)
        ci = imp.layers[j].heatConduct(T[i])/(h[j]**2)
        fi = -imp.layers[j].density*imp.layers[j].heatCapac(T[i])*T[i]/tau
        
        alfa[i] = ai/(bi - ci * alfa[i-1])
        beta[i] = (ci*beta[i-1]-fi)/(bi-ci*alfa[i-1])

        alfa[c.n-1] = (2*a0*a1*tau*imp.layers[1].heatConduct(T[i])/(2*a0*a1*tau
                      *(imp.layers[1].heatConduct(T[i])
                      +imp.layers[0].heatConduct(T[i])*(1-alfa[c.n-2]))
                      +(h[j]**2)*(a0*imp.layers[1].heatConduct(T[i])
                      +a1*imp.layers[0].heatConduct(T[i]))))
       
        beta[c.n-1] = ((2*a0*a1*tau*imp.layers[0].heatConduct(T[i])*beta[c.n-2]
                      +(h[j]**2)*(a0*imp.layers[1].heatConduct(T[i])
                      +a1*imp.layers[0].heatConduct(T[i]))*T[c.n-1])
                      /(2*a0*a1*tau*(imp.layers[1].heatConduct(T[i])
                      +imp.layers[0].heatConduct(T[i])*(1-alfa[c.n-2]))
                      +(h[j]**2)*(a0*imp.layers[1].heatConduct(T[i])
                      +a1*imp.layers[0].heatConduct(T[i]))))
        
        T[gP.N-1] = ((imp.layers[1].Bi(T[gP.N-1],1)*c.T_ambient + T[gP.N-2])
                    /(1-imp.layers[1].Bi(T[gP.N-1],1)))

    for i in range(gP.N-2,-1,-1):
        T[i] = alfa[i]*T[i+1]+beta[i]
    time += tau

a, b = int(len(T_bulk)/gP.N), gP.N  #rows, columns for .reshape
T_output = np.array(T_bulk)
T_output = T_output.reshape(a, b)
timeArray = np.round(np.array(timeArray),2)

end = t.time()
timeOfWaiting = round(end - start)
print('Total ' + str(timeOfWaiting) + ' sec. of waiting')

