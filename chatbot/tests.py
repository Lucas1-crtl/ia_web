from django.urls import reverse 
from django.test import Client
import pytest 
from.views import gerar_resposta
import random



def teste_index_url():  # Teste de URL para testar ROTA
    assert reverse('index') == '/'
# teste da url do meu projeto;


@pytest.mark.django_db    #Teste de Requisição
def teste_index():
    client = Client()
    reponse = client.get(reverse('index'))
    assert reponse.status_code == 200
    #teste de requisição usando 'Client'

''''
def teste_gerar_resposta(): #Teste de Integração 1 forma (mais divertida)
   resposta = gerar_resposta("oi")
   assert resposta in [ "E aí! Em que posso ajudar?"
                        "Olá! Como posso ajudar?"
                        "Oi! Manda sua dúvida."
                
                
   ]    
'''

def teste_gerar_resposta(): #Teste de Integração 2 forma fixada (fixa a resposta que você escolher)
    random.seed(3)
    resposta = gerar_resposta("oi")
    assert resposta == "E aí! Em que posso ajudar?"
    

'''
def teste_saudacao():
    resposta = gerar_resposta("oi")
    respostas_validas = [
                "Olá! Como posso ajudar?",
                "Oi! Manda sua dúvida.",
                "E aí! Em que posso ajudar?"

    ]
    assert resposta in respostas_validas
    '''

# Resto das intenções...
