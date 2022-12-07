from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .forms import ContactForm
# Create your views here.

def index(request):
    if request.method == "POST":
        form = ContactForm(request.POST)




        if form.is_valid():
            print('the form was valid')
            name = (form.cleaned_data['name'])
            email = (form.cleaned_data['email'])
            content = (form.cleaned_data['content'])

            html = render_to_string('contact/emails/contactform.html', {
                "name":name,
                "content":content,
                "email":email,
            })

            send_mail('Laiškas qMarketing.', content , email ,['gandrulionis1@gmail.com'], html_message=html)

            return redirect('index')
    else:
        form = ContactForm()


    return render(request, 'contact/index.html',{
        'form': form
    }
)