from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
#2

#Machine attached to the end of a cantilever beam

import math

def stiffness_of_cantilever_beam(E,I,L):
  k = 3*E*I/(L**3)
  return k

def cantilever_beam_view(request):
       
        
       try:  

         
            E = float(request.GET.get('elasticModulus'))
            I= float(request.GET.get('areaMoment'))
            L= float(request.GET.get('cantileverBeamLength'))


            K = stiffness_of_cantilever_beam(E,I,L)
            
            result = {
                 'K': K,
            }
            return JsonResponse({'result': result})
       except(ZeroDivisionError, ValueError, TypeError) as e:
              return JsonResponse({'e': str(e)})
           