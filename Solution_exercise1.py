from complex_operations import r2p,p2r,ps,pm,pd,alf,a,conj,Electrical,alf2


"1 - Impedances and admittances (D)"

za = 1+2j
zb = 3-4j
zc = 10

"2 - Impedance (Y)"

d2y = Electrical.d2y
zan,zbn,zcn = d2y(za,zb,zc,return_rect=True)

print("\nCalculation of impedances in the Y equivalent:\n")
print(f"Zan = {r2p(zan)}\nZbn = {r2p(zbn)}\nZcn = {r2p(zcn)}")

"3 - Transforming impedance (Y) + line impedance in admittances"

zl = 0.1+0.2j
zal = zan+zl
zbl = zbn+zl
zcl = zcn+zl

yal = 1/zal
ybl = 1/zbl
ycl = 1/zcl

print("\nCalculation of admittances (line + Y equivalent):\n")
print(f"YA = {r2p(yal)}\nYB = {r2p(ybl)}\nYC = {r2p(ycl)}")

"4 - Phase voltages Van, Vbn and Vcn"

vab = (220,0)
van = pd(vab,alf2)
vbn = pm(van,a)
vcn = pm(van,a,a)

print("\nCalculation of phase voltages:\n")
print(f"Van = {van}\nVbn = {vbn}\nVcn = {vcn}\n")

"5 - Vnn' voltage"

vnn = pd(ps(pm(van,-yal),pm(vbn,-ybl),pm(vcn,-ycl)),yal+ybl+ycl)
print(f"=> Vnn' = {vnn}")

"6 - Van', Vbn' and Vcn' voltages"

vaN = ps(van,vnn)
vbN = ps(vbn,vnn)
vcN = ps(vcn,vnn)

print("\nCalculation of Van', Vbn' and Vcn' voltages:\n")
print(f"Van' = {vaN}\nVbn' = {vbN}\nVcn' = {vcN}\n")

"7 - Phase currents"

Ia = pd(vaN,zal)
Ib = pd(vbN,zbl)
Ic = pd(vcN,zcl)

print("Calculation of phase currents:\n")
print(f"Ia = {Ia}\nIb = {Ib}\nIc = {Ic}\n")

"8 - Phase voltages va'n', vb'n' and vc'n' (delta)"

vAN = pm(zan,Ia)
vBN = pm(zbn,Ib)
vCN = pm(zcn,Ic)

print("Calculation of phase voltages va'n', vb'n' and vc'n' (delta):\n")
print(f"Va'n' = {vAN}\nVb'n' = {vBN}\nVc'n' = {vCN}\n")

"9 - Line voltages (Y equivalent and delta) va'b', vb'c' and vc'a'"

vAB = ps(vAN,pm(vBN,-1))
vBC = ps(vBN,pm(vCN,-1))
vCA = ps(vCN,pm(vAN,-1))

print("Calculation of line voltages va'b', vb'c' and vc'a':\n")
print(f"Va'n' = {vAB}\nVb'n' = {vBC}\nVc'n' = {vCA}\n")

"10 - Phase currents (delta load)"

iAB = pd(vAB,zb)
iCB = pd(vBC,za)
iCA = pd(vCA,zc)

print("Calculation of phase currents Ia'b', Ib'c' and Ic'a':\n")
print(f"Ia'b' = {iAB}\nIb'c' = {iCB}\nIc'a' = {iCA}\n")