from django.shortcuts import render, redirect
from django.http import HttpResponse
from openai import OpenAI
# Create your views here.
from dotenv import load_dotenv
import os


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

def saludar(request):
    metodo_usado = request.method
    if request.method == "POST":
        respuesta = request.POST.get('consulta')
        client = OpenAI(api_key= api_key,
                        base_url="https://openrouter.ai/api/v1")
        response = client.chat.completions.create(
            model="deepseek/deepseek-r1:free",
            messages=[{"role": "user", "content": respuesta}],
        )
        iarespuesta = response.choices[0].message.content
        return render(request, "base.html", context={"respuesta": respuesta, "metodo": metodo_usado, "iarespuesta": iarespuesta})
    else:
        return render(request, "base.html")
