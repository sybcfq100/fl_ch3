import matplotlib.pyplot as plt
from scipy import interpolate
import numpy as np

# 读入要调整的数据

fileR = 'C:/Users/sybcf/Desktop/workWithAllData/Reflection_sample1.txt'
fileRCS = 'C:/Users/sybcf/Desktop/workWithAllData/RCS_sample1_2.6-3.95GHz.txt'
aR = np.loadtxt(fileR)
aRCS = np.loadtxt(fileRCS)
xR = aR[:, 0]
yR_0 = aR[:, 1]
yR_13 = aR[:, 2]
yR_22 = aR[:, 3]

tck_0 = interpolate.splrep(xR, yR_0)
tck_13 = interpolate.splrep(xR, yR_13)
tck_22 = interpolate.splrep(xR,yR_22)

xxR = np.linspace(min(xR),max(xR),501)
yyR_0 = interpolate.splev(xxR, tck_0, der=0)
yyR_13 = interpolate.splev(xxR,tck_13, der=0)
yyR_22 = interpolate.splev(xxR,tck_22, der=0)

plt.plot(xxR, yyR_0,'o',xxR,yyR_13,'*',xxR,yyR_22,'+')

Data_R0 = np.c_[xxR,yyR_0,yyR_13,yyR_22]
print(Data_R0.shape)
np.savetxt('Data_R0.txt',Data_R0)
