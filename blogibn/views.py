from django.shortcuts import render
from .models import Publicacao
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PubForm
from django.shortcuts import redirect

# Create your views here.

def post_list(request):
        posts = Publicacao.objects.filter(data_publicacao__lte=timezone.now()).order_by('data_publicacao')
        return render(request, 'blogibn/lista_publicacao.html', {'posts': posts})


def post_new(request):
    if request.method == "POST":
        form = PubForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.data_publicacao = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PubForm()
    return render(request, 'blogibn/post_edit.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Publicacao, pk=pk)
    return render(request, 'blogibn/post_detail.html', {'post': post})

def post_edit(request, pk):
    post = get_object_or_404(Publicacao, pk=pk)
    if request.method == "POST":
        form = PubForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.data_publicacao = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PubForm(instance=post)
    return render(request, 'blogibn/post_edit.html', {'form': form})