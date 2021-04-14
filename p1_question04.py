# s = 40k + j.53,34k p/VL = 200V
# Vab = (220,10) - positive sequence

from complex_operations import pm,alf,a,mm,pos_seq,conj,pd,r2p,d2r,r2d,p2r,re,im,Electrical
from math import cos

# Part 1

vl = 200
vf = vl/(3**0.5)
s3o = 40000+53340j
sf = s3o/3
zc = pd(vf**2,conj(sf))
vab = (220,0)
vab,vbc,vca = mm(vab,pos_seq)[0]
van = pd(vab,alf)
van,vbn,vcn = mm(van,pos_seq)[0]
Ia = pd(van,zc)
Ia,Ib,Ic = mm(Ia,pos_seq)[0]

# Part 2

vnf = vab

snf = pm(pm(pd(vnf,vl),pd(vnf,vl)),sf)
snf3 = pm(3,snf,return_rect=True)
fpn = 0.92
fpv = cos(d2r(snf[1]))
p = re(snf3)
q = im(snf3)
qn = Electrical.pfc(p=p,q=q,fp=fpv,fpn=fpn)

# Prints

print(vf,r2p(sf))
print(zc)
print(vab,vbc,vca)
print(van,vbn,vcn)
print(Ia,Ib,Ic)
print(snf,snf3)
print(fpv)
print(qn)


