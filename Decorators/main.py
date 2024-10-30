class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

    def is_authenticated_decorator(function):
        def wrapper(*args, **kwargs):
            if args[0].is_logged_in:
                function(args[0])

            else:
                print("You are not logged in")
        return wrapper


    @is_authenticated_decorator
    def post(user):
        print(f"This is {user.name}'s new blog post!")


new_user = User(name="Steven")
new_user.is_logged_in = True
new_user.post(new_user)