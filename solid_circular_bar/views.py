from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

#2
# a solid circular bar
# principal stresses 
import math
pi = math.pi
def principal_strain_one(e_a, e_c, e_b):
    r = ((e_a - e_b) ** 2 + (e_c - e_b) ** 2) ** 0.5
    e_i = ((e_a + e_c) / 2) + (1 / (2 ** 0.5)) * r
    e_ii = ((e_a + e_c) / 2) - (1 / (2 ** 0.5)) * r
    return e_i, e_ii


# principal stresses

def principal_stresses(E, Ei, Eii, v):
    s_i = (E/(1-v**2))*(Ei + v*Eii)
    s_ii = (E/(1-v**2))*(Eii + v*Ei)
    
    return (s_i, s_ii)


# direct stress

def direct_stress(Si, Sii):
    s_d = Si + Sii
    return s_d


def axial_load(d, Sd):
    pi = math.pi
    p = (pi*d**2/4)*Sd
    return p


def shear_stress(Si, Sd):
    s_s = (((2*Si-Sd)**2 - Sd**2)/4)**0.5
    return s_s


# Torque

def torque(Ss, d):
    t = (Ss*pi*d**4/16)/d
    return(t)

def solid_circular_bar_view(request):
          
      
    try:
       
        e_a = float(request.GET.get('strainA'))
        e_b = float(request.GET.get('StrainB'))
        e_c = float(request.GET.get('StainC'))
        v   = float(request.GET.get('poisonRatio'))
        E  = float(request.GET.get('modulusE'))*1e-6
        d = float(request.GET.get('diameter'))




        Ei = principal_strain_one(e_a, e_c, e_b)[0]
        Eii = principal_strain_one(e_a, e_c, e_b)[1]
      

        Si = principal_stresses(E, Ei, Eii, v)[0]
        Sii = principal_stresses(E, Ei, Eii, v)[1]
       

        Sd = direct_stress(Si, Sii)
        

        P = axial_load(d, Sd)

        Ss = shear_stress(Si, Sd)

        T = torque(Ss, d)

        result = {
            "Ei": Ei,
            "Eii": Eii,
            "Si": Si,
            "Sii": Sii,
            "Sd": Sd,
            "P": P,
            "Ss": Ss,
            "T": T
        }
        
        return JsonResponse({"result": result})
    except(TypeError, ValueError, ZeroDivisionError) as e:
        return JsonResponse({'error': str(e)})
