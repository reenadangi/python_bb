"""python_bb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from users import views as user_views
from quotes import views as quotes_views


# Django provides login and logout views 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',user_views.register,name="register"),
    path('signin/', user_views.signin, name="signin"),
    path('signout/',user_views.signout,name="signout"),
    path('editProfile/',user_views.editProfile,name="editProfile"),
    path('edit_user/',user_views.edit_user,name="edit_user"),
    

    path('quotes/',quotes_views.quotes,name="quotes"),
    # path('postmsg/',fbook_views.postmsg,name="postmsg"),  
    path('post_quote/',quotes_views.post_quote,name="post_quote"),  
    path('my_quotes/<int:id>/',quotes_views.my_quotes,name="my_quotes"),  
    path('delete_quote/<int:id>/',quotes_views.delete_quote,name="delete_quote"),
    path('quote_like/<int:id>/',quotes_views.quote_like,name="quote_like"),
    
    
    
]