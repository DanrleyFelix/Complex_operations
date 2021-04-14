from complex_operations import Electrical,mm,neg_seq,alf2,pd,ps

vab = (220,0)
zgy = 0.2j
zl = 0.1+0.5j
zy = 1
zan = 2+1j
zbn = 1-2j
zcn = 2

vab,vbc,vca = mm(vab,neg_seq)[0]
van = pd(vab,alf2)
van,vbn,vcn = mm(van,neg_seq)[0]
iaa = pd(van,ps(zgy,zl,zan,zy))
ibb = pd(vbn,ps(zgy,zl,zbn,zy))
icc = pd(vcn,ps(zgy,zl,zcn,zy))


print(vab,vbc,vca)
print(van,vbn,vcn)
print(iaa,ibb,icc)