
from django.shortcuts import render
from django.views import View
from sgucretreat import settings
from django.core.mail import EmailMessage
from django.http import HttpResponse


class HomeView(View):
    template_name = 'app/index.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        SUBJECT = 'Question'
        SENDER = 'A patricipant'
        BODY = request.POST.get('message')

        TO_MAIL = ['elokai@st.ug.edu.gh','ernest6175@gmail.com']

        to_be_sent = EmailMessage(SUBJECT,BODY, settings.EMAIL_HOST, TO_MAIL)
        to_be_sent.send()
        to_be_sent.fail_silently = False
        
        return HttpResponse('<h1>Mail Successfully!</h1>')
