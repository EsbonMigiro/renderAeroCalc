from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
# 5
# a beam 
y_ = 21.6
x_ = 16
Ixx = 1.09e6
Iyy = 1.31e6
Ixy = 0.34e6

y = -66.4
x = -8

def solving_beam_stress(mx):
    I = Ixx*Iyy - Ixy**2
    s = ((mx*(Iyy*y-Ixy*x))/I) 
    return s



def beam_stress_view(request):
    try:
        
        mx = float( request.GET.get('bendingMoment')) * 1000
        S = solving_beam_stress(mx)
        

        result = {
            'S': S,
        }
        return JsonResponse({'result': result})
    except(ValueError, ZeroDivisionError, TypeError) as e:
        return JsonResponse({'error': str(e)})

