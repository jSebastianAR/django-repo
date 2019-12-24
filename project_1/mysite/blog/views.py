from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import get_list_or_404, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

# Create your views here.

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	print(render(request,'blog/post_list.html',{'posts':posts}))
	print(request)
	return render(request,'blog/post_list.html',{'posts':posts})

def post_detail(request,pk):
	post = get_object_or_404(Post,pk=pk)
	return render(request,'blog/post_detail.html',{'post':post})

def post_new(request):
	form = PostForm(request.POST)

	if form.is_valid(): #si el formulario ha sido llenado para ingresar nuevos datos
		print("Hello")
		post = form.save(commit=False) #False Porque debemos agregar primero el autor antes de guardar
		post.author = request.user
		post.published_date = timezone.now()
		post.save()
		return redirect('post_detail',pk=post.pk)
	else:
		form = PostForm()
	return render(request,'blog/post_edit.html',{'form':form})	

def post_edit(request,pk):
	post = get_object_or_404(Post,pk=pk)
	if request.method=='POST':
		form = PostForm(request.POST,instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author=request.user
			post.published_date = timezone.now()
			post.save()
			redirect('post_detail',pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request,'blog/post_edit.html',{'form':form})







