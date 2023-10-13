from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

# 5
# thin disk

def max_dispacement(p,k):
    x=2*p/k
    return  x


def angular_acceleration(p,k,x,m,r):
    a = 2*(p-k*x)/(3*m*r)
    return a


def is_no_slip_assumption(p, m, r, u, g):
    e = (2*p)/(3*m*r)
    f = m*r*e/2
    f_r = u*m*g  
    
    return (f'force = {f} and Friction force = {f_r}')

def thin_disk_view(request):

    try:
        p = 15
        k = 3000
        x = 0.01
        m = 6
        r = 0.3
        u = 0.1
        g = 9.81


        Xmax = max_dispacement(p,k)

        A  = angular_acceleration(p,k,x,m,r)


        NSA = is_no_slip_assumption(p, m, r, u, g)

        result = {
             'Xmax': Xmax ,
              'A' : A ,
              'NSA': NSA,
        }

        return JsonResponse({'result': result})
    except(ValueError, TypeError, ZeroDivisionError) as e:
            return JsonResponse({'error': str(e)})

    
