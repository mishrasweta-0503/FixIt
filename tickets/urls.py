from django.urls import path,include
from django.contrib.auth import views as auth_views
from .views import DashboardView,TicketCreateView,TicketUpdateView, SignUpView,TicketDeleteView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('ticket/new/', TicketCreateView.as_view(), name='ticket-create'),
    path('ticket/<int:pk>/status/', TicketUpdateView.as_view(), name='ticket-update'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('ticket/<int:pk>/edit/', TicketUpdateView.as_view(), name='ticket_edit'),
    path('ticket/<int:pk>/delete/', TicketDeleteView.as_view(), name='ticket_delete'),
]