from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Location, Activity


# Create your views here.
def index(request):

    context = {
        'locations': Location.objects.filter(latitude__gte=1),
        'activities': Activity.objects.all(),
    }

    return render(request, 'theme_app/index.html', context)

def process(request):
    print "in process", request.POST
    print "views", request.POST['name']

    #(True, obj)
    #(False, error_list)
    valid, response = Location.objects.validate_location(request.POST)
    if valid is True:
        request.session.name = response.name
    else:
        for error in response:
            print error
            messages.error(request, error)
    #call a function in Models
    # my_variable = 2
    # what_comes_back = invocation()
    # print type(what_comes_back)
    # print my_variable
    return redirect('/')

def create_activity(request):
    if request.method == 'POST':
        #do our logic
        print request.POST, "<<<<<<---- request.POST"
        valid, response = Activity.objects.validate_activity(request.POST)

        if valid:
            print "woop made it, ", response
            return redirect('/')
        else:
            for error in response:
                messages.error(request, error)


    return redirect('/')