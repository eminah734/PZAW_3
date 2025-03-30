from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
import json
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm

@ensure_csrf_cookie
@require_http_methods(["GET"])
def set_csrf_token(request):
    return JsonResponse({"detail": "CSRF cookie set"})

@csrf_protect
@require_http_methods(['POST'])
def login_view(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
        email = data.get('email')
        password = data.get('password')
        
        if not email or not password:
            return JsonResponse(
                {'success': False, 'message': 'Email and password are required'}, 
                status=400
            )

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'success': True, 'message': 'Login successful'})
        return JsonResponse(
            {'success': False, 'message': 'Invalid credentials'}, 
            status=401
        )
    except json.JSONDecodeError:
        return JsonResponse(
            {'success': False, 'message': 'Invalid JSON'}, 
            status=400
        )

@csrf_protect
@require_http_methods(['POST'])
def logout_view(request):
    logout(request)
    return JsonResponse({'message': 'Logged out successfully'})

@require_http_methods(['GET'])
def user(request):
    if request.user.is_authenticated:
        return JsonResponse({
            'username': request.user.username, 
            'email': request.user.email
        })
    return JsonResponse(
        {'message': 'Not logged in'}, 
        status=401
    )

@csrf_protect
@require_http_methods(['POST'])
def register(request):
    try:
        data = json.loads(request.body.decode("utf-8"))
        form = CreateUserForm(data)
        
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatyczne logowanie po rejestracji
            return JsonResponse({
                'success': True,
                'message': 'User registered successfully',
                'user_id': user.id
            }, status=201)
        else:
            # Uproszczona forma błędów
            errors = {field: error[0] for field, error in form.errors.items()}
            return JsonResponse({
                'success': False,
                'message': 'Registration failed',
                'errors': errors
            }, status=400)
            
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'message': 'Invalid JSON'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': str(e)
        }, status=500)