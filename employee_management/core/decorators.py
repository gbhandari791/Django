from django.contrib import messages
from django.shortcuts import redirect
from functools import wraps

def has_role(roles):
    """
    Custom decorator to allow only users from specific role(s).
    Example: @has_role('Admin') or @has_role(['Admin', 'Manager'])
    """
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            # Check if user is logged in
            if not request.user.is_authenticated:
                messages.error(request, "Please log in to access this page.")
                return redirect('login')

            # Normalize roles to a list (in case a single string is passed)
            if isinstance(roles, str):
                role_list = [roles]
            else:
                role_list = roles

            # Check if user belongs to any of the allowed groups
            if not request.user.groups.filter(name__in=role_list).exists():
                messages.error(request, "Access denied! You don’t have permission to access this page.")
                return redirect(request.META.get('HTTP_REFERER', '/'))

            # Access granted
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator
