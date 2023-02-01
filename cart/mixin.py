from django.shortcuts import redirect
class UserLoginDetail:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("account:register_login")
        else:
            return super(UserLoginDetail, self).dispatch(request, *args, **kwargs)
