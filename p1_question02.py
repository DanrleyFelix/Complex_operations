from complex_operations import r2p,p2r,ps,pm,pd,a

"impedâncias - carga equilibrada"

zy = 2+3j
zd = -6.5j
zl = 5j

Ia = (60,0)
Ib = pm(Ia,a,a)
Ic = pm(Ia,a)

print("\nIA, IB e IC:\n",Ia,Ib,Ic)

vAN = pm(zy,Ia)
vBN = pm(zy,Ib)
vCN = pm(zy,Ic)

print("Va'n', Vb'n' e Vc'n':\n",vAN,vBN,vCN)

vAB = ps(vAN,pm(vBN,-1))
vBC = ps(vBN,pm(vCN,-1))
vCA = ps(vCN,pm(vAN,-1))

print("Va'b', Vb'c' e Vc'a':\n",vAB,vBC,vCA)

iAB = pd(vAB,zd)
iBC = pd(vBC,zd)
iCA = pd(vCA,zd)

print("Ia'b', Ib'c' e Ic'a':\n",iAB,iBC,iCA)

Ial = ps(iAB,pm(iCA,-1))
Ibl = ps(iBC,pm(iAB,-1))
Icl = ps(iCA,pm(iBC,-1))

print("Ia', Ib' e Ic':\n",Ial,Ibl,Icl)

Van = ps(pm(ps(Ial,Ia),zl),vAN)
Vbn = pm(Van,a,a)
Vcn = pm(Van,a)

print("Van, Vbn e Vcn:\n",Van,Vbn,Vcn)

