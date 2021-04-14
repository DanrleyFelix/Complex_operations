# Direct sequence - BAC
# Balanced system (Delta load)
# f = 60hz - VL = 220V

from complex_operations import ps,pd,pm,alf,a,pos_seq,mm,conj,re

zab = 15
zbc = 15j
zca = -15j
vab = (220,0)

vab,vbc,vca = mm(vab,pos_seq)[0]

print(vab,vbc,vca)

Iab = pd(vab,zab)
Ibc = pd(vbc,zbc)
Ica = pd(vca,zca)

print(Iab,Ibc,Ica)

sload = ps(pm(vab,conj(Iab)),pm(vbc,conj(Ibc)),pm(vca,conj(Ica)))

print(sload)

Ia = ps(Iab,pm(-1,Ica))
Ib = ps(Ibc,pm(-1,Iab))
Ic = ps(Ica,pm(-1,Ibc))

print(Ia,Ib,Ic)

# B is the common point and c potential coil point
vcb = pm(vbc,-1)

w1 = re(pm(vab,conj(Ia)))
w2 = re(pm(vcb,conj(Ic)))
wt = w1+w2

print(w1,w2,wt)