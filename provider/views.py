from django.shortcuts import render

import SoftLayer

# Create your views here.

def index(request):
    cl = SoftLayer.Client(
        username='',
        api_key=''
    )

    result = cl['Account'].getObject()
    return render(request, 'provider/index.html', {'result': result})
