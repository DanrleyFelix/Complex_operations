from cmath import polar, phase, rect
from math import pi,tan,sin,acos
from numpy.linalg import solve
from numpy import array


"Convert radian to degrees"
def r2d(o):

    return o*(180/pi)

"Convert degrees to radian"
def d2r(o):

    return o*(pi/180)

"Convert rectangular to polar"
def r2p(a,rad=False):

    a = polar(a)
    if rad:
        a = (a[0], a[1])
    else:
        a = (a[0], r2d(a[1]))
    return a

"convert polar to rectangular"
def p2r(a,b,rad=False):

    if rad:
        c = rect(a,b)
    else:
        b = d2r(b)
        c = rect(a,b)
    return c

"Polar multiplication (return polar as default)"
def pm(a,*args,return_rect=False,return_rad=False,is_rad=False):

    if isinstance(a, tuple):
        a = p2r(a[0],a[1],rad=is_rad)
    for cx in args:
        if isinstance(cx, tuple):
            cx = p2r(cx[0],cx[1],rad=is_rad)
        a = a*cx
    if return_rect:
        return a
    else:
        a = r2p(a,rad=return_rad)
        return a

"Polar division (return polar as default)"
def pd(a,b,return_rect=False,return_rad=False,is_rad=False):

    if isinstance(a, tuple):
        a = p2r(a[0],a[1],rad=is_rad)
    if isinstance(b, tuple):
        b = p2r(b[0],b[1],rad=is_rad)
    a = a/b
    if return_rect:
        return a
    else:
        return r2p(a,rad=return_rad)
        
"Polar sum (return polar as default)"
def ps(a,*args,return_rect=False,return_rad=False,is_rad=False):

    if isinstance(a, tuple):
        a = p2r(a[0],a[1],rad=is_rad)
    for cx in args:
        if isinstance(cx, tuple):
            cx = p2r(cx[0],cx[1],rad=is_rad)
        a = a+cx
    if return_rect:
        return a
    else:
        return r2p(a,rad=return_rad)

def conj(a,is_rad=False,return_rect=False,return_rad=False):
    
    if isinstance(a, tuple):
        a = p2r(a[0],a[1],rad=is_rad)
    a = a.conjugate()
    if return_rect:
        return a
    else:
        return r2p(a,rad=return_rad)

def re(a,is_rad=False):

    if isinstance(a, tuple):
        a = p2r(a[0],a[1],rad=is_rad)
    a = a.real
    return a

def im(a,is_rad=False):

    if isinstance(a, tuple):
        a = p2r(a[0],a[1],rad=is_rad)
    a = a.imag
    return a

def sol(a,b,return_rect=False,return_rad=False,is_rad=False):

    temp1 = []
    temp2 = []
    for var in b:
        if isinstance(var, tuple):
           temp2.append(p2r(var[0],var[1],rad=is_rad))
        else:
            temp2.append(var)
    for var in a:
        aux = []
        for var_2 in var:
            if isinstance(var_2, tuple):
                aux.append(p2r(var_2[0],var_2[1],rad=is_rad))
            else:
                aux.append(var_2)
        temp1.append(aux)
    rect_result = solve(temp1,temp2)
    if return_rect:
        return rect_result
    else:
        polar_result = []
        for var in rect_result:
            polar_result.append(r2p(var,rad=return_rad))
        return polar_result

def mm(a,b,return_rect=False,return_rad=False,is_rad=False,scalar=True):

    temp1 = []
    temp2 = []
    if not isinstance(a,list):
        a = [[a]]
    elif not isinstance(a[0],list):
        a = [a]
    if not isinstance(b,list):
        b = [[b]]
    elif not isinstance(b[0],list):
        b = [b]
    for var in b:
        aux = []
        for var_2 in var:
            if isinstance(var_2, tuple):
                aux.append(p2r(var_2[0],var_2[1],rad=is_rad))
            else:
                aux.append(var_2)
        temp1.append(aux)
    for var in a:
        aux = []
        for var_2 in var:
            if isinstance(var_2, tuple):
                aux.append(p2r(var_2[0],var_2[1],rad=is_rad))
            else:
                aux.append(var_2)
        temp2.append(aux)
    if scalar:
        rect_result = array(temp2)*array(temp1)
    else:
        rect_result = array(temp2)@array(temp1)
    if return_rect:
        return rect_result
    else:
        polar_result = []
        aux = []
        for var in rect_result:
            for var_2 in var:
                aux.append(r2p(var_2,rad=return_rad))
            polar_result.append(aux)
        return polar_result


class Electrical:

    "Convert Delta to Y"
    @staticmethod
    def d2y(za,zb,zc,is_rad=False,return_rect=False,return_rad=False):

        zabc = ps(za,zb,zc,is_rad=is_rad)
        zan = pd(pm(zb,zc,is_rad=is_rad),zabc,return_rad=return_rad,return_rect=return_rect)
        zbn = pd(pm(za,zb,is_rad=is_rad),zabc,return_rad=return_rad,return_rect=return_rect)
        zcn = pd(pm(za,zc,is_rad=is_rad),zabc,return_rad=return_rad,return_rect=return_rect)
        return zan,zbn,zcn

    "Convert Y to Delta"
    @staticmethod
    def y2d(z1,z2,z3,is_rad=False,return_rect=False,return_rad=False):

        z123 = ps(pm(z1,z2,is_rad=is_rad),pm(z2,z3,is_rad=is_rad),pm(z1,z3,is_rad=is_rad))
        za = pd(z123,z1,return_rect=return_rect,return_rad=return_rad)
        zb = pd(z123,z2,return_rect=return_rect,return_rad=return_rad)
        zc = pd(z123,z3,return_rect=return_rect,return_rad=return_rad)
        return za,zb,zc

    "Power factor correction"
    @staticmethod
    def pfc(q=0,p=0,fp=0.1,fpn=0.1,il=None,vl=None):

        phi1 = acos(fp)
        phi2 = acos(fpn)
        if vl is None or il is None:
            Qafter = q-tan(phi2)*p
        else:
            Qafter = (3**0.5)*vl*il*sin(phi1)-tan(phi2)*p   
        return Qafter

    "Neutral current and line currents"
    @staticmethod
    def inN(van,vbn,vcn,zla,zlb,zlc,zan,zbn,zcn,znn,return_rad=False,return_rect=False,wires=4,line_currents=False):
        
        if wires==4:
            num = ps(pd(van,ps(zla,zan)),pd(vbn,ps(zlb,zbn)),pd(vcn,ps(zlc,zcn)))
            den = ps(1,pd(znn,ps(zla,zan)),pd(znn,ps(zlb,zbn)),pd(znn,ps(zlc,zcn)))
            inn = pd(num,den,return_rad=return_rad,return_rect=return_rect)
        if line_currents:
            iaa = pd(ps(van,pm(-1,znn,inn)),ps(zla,zan))
            ibb = pd(ps(vbn,pm(-1,znn,inn)),ps(zlb,zbn))
            icc = pd(ps(vcn,pm(-1,znn,inn)),ps(zlc,zcn))
            return inn,iaa,ibb,icc
        else:
            return inn


a = (1,120)
alf = (3**0.5,30)
alf2 = (3**0.5,-30)
pos_seq = [1,pm(a,a),a]
neg_seq = [1,a,pm(a,a)]