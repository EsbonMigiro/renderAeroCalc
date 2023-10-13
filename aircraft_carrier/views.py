from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
# 3
#aircraft landing on ground

def inertial_forces(px, py, w):
    m_ax = px
    m_ay = py-w
    
    return(m_ax, m_ay)


# angular acceletion
def angular_accelation(py, px,Icg):
    o = (py+2.5*px)/(Icg) 
    return o


def time(v, May, w, g):
    ay = May/(w)
    print(ay)
    t = v/(ay*g)
    
    return t


def angular_velocity(O, T):
    ot = O*T
    return ot

def aircraft_carrier_view(request):


    try:

       

        px = float(request.GET.get('horizontalReaction'))
        py = float(request.GET.get('verticleReaction'))
        w  = float(request.GET.get('aircraftWeight'))
        Icg =float(request.GET.get('inertiaMoment'))
        v = float(request.GET.get('verticalVelocity'))
        g = 9.81



        Max = inertial_forces(px, py, w)[0]
        May = inertial_forces(px, py, w)[1]
      

        O = angular_accelation(py, px,Icg)
       

        T = time(v, May, w, g)
        
        Ot = angular_velocity(O, T)
       

        result= {
            "Max": Max,
            "May": May,
            "O": O,
            "T": T,
            "Ot": Ot
        }

       
        return JsonResponse({'result': result})
    except(TypeError, ValueError) as e:
        return JsonResponse({'error': str(e)})
