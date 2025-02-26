from django.shortcuts import redirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Exercise
from .forms import AddExerciseForm
from django.urls import reverse_lazy

# Create your views here.
class ListExercises(ListView):
    template_name="toExerciseHtmls/home.html"
    model=Exercise
    context_object_name="exercises"

    def get_queryset(self):
        exercises=Exercise.objects.order_by("-date")
        return exercises
    
    
class SingleDetailExercise(DetailView):
    template_name="toExerciseHtmls/detail.html"
    model=Exercise
    
class AddExercise(CreateView):
    model=Exercise
    form_class=AddExerciseForm
    template_name="toExerciseHtmls/addExercise.html"
    # sin poner reverse_lazy no funciona
    success_url=reverse_lazy('home')
    
    
class UpdateExercise(UpdateView):
    model=Exercise
    form_class=AddExerciseForm
    template_name="toExerciseHtmls/updateExercise.html"
    success_url=reverse_lazy('home')
    
    def form_valid(self, form):
        form.instance.image = self.request.FILES.get("image", form.instance.image)
        return super().form_valid(form)
    
class DeleteExercise(DeleteView):
    model=Exercise
    template_name="toExerciseHtmls/deleteExercise.html"
    success_url=reverse_lazy('home')
    
class Favorites(ListView):
    template_name = "toExerciseHtmls/favorites.html"
    model = Exercise
    context_object_name = "exercises"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        favorite_ids = self.request.session.get("favorites", []) 
        context["favorites"] = Exercise.objects.filter(id__in=favorite_ids) 
        return context


    def get_queryset(self):
        exercises=Exercise.objects.order_by("-date")
        return exercises
    
def add_favorite(request,pk):
        favorites=request.session.get("favorites",[])   
        
        if pk not in favorites:
          favorites.append(pk)
        else:
            favorites.remove(pk)
            
        request.session["favorites"]=favorites
        
        return redirect("favorites")