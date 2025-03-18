from django.shortcuts import render, redirect
from django.http import HttpResponse
from openai import OpenAI
# Create your views here.


def saludar(request):
    metodo_usado = request.method
    if request.method == "POST":
        respuesta = request.POST.get('consulta')
        client = OpenAI(api_key="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",
                        base_url="https://openrouter.ai/api/v1")
        response = client.chat.completions.create(
            model="deepseek/deepseek-r1:free",
            messages=[{"role": "user", "content": respuesta}],
        )
        iarespuesta = response.choices[0].message.content
        return render(request, "base.html", context={"respuesta": respuesta, "metodo": metodo_usado, "iarespuesta": iarespuesta})
    else:
        return render(request, "base.html")
