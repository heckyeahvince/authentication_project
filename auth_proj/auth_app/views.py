from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm


def index(request):
    return render(request, 'auth_app/index.html', {})


def signup(request):
    if request.method == "POST":
        user_form = CustomUserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('index')
        else:
            user_form_new = CustomUserCreationForm()
            # error_message_user = user_form.errors.as_json(escape_html=False)
            error_message_user_form = user_form.errors.as_data()
            return render(request, 'registration/create_user.html', {'user_form': user_form_new,
                                                                     'error_message_user': error_message_user_form
                                                                     })
            # return HttpResponse(error_message_user)
    else:
        user_form_new = CustomUserCreationForm()

        return render(request, 'registration/create_user.html', {'user_form': user_form_new})