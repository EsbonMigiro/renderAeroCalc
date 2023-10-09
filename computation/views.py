from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.

# views.py in Django# views.py in Django
def compute_ab(request):
    result = 0

    if request.method == 'GET':
        try:
            a = int(request.GET.get('a', 0))
            b = int(request.GET.get('b', 0))
            result = a + b
        except ValueError:
            # Handle invalid input (non-integer values)
            return JsonResponse({'error': 'Invalid input. Both a and b must be integers.'}, status=400)

    return JsonResponse({'result': result})



from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    status = 'error'
    message = 'Something went wrong! Please try again later'
    if request.GET.get('x'):
        x = int(request.GET['x'])
        y = int(request.GET['y'])
        o = request.GET['o']
        status = 'success'
        if o == 'add':
            message = x + y
        elif o == 'sub':
            message = x - y
        elif o == 'div':
            if y != 0:
                message = x / y
        elif o == 'mul':
            message = x * y
        elif o == 'rem':
            message = x % y
        else:
            status = 'fail'
            message = 'Don\'t waste your time!'
    return JsonResponse({'result': message, 'status': status})
