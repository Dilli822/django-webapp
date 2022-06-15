
from django.urls import path

from .views import (create_user_info, delete_user_info,
 detail_view_of_users, list_all_user, update_user_info )


app_name = 'crud'
urlpatterns = [
    # crud/list/
    # {% url 'crud' /list %}
    path('list/', list_all_user,  name='list'),
    # capturing value
    path('detail/<int:user_id>/', detail_view_of_users, name='detail'),
    path('create/', create_user_info, name='create'),
    path('update/<int:user_id>/', update_user_info, name='update'),
    path('delete/<int:user_id>/', delete_user_info, name='delete')
    
]