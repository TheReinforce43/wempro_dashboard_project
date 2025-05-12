from rest_framework.permissions import BasePermission, SAFE_METHODS 



class OrderObjectPermission(BasePermission):
    """
    Custom permission:
    - Admin or Seller: Full access
    - Customer: Only access to their own objects (e.g., orders)
    """

    def has_object_permission(self, request, view, obj):
        user = request.user

        # If user has a single role
        role = user.role  # or adjust this if roles is a list

        if role in ['Admin', 'Seller']:
            return True

        elif role == 'Customer':
            # Allow read access to their own object
            if request.method in SAFE_METHODS and getattr(obj, 'user', None) == user:
                return True
            # Allow write/delete only if the object belongs to them
            if getattr(obj, 'user', None) == user:
                return True

        return False