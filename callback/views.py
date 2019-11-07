from django.http import JsonResponse

import time

from .forms import *





def createCallbackForm(request):
    return_dict = {}
    if request.POST:
        form = CallbackOrderForm(request.POST)
        if form.is_valid():

            form.save()
            return_dict['result'] = 'ok'

        else:
            return_dict['result'] = 'error'
            return_dict['errors'] = form.errors
            print(form.errors)
    return JsonResponse(return_dict)