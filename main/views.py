from django.shortcuts import render, redirect
from .models import About, Skill, Contact
from projects.models import Project
from blog.models import Post
from .forms import ContactForm

def home(request):
    about = About.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()[:3]
    posts = Post.objects.filter(is_published=True)[:3]

    context = {
        'about': about,
        'skills': skills,
        'projects': projects,
        'posts': posts,
    }
    return render(request, 'main/home.html', context)

def about(request):
    about = About.objects.first()
    skills = Skill.objects.all()
    return render(request, 'main/about.html', {'about': about, 'skills': skills})

def contact(request):
    about = About.objects.first()  # ← qo'shildi
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form': form, 'about': about})  # ← about qo'shildi