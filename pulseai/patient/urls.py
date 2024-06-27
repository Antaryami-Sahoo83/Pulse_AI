from django.urls import path

from patient import views

urlpatterns = [
      # path("form/", views.form_demo)  
      path("signup/", views.signup, name="signup"),
      path("signin/", views.signin, name="signin"), 
      path("signout/", views.signout, name="signout"), 
      path("take-a-test/", views.take_a_test, name="take_a_test"),
      path("appointment/", views.appointment, name="appointment"), 
      path("delete_appointment/<int:aid>/", views.delete_appointment, name="delete_appointment"), 
      path("update_appointment/<int:aid>/", views.update_appointment, name="update_appointment"), 
      path("profile/", views.profile, name="profile"), 
]
