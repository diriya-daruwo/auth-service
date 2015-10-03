from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from auth_api.models import User
from auth_api.utils import json_response


@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        if username is not None and password is not None:
            try:
                user = User.objects.create(username=username,
                                                    password=password)
                return json_response({
                            'token': user.auth_token,
                            'username': user.username
                        })
            except IntegrityError:
                return json_response({'error': 'User Exists'}, status=400)
        else:
            return json_response({'error': 'Invalid Data'}, status=400)
    elif request.method == 'OPTIONS':
        return json_response({})
    else:
        return json_response({
            'error': 'Method not allowed'
        }, status=405)


@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        if username is not None and password is not None:
            user = User.objects.get(username=username, password=password)
            if user is not None:
                return json_response({
                                    'token': user.auth_token,
                                    'username': user.username
                                })
            else:
                return json_response({'error': 'Invalid login'}, status=400)
        else:
            return json_response({'error': 'Invalid Data'}, status=400)
    elif request.method == 'OPTIONS':
        return json_response({})
    else:
        return json_response({
            'error': 'Method not allowed'
        }, status=405)
