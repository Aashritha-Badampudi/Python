is_logged_in = False

def login_required(func):
    def wrapper():
        if is_logged_in:
            func()
        else:
            print("Access Denied")
    return wrapper

@login_required
def dashboard():
    print("Welcome to dashboard")

dashboard()