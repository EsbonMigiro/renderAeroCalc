from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
#Machine tool mounted on elastic foundation modelled as a spring and viscous damper in parallel
from sympy import symbols, Eq, solve
import math
from django.core import serializers
import json
pi = math.pi

def damping_factor(f,m,x_s,f_m):
    
    d_f = symbols('d_f')
    r_m = ((2*pi*f)**2 * m *x_s)/(f_m)
    equation = Eq(r_m, (1 - 2 * d_f**2) / (2 * d_f * (1 - d_f**2)**0.5))

    roots = solve(equation, d_f)
    positive_real_roots = [root for root in roots if root > 0]
    
    if positive_real_roots:
        solution = round(positive_real_roots[0], 3)
        return solution
    else:
        return "No positive real solutions found."

def natural_frequency(f,Dr):
  w_n = 2*pi*f/(1-2*Dr**2)**0.5
  return round(w_n, 2)


def stiffness_of_the_foundation(m, Wn):
  k = m*Wn**2
  return k 


def damping_coefficient(Dr, m, Wn):
  c=2*Dr*m*Wn
  return c

def machine_tool_view(request):
    try:
        f = float(request.GET.get('frequency'))
        m = float(request.GET.get('mass'))
        x_s = float(request.GET.get('amplitude'))
        f_m = float(request.GET.get('force'))
        print(f, m, x_s, f_m)
        Df = damping_factor(f, m, x_s, f_m)
       
        Wn = natural_frequency(f, Df)
      
        K = stiffness_of_the_foundation(m, Wn)
       
        C = damping_coefficient(Df, m, Wn)
        
        result = {
            "Df": Df,
            "Wn": Wn,
            "K": K,
            "C": C,
        }
        print(result)
        serialized_result = {
            'Df': float(result['Df']),
            'Wn': float(result['Wn']),
            'K': float(result['K']),
            'C': float(result['C'])
        }

        return JsonResponse({'result': serialized_result})
       
        

    except Exception as error:
        return JsonResponse({'error': str(error)})
