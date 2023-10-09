from django.shortcuts import render

# Create your views here.
# Milling Machine

# constants
import math
import numpy as np
from django.http import JsonResponse


def transmissibility(F_t, F_o):
    return F_t / F_o

def minimum_frequency_ratio(a,b):

    T = transmissibility(a,b)


    a = T**2
    b = 0
    c = -(1.99*T**2 + 0.01)
    d = 0
    e = T**2 - 1

    coefficients = [a, b, c, d, e]
    roots = np.roots(coefficients)
    positive_real_roots = [root.real for root in roots if root.imag == 0 and root.real > 0]
    r = round( positive_real_roots[0], 4)
    

    return r


def natural_frequency(rpm, r):
  pi = math.pi
  w = ((2* pi * rpm)/60)
  w_n = w/r

  return round(w_n, 2)




def max_amplitude_at_w_n (F_o, m, w_n, d_r):
  x_max = F_o /((m*w_n**2)*2*d_r*(1-d_r**2)**0.5)
  return round( x_max, 4)


def mass_at_decreased_resonant_amplitude(F_o, x_r, w_n, d_r):
  m = F_o/(x_r*w_n**2*2*d_r*(1-d_r**2)**0.5)

  return round(m, 4)


def steady_state_amplitude_at_increased_mass(F_o, m, w_n, r, d_r):
  x = F_o / (m*w_n**2*((1-r**2)**2 + (2*d_r*r)**2)**0.5)
  return round(x, 6)

def isolator_stiffness(m,w_n):
  k = m*w_n**2
  return round(k, 4)

def aero_view(request):
    try:
        rpm = float(request.GET.get('speed'))
        f_o = float(request.GET.get('force'))
        f_t = float(request.GET.get('forcet'))
        m = float(request.GET.get('mass'))
        d_r = float(request.GET.get('damping'))
        x_r = float(request.GET.get('amplitude'))
    except (TypeError, ValueError):
        # Handle the error when input values are None or not convertible to float
        error_response = {
            "error": "Invalid input. Please provide valid values for speed, force, forcet, mass, damping, and amplitude."
        }
        return JsonResponse({"error": error_response})

    try:
              
        T = transmissibility(f_t, f_o)
        R = minimum_frequency_ratio(f_t, f_o)
        Wn = natural_frequency(rpm, R)
        Xmax = max_amplitude_at_w_n(f_o, m, Wn, d_r)
        Mr = mass_at_decreased_resonant_amplitude(f_o, x_r, Wn, d_r)
        X = steady_state_amplitude_at_increased_mass(f_o, Mr, Wn, R, d_r)
        K = isolator_stiffness(Mr, Wn)
        result = {
            "T": T,
            "R": R,
            "Wn": Wn,
            "Xmax": Xmax,
            "Mr": Mr,
            "X": X,
            "K": K
        }

        return JsonResponse({"result": result})
    except ValueError as e:
        error_response = {
            "error": str(e)
        }
        return JsonResponse({"error": error_response})


























# def aero_view(request):
   
#         rpm = float(request.GET.get('speed'))
#         f_o = float(request.GET.get('force'))
#         f_t = float(request.GET.get('forcet'))
#         m = float(request.GET.get('mass'))
#         d_r = float(request.GET.get('damping'))
#         x_r = float(request.GET.get('amplitude'))
        
#         # Print input values
#         print(f"Received parameters: rpm={rpm}, f_o={f_o}, f_t={f_t}, m={m}, d_r={d_r}, x_r={x_r}")
        
  

    
#         T = transmissibility(f_t, f_o)
#         R = minimum_frequency_ratio(f_t, f_o)
#         Wn = natural_frequency(rpm, R)
#         Xmax = max_amplitude_at_w_n(f_o, m, Wn, d_r)
#         Mr = mass_at_decreased_resonant_amplitude(f_o, x_r, Wn, d_r)
#         X = steady_state_amplitude_at_increased_mass(f_o, m, Wn, R, d_r)
#         K = isolator_stiffness(m, Wn)
        
#         # Print intermediate values
#         print(f"T={T}, R={R}, Wn={Wn}, Xmax={Xmax}, Mr={Mr}, X={X}, K={K}")

#         result = {
#             "T": T,
#             "R": R,
#             "Wn": Wn,
#             "Xmax": Xmax,
#             "Mr": Mr,
#             "X": X,
#             "K": K
#         }
        
#         # Print result
#         print(f"Result: {result}")

#         return JsonResponse({"result": result})
    
        



# def aero_view(request):
    
#     try:
#         rpm = float(request.GET.get('speed'))
#         f_o = float(request.GET.get('force'))
#         f_t = float(request.GET.get('forcet'))
#         m = float(request.GET.get('mass'))
#         d_r = float(request.GET.get('damping'))
#         x_r = float(request.GET.get('amplitude'))
#     except (TypeError, ValueError):
     
#         error_response = {
#             "error": "Invalid input. Please provide valid values for speed, force, forcet, mass, damping, and amplitude."
#         }
#         return JsonResponse({"error": error_response})

#     try:
#         T = transmissibility(f_t, f_o)
#         R = minimum_frequency_ratio(f_t, f_o)
#         Wn = natural_frequency(rpm, R)
#         Xmax = max_amplitude_at_w_n(f_o, m, Wn, d_r)
#         Mr = mass_at_decreased_resonant_amplitude(f_o, x_r, Wn, d_r)
#         X = steady_state_amplitude_at_increased_mass(f_o, m, Wn, R, d_r)
#         K = isolator_stiffness(m, Wn)

#         result = {
#             "T": T,
#             "R": R,
#             "Wn": Wn,
#             "Xmax": Xmax,
#             "Mr": Mr,
#             "X": X,
#             "K": K
#         }

#         return JsonResponse({"result": result})
#     except ValueError as e:
        
#         error_response = {
#             "error": str(e)
#         }
#         return JsonResponse({"error": error_response})



# def aero_view(request):
#     result = {
#         "T": 123,
#         "Xmax": 456,
#         "Mr": 789,
#         "X": 1011,
#         "K": 1213
#     }
#     return JsonResponse({"result": result})
















# # views.py
# import numpy as np
# from django.http import JsonResponse

# def calculate_mean(request):
#     # Dummy list of numbers
#     numbers = [2, 5, 7, 10, 15, 20]

#     # Calculate the mean using NumPy
#     mean_value = np.mean(numbers)

#     # Prepare the response data
#     response_data = {
#         'mean': mean_value,
#         'numbers': numbers
#     }

#     # Return the response as JSON
#     return JsonResponse({'result': response_data})
