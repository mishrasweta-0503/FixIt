from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Ticket, User, Profile
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import TicketForm, TicketStatusUpdateForm, NewUserCreationForm
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden
from django.core.exceptions import PermissionDenied

# Create your views here.

class DashboardView(LoginRequiredMixin,ListView):
    model = Ticket
    template_name = 'tickets/dashboard.html'
    context_object_name = 'tickets'

    def get_queryset(self):
        # Check if they are a superuser/native staff OR if their custom profile marks them as maintenance staff
        if self.request.user.is_staff or (hasattr(self.request.user, 'profile') and self.request.user.profile.is_staff_member):
            return Ticket.objects.all()
        return Ticket.objects.filter(created_by=self.request.user)
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        tickets_to_count = self.get_queryset()
        data['open_tickets'] = tickets_to_count.filter(status='Open').count()
        data['closed_tickets'] = tickets_to_count.filter(status='Closed').count()
        data['pending_tickets'] = tickets_to_count.filter(status='Pending').count()
        data['resolved_tickets'] = tickets_to_count.filter(status='Resolved').count()

        return data
    
class TicketCreateView(LoginRequiredMixin,CreateView):
   model = Ticket
   form_class = TicketForm
   template_name = 'tickets/ticket_form.html'
   success_url = reverse_lazy('dashboard')

   def form_valid(self, form):
       form.instance.created_by = self.request.user
       return super().form_valid(form)
   
class TicketUpdateView(LoginRequiredMixin,UpdateView):
   model = Ticket
   form_class = TicketStatusUpdateForm
   template_name = 'tickets/ticket_status_form.html'
   success_url = reverse_lazy('dashboard')

   def dispatch(self, request, *args, **kwargs):
       if request.user.is_staff or (hasattr(request.user, 'profile') and request.user.profile.is_staff_member):
           return super().dispatch(request, *args, **kwargs)
       return HttpResponseForbidden("You must be a staff member to update the ticket")
   
class SignUpView(CreateView):
    model = User
    form_class = NewUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

    #form is submitted, validation passed, there is where we save the user in the db and add extra checks
    def form_valid(self, form):
        response = super().form_valid(form) #saves/creates the user in db, returns a redirect response
        user_profile = Profile(user=self.object, is_tenant=True) #django stores the new user inside self.object
        user_profile.save()
        return response
    
class TicketUpdateView(LoginRequiredMixin,UpdateView):
    model = Ticket
    form_class = TicketForm
    template_name = 'registration/ticket_update_form.html'
    success_url = reverse_lazy('dashboard')

    def dispatch(self, request, *args, **kwargs):
        ticket = self.get_object()
        if ticket.created_by != request.user:
            raise PermissionDenied("You do not have access to edit this ticket.")
        return super().dispatch(request, *args, **kwargs)
    
class TicketDeleteView(LoginRequiredMixin,DeleteView):
    model = Ticket
    template_name = 'registration/ticket_confirm_delete.html'
    success_url = reverse_lazy('dashboard')

    def dispatch(self, request, *args, **kwargs):
        ticket = self.get_object()
        if ticket.created_by != request.user:
            raise PermissionDenied("You do not have access to delete this ticket.")
        return super().dispatch(request, *args, **kwargs)

           
       