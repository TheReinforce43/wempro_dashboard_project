from rest_framework.permissions import BasePermission, SAFE_METHODS 



class ProductObjectPermission(BasePermission):
  
    """
    Custom permission to allow:
    - Admin: Full access
    - Seller: Only read and update own products (based on user-category relationship)
    - Customer: Read-only access
    
    """
    def has_object_permission(self, request, view, obj):
        user = request.user 

        print(user.roles)
        if user.roles in ['Admin','Seller']:
            return True
        
        # elif user.role == 'Seller':
        #    if request.method in ['GET', 'PUT', 'PATCH','HEAD','OPTIONS']:
        #         # Check if the product belongs to the user's category
        #         return user in  obj.product_category.category_seller.all()
        elif user.roles == 'Customer':
            if request.method in SAFE_METHODS:
                return True
        else:  
            return False