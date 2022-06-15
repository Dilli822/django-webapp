from crud.models import UserInfo
# from crud.forms import UserInfoModel
from modelrelation.models import User
from django.shortcuts import render, get_object_or_404, redirect
from .models import UserInfo
from .forms import UserInfoModelForm

# Create your views here.

def list_all_user(request):
    # for storing dynamic data
    data = UserInfo.objects.all()
    # making set data type where we can pick up the data
    context = {
        'data': data
    }

    return render(request, 'crud/list.html', context=context)


# for dob views
def detail_view_of_users(request, user_id):
    # for non existed id and key value pair we can do try catch method
    # user_obj = UserInfo.objects.get(id=user_id)
    # django has shortcut method for error handling and non existed data's request from client
    # with shortcut method 
    user_obj = get_object_or_404(UserInfo, id=user_id)
    # passing in the form of context 
    return render(request, 'crud/details.html',context={
        'user_obj': user_obj
    })


# function/views for creating and allowing users to apply,submit,validate
# and redirect them to users table data

def create_user_info(request):

    if request.method == 'POST':
        #form passess

        # if post method
        form = UserInfoModelForm(request.POST)
        if form.is_valid():

            # printing the data
            print(form.cleaned_data)
            print("form is valid and printed")
            # model form have save method which wilsave form in the db
            form.save()

            # after form validations redirect to
            return redirect('/crud/list/')

        # if form is not passed 
        else:
            print("Form is invalid or not validated,Wrong Input!")
            # [13/Sep/2021 17:03:41] "GET /crud/create/ HTTP/1.1" 200 1268
            #Form is invalid or not validated,Wrong Input!
            # THis will be printed on the server terminal.
    else:
        form = UserInfoModelForm()
        
    return render(request, 'crud/create.html', {
        'form': form
    
    }) 


# views for Update
# update for user_id to know on which user_id to update,create or delete
# padding user id as an param

def update_user_info(request, user_id):
    user_object = get_object_or_404(UserInfo, id=user_id)

    if request.method == 'POST':
        #form passess

        # if post method
        form = UserInfoModelForm(
            request.POST,
            instance = user_object
        )
        
        if form.is_valid():
            # printing the data
            print(form.cleaned_data)
            print("form is valid and printed")
            # model form have save method which wilsave form in the db
            form.save()
            # after form validations redirect to
            return redirect(f'/crud/detail/{user_id}')

        # if form is not passed 
        else:
            print("Form is invalid or not validated,Wrong Input!")
            # [13/Sep/2021 17:03:41] "GET /crud/create/ HTTP/1.1" 200 1268
            #Form is invalid or not validated,Wrong Input!
            # THis will be printed on the server terminal.
    else:
        # pre polluting the user's data as an instance at the update page
        form = UserInfoModelForm(instance = user_object)
    
    return render(request, 'crud/update.html', {
        'form': form
    
    }) 



# for deleting views

def delete_user_info(request, user_id):
    # if request.method == 'POST':
        user_object = get_object_or_404(UserInfo, id=user_id)
        user_object.delete()
        return redirect(f'/crud/list/')

    
    # return redirect(f'/crud/list')



# pre polluting the users data for /crud/update/user_id


