from complex_operations import Electrical

p = 10000
vl = 440
fp = 0.9
fpn = 0.97
c = 3**0.5
il = p/(c*vl*fp)
print(il)
z = Electrical.pfc
q = z(p=p,fp=fp,fpn=fpn,il=il,vl=vl)
print(q)
