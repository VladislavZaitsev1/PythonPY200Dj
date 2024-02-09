from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
from app.forms import TemplateForm



# Create your views here.
def my_view(request):
    return render(request, 'landing/index.html')


class MyTemplateView(TemplateView):
    template_name = "landing/index.html"

def post(self, request, **kwargs):
        received_data = request.POST
        form = TemplateForm(received_data)
        if form.is_valid():
            My_name = form.cleaned_data.get("My_name")  # Получили очищенные данные
            My_email = form.cleaned_data.get('My_email')
            My_message = form.cleaned_data.get('My_message')
            data = form.cleaned_data
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]  # Получение IP
            else:
                ip = request.META.get('REMOTE_ADDR')  # Получение IP

            user_agent = request.META.get('HTTP_USER_AGENT')
            data['ip'] = ip
            data['user_agent'] = user_agent

            return JsonResponse(data, json_dumps_params={'indent': 4, 'ensure_ascii': False})
        context = self.get_context_data(**kwargs)  # Получаем контекст, если он есть
        context["form"] = form  # Записываем в контекст форму
        return self.render_to_response(context)  # Возвращаем вызов метода render_to_response
