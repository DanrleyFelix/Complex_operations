from complex_operations import ps,pd,pm,alf,a,pos_seq,mm,conj,re

zab = 16+28j
zbc = 14.8-6.4j
zca = 14+8j
vab = (230,0)
vbc = (230,-120)
vca = (230,120)

Iab = pd(vab,zab)
Ibc = pd(vbc,zbc)
Ica = pd(vca,zca)

Ia = ps(Iab,pm(-1,Ica))
Ib = ps(Ibc,pm(-1,Iab))
Ic = ps(Ica,pm(-1,Ibc))

vac = pm(vca,-1)
vcb = pm(vbc,-1)

w1 = re(pm(vac,conj(Ia)))
w2 = re(pm(vcb,conj(Ib)))
wt = w1+w2

print(Iab,Ibc,Ica)
print(Ia,Ib,Ic)
print(w1,w2,wt)

