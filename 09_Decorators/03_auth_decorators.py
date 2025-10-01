from functools import wraps


def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("Access Denied : Admins Only")
        else:
            return func(user_role)

    return wrapper


@require_admin
def access_tea_inventory():
    print("Access granted to Tea Invntory")


access_tea_inventory("user")
access_tea_inventory("admin")
