from complex_operations import *
from math import acos,cos,sin

vab = (220,0)
vl = 220
zl = 0.2j
ct = 3**0.5

# Load delta
fp1 = 0.8
phi1 = acos(0.8)
s1 = 10000
il1 = s1/(ct*vl)
iab_d = (il1,-1*r2d(phi1))
iab_d,ibc_d,ica_d = mm(iab_d,pos_seq)[0]
Ia_d = ps(iab_d,pm(ica_d,-1))
Ib_d = ps(ibc_d,pm(iab_d,-1))
Ic_d = ps(ica_d,pm(ibc_d,-1))


p2 = 5000
fp2 = 0.92
phi2 = acos(fp2)
il2 = p2/(ct*vl*fp2)
iab_y = (il2,-1*r2d(phi2))
iab_y,ibc_y,ica_y = mm(iab_y,pos_seq)[0]

van_y = pd(vab,alf)
van_y,vbn_y,vcn_y = mm(van_y,pos_seq)[0]
vab,vbc,vca = mm(vab,pos_seq)[0]

van_g = ps(pm(zl,ps(iab_y,Ia_d)),van_y)
van_g,vbn_g,vcn_g = mm(van_g,pos_seq)[0]
vab_g = pm(van_g,alf)
vab_g,vbc_g,vca_g = mm(vab_g,pos_seq)[0]


print(iab_d,ibc_d,ica_d)
print(Ia_d,Ib_d,Ic_d)
print(van_y,vbn_y,vcn_y)
print(iab_y,ibc_y,ica_y)
print(van_g,vbn_g,vcn_g)
print(vab_g,vbc_g,vca_g)
