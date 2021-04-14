from complex_operations import Electrical

van = (10,0)
vbn = (10,-120)
vcn = (10,120)

zla = zlb = zlc = 5j
znn = 2
zan = 10
zcn = 2
zbn = 5

inn = Electrical.inN(van,vbn,vcn,zla,zlb,zlc,zan,zbn,zcn,znn,line_currents=True)

print(inn)