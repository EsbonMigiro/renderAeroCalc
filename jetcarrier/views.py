from django.shortcuts import render
from django.http  import JsonResponse

# Create your views here.

#4 Aircft Carrier
#Tension on the cable
# oi in degrees
import math

def tension_on_cable(w, a,oi):
    t = (w)*a/(math.cos(math.radians(oi)))
    return t


# load on the struct
def load_struct(w, T, oi, oii):
    r = w + T*math.sin(math.radians(oi))
    p = r/(2*math.cos(math.radians(oii)))
    return p



# solving forces
def forces(T, wi, a, oi ):
    # mi = wi/9.81
    # ai = a*9.81
    n = T +wi*math.sin(math.radians(oi))-wi*a*math.cos(math.radians(oi))
    s = wi*math.cos(math.radians(oi)) + wi*a*math.sin(math.radians(oi))
    return (n, s)


def length_covered(v,a):
    d = v**2/(2*a*9.81)
    return d




def jetcarrier_view(request):


    try:
       
        w= float(request.GET.get('aircraftWeight'))
        a = float(request.GET.get('aircraftDecceleration'))
        oi = 10
        oii =20
        wi= float(request.GET.get('fuselageSectionWeight'))
        print(wi)
        v = float(request.GET.get('touchDownSpeed'))

        T = tension_on_cable(w, a,oi)
      
        P = load_struct(w, T, oi, oii)
       

        N = forces(T, wi, a, oi)[0]
        S = forces(T, wi, a, oi)[1]

      

        D = length_covered(v,a)
        

        result= {
        'T': T,
        'P': P,
        'N': N,
        'S': S,
        'D': D
    }

        return JsonResponse({'result': result})
    except(ValueError, TypeError, ZeroDivisionError) as e:
        return JsonResponse({'error': str(e)})
