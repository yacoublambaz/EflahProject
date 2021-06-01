from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticatedUser(viewFunc):
    def wrapperFunc(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return viewFunc(request,*args,**kwargs)
    return wrapperFunc


def allowedUsers(allowed_roles = []):
    def decorator(viewFunc):
        def wrapperFunc(request,*args,**kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            
            if group in allowed_roles:
                return viewFunc(request,*args,**kwargs)

            else:
                return HttpResponse("You are not authorized to view this page")
        return wrapperFunc
    return decorator