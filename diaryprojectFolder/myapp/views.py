from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Diary, Comment
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.files.storage import FileSystemStorage
from .forms import DiaryForm, CommentForm
from django.contrib.auth.models import User
from django.contrib import auth

def new(request):
    
    if request.method == 'GET':
        form = DiaryForm()
        return render(request, 'new.html', {'form':form})

    else:
        diary = Diary()
        form = DiaryForm(request.POST)
        if form.is_valid():
            diary = form.save(commit=False)
           
            images = request.FILES['image']
            im = FileSystemStorage()
            diary.image = im.save(images.name, images)
            
            diary.writer = request.user

            diary.save()
    
        return redirect('/')

def index(request):
    diary=Diary.objects.all()
    diary_list = Diary.objects.all()
    paginator = Paginator(diary_list, 4)
    page = request.GET.get('page')
    try:
        posts = paginator.get_page(page)
    except PageNotAnInteger:            
        posts = paginator.get_page(1)
    except EmptyPage:
        posts = paginator.get_page(paginator.num_pages)
    return render(request, 'index.html', {'diary':diary, 'posts':posts})

def detail(request, diary_id):
    diary=get_object_or_404(Diary, pk=diary_id)

    return render(request, 'detail.html', {'diary':diary})

def edit(request, diary_id):

    diary = get_object_or_404(Diary, pk=diary_id)

    if request.method == 'GET':
        form = DiaryForm(instance=diary)
        return render(request, 'edit.html', {'form':form})
    
    else:        
        
        form = DiaryForm(request.POST, instance = diary)
        if form.is_valid():
            diary = form.save(commit=False)
            
            images = request.FILES['image']
            im = FileSystemStorage()
            diary.image = im.save(images.name, images)
            
            diary.date = timezone.now() 

            diary.save()
    
        return redirect('/' + str(diary_id))


def delete(request, diary_id):
    diary = get_object_or_404(Diary, pk=diary_id)
    diary.delete()

    return redirect('/')

def signup(request):
    if request.method == 'POST':

        if request.POST['username'] == '' or request.POST['password'] == '':
            return render(request, 'signup.html', {'error':'아이디 비밀번호를 입력하세요'})
        
        if request.POST['password'] != request.POST['con_password']:
            return render(request, 'signup.html', {'error':'비밀번호 불일치'})

        try :
            user = User.objects.get(username = request.POST['username'])
            return render(request, 'signup.html', {'error':'이미 존재하는 이름'})
        except User.DoesNotExist:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            auth.login(request, user)

            return redirect('/')


    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        pw = request.POST['password']

        user = auth.authenticate(request, username = username, password = pw)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error':'아이디, 비밀번호 확인'})

    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

    
def comment_create(request, diary_id):

        if request.method == 'POST':
                diary = get_object_or_404(Diary, pk=diary_id)
                form = CommentForm(request.POST)
                
                if form.is_valid():
                        comment = form.save(commit=False)
                        comment.diary = diary
                        comment.com_writer = request.user

                        comment.save()
                return redirect('/' + str(diary.id))
        else:
                form=CommentForm()
                return render(request, 'detail.html', {'form':form})


def comment_delete(request, diary_id, comment_id):
        diary = get_object_or_404(Diary, pk=diary_id)
        comment = get_object_or_404(Comment, pk=comment_id)

        comment.delete()

        return redirect('/' + str(diary.id))




def comment_edit(request, diary_id, comment_id):

        diary = get_object_or_404(Diary, pk=diary_id)
        comment = get_object_or_404(Comment, pk=comment_id)
        
        if request.method == 'POST':
            form = CommentForm(request.POST, instance=comment) 
            if form.is_valid():
                comment = form.save(commit=False)
                comment.diary = diary
                comment.save()
                return redirect('/' + str(diary_id))
        else:
            form=CommentForm(instance=comment)
            return render(request, 'comment_edit.html', {'form':form})
