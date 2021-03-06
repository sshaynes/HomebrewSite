from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url

from django.contrib import admin
from HomebrewSite.views.auth.LoginView import LoginView
from HomebrewSite.views.auth.IsSessionActiveView import IsSessionActiveView
from HomebrewSite.views.auth.LogoutView import LogoutView
from HomebrewSite.views.auth.PasswordResetView import PasswordResetView
from HomebrewSite.views.user.CreateUserView import CreateUserView
from HomebrewSite.views.user.DeleteUserView import DeleteUserView
from HomebrewSite.views.user.UpdateUserPasswordView import UpdateUserPasswordView
from HomebrewSite.views.user.UpdateUserProfileView import UpdateUserProfileView
from HomebrewSite.views.user.UserAndProfileInfoAPI import UserAndProfileInfoAPI
from HomebrewSite.views.recipes.RecipeView import RecipeView
admin.autodiscover()

urlpatterns = patterns('',
  # Examples:
  # url(r'^$', 'HomebrewSite.views.home', name='home'),
  # url(r'^blog/', include('blog.urls')),

  #index
  url(r'^$', 'HomebrewSite.views.home.index', name="home"),

  #admin
  url(r'^admin/', include(admin.site.urls)),

  # RESTful API
	url(r'^auth/login/$', LoginView.as_view()),
	url(r'^auth/logout/$', LogoutView.as_view()),
	url(r'^auth/passwordReset/$', PasswordResetView.as_view()),
	url(r'^auth/isSessionActive/$', IsSessionActiveView.as_view()),
	url(r'^user/(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/$', CreateUserView.as_view()),
	url(r'^user/$', CreateUserView.as_view()),
	url(r'^user/updatePassword/$', UpdateUserPasswordView.as_view()),
	url(r'^user/updateProfile/$', UpdateUserProfileView.as_view()),
	url(r'^user/info/$', UserAndProfileInfoAPI.as_view()),
	url(r'^recipe/(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/', RecipeView.as_view()),
	url(r'^recipe/$', RecipeView.as_view())
)
