from django.http import HttpResponse

# Create your views here.

from .models import Question,Choice

def index(request):
    latest_questionlist = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_questionlist])
    return HttpResponse(output)


