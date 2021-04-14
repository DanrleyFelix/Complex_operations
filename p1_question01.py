from complex_operations import pm,pd,alf,a,neg_seq,mm

# Ia = 1*Ia
# Ib = a*Ia
# Ic = a²*Ia => Ia = Ic/a² (negative sequence)

Ic = (67,-52)
Ia = pd(Ic,pm(a,a))
res = mm(Ia,neg_seq)

print(res)

iAB = pd(Ia,alf)

print(iAB)