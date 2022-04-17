
from smtplib import SMTPAuthenticationError
from django.shortcuts import render, redirect
from django.views import View
from app.models import Question
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

        question = Question.objects.create(
            question_text=BODY,
        )
        question.save()
        messages.success(request, 'Your question has been sent successfully!')
        return redirect('app:home')


class QuestionsListView(View):
    template_name = 'app/questions.html'

    def get(self, request, *args, **kwargs):
        context = {
            'questions': Question.objects.all().order_by('-id')
        }
        return render(request, self.template_name, context)
