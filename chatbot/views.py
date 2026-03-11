from django.shortcuts import redirect, render
from .services.ia_engine import gerar_resposta

def index(request):

    if "historico" not in request.session:
        request.session["historico"] = []

    historico = request.session["historico"]

    if request.method == "POST":
        pergunta = request.POST.get("pergunta", "")

        if pergunta:
            resposta = gerar_resposta(pergunta)

            historico.append({
                "pergunta": pergunta,
                "resposta": resposta
            })

            request.session["historico"] = historico

    return render(request, "chatbot/index.html", {
        "historico": historico
    })

def limpar_chat(request):
    request.session["historico"] = []
    return redirect("index")

