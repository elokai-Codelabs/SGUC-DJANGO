
from smtplib import SMTPAuthenticationError
from django.shortcuts import render, redirect
from django.views import View
from sgucretreat import settings
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.contrib import messages


class HomeView(View):
    template_name = 'app/index.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        SUBJECT = 'Question'
        SENDER = 'A patricipant'
        BODY = request.POST.get('message')

        TO_MAIL = ['elokai@st.ug.edu.gh',
                   'ernest6175@gmail.com', 'princesamuelpks@gmail.com']

        to_be_sent = EmailMessage(SUBJECT, BODY, settings.EMAIL_HOST, TO_MAIL)
        try:
            to_be_sent.send()
            to_be_sent.fail_silently = False
            messages.success(
                request, 'Your message has been sent successfully')
        except SMTPAuthenticationError:
            messages.error(request, 'Your message could not be sent')
            return redirect('app:home')
        else:
            return redirect('app:home')
