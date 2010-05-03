from django.http import HttpResponse
from django.shortcuts import render_to_response
from mysite.books.models import Book
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from mysite.books.forms import ContactForm

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html',
                {'books': books, 'query': q})
    return render_to_response('search_form.html',
	    {'error': error})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'exe.zaid@gmail.com'),
                ['exe.zaid@gmail.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
            initial = {'subject':'I love your site!'}
        )
    return render_to_response('contact_form.html', {'form': form})
