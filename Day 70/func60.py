def login_required(func):
    def wrapper(username):
        if username == "admin":
            func(username)
        else:
            print("Access Denied")
    return wrapper

@login_required
def dashboard(username):
    print("Welcome", username)

dashboard("admin")