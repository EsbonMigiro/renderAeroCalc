from django.http import JsonResponse
import math
import numpy as np

# 1

# Milling Machine

# constants



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
    r = round( positive_real_roots[0], 2)

    return r


def natural_frequency(rpm, r):
  pi = math.pi
  w = ((2* pi * rpm)/60)
  w_n = w/r

  return round(w_n, 2)




def max_amplitude_at_w_n (F_o, m, w_n, d_r):
  x_max = F_o /((m*w_n**2)*2*d_r*(1-d_r**2)**0.5)
  return round( x_max, 5)



def mass_at_decreased_resonant_amplitude(F_o, x_r, w_n, d_r):
  m = F_o/(x_r*w_n**2*2*d_r*(1-d_r**2)**0.5)

  return round(m, 4)




def steady_state_amplitude_at_increased_mass(F_o, m, w_n, r, d_r):
  x = F_o / (m*w_n**2*((1-r**2)**2 + (2*d_r*r)**2)**0.5)
  return round(x, 6)

def isolator_stiffness(Mr,w_n):
  k = Mr*w_n**2
  return round(k, 4)


def aeroview(request):

  


    try:
        rpm = float(request.GET.get('speedInRPM'))
        f_o = float(request.GET.get('harmonicRepeatedForce'))
        f_t = float(request.GET.get('limitedTranmmitedForce'))
        m = float(request.GET.get('millingMachineMass'))
        d_r = float(request.GET.get('dampingRatio'))
        x_r = float(request.GET.get('amplitudeDuringStartup')) /1000
        print(rpm  ,f_o, f_t ,m ,d_r, x_r )

       

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
    except (TypeError, ValueError) as e:
        return JsonResponse({"error": str(e)})
