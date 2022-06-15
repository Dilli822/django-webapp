

from django.urls import path 

from .views import logout_view, login_view, profile_view, fail_view, signup_view,guest_view
urlpatterns = [
    # accounts/
    path('login/',login_view ),
    path('profile/', profile_view),
    path('fail/', fail_view),
    path('logout/', logout_view),
    path('signup/', signup_view),
    path('guest/', guest_view),
]