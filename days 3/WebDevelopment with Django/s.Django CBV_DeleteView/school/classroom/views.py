from django.shortcuts import render
from django.views.generic import TemplateView, FormView,CreateView,ListView,DetailView,UpdateView,DeleteView
from classroom.forms import ContactForm
from classroom.models import Teacher
from django.urls import reverse_lazy


class HomeView(TemplateView):
    template_name = 'classroom/home.html'


class ThankYouView(TemplateView):
    template_name = 'classroom/thank_you.html'
    
class TeacherCreateView(CreateView):
    model=Teacher
    #automaticaly look for teache_form.html
    fields="__all__"
    success_url=reverse_lazy('classroom:thank_you')


class TeacherListView(ListView):
    model = Teacher
    queryset=Teacher.objects.order_by('first_name')
    context_object_name="teacher_list"


class TeacherDetailView(DetailView):
    model = Teacher


class TeacherUpdateView (UpdateView):
    model=Teacher
    fields= "__all__"
    success_url = reverse_lazy('classroom:teacher_list')


class TeacherDeleteView (UpdateView):
    model = Teacher
    success_url = reverse_lazy('classroom:teacher_list')
    
    

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'
    success_url = "/classroom/thank_you"

    def form_valid(self, form):
        # Process the form data here
        print(form.cleaned_data)
        # You can save the form data to the database or perform any other actions here
        return super().form_valid(form)
