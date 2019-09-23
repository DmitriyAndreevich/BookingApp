from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from django.shortcuts import get_object_or_404
from .models import Tour, Post_list




def tour_page(request, id):
    tour = get_object_or_404(Tour, id=id)
    

    return render(request, 'single-package.html', locals())


def blog_page(request):
    posts = Post_list.objects.order_by('-created_date')

    
    return render(request, 'blog-version-one.html', locals())


def post_detail(request, id):
    post = get_object_or_404(Post_list, pk=id)
    return render(request, 'blog-single.html', {'post': post})



def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "email.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')


def index(request):
    return render (request, 'index.html', locals ())



def singlepackage(request):
    return render (request, 'single-package.html', locals ())



def blog(request):
    return render (request, 'blog-version-one.html', locals ())



def contact(request):
    return render (request, 'contact.html', locals ())


