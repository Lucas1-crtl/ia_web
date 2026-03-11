import random
import unicodedata

def normalizar_texto(texto):
    texto = texto.lower()
    texto = unicodedata.normalize('NFD', texto)
    texto = ''.join(c for c in texto if unicodedata.category(c) != 'Mn')
    return texto


def gerar_resposta(pergunta):
    pergunta = normalizar_texto(pergunta)

    intencoes = [
        {
            "nome": "saudacao",
            "palavras_chave": ["oi", "ola", "eai", "bom dia", "boa tarde", "boa noite"],
            "respostas": [
                "Olá! Como posso ajudar?",
                "Oi! Manda sua dúvida.",
                "E aí! Em que posso ajudar?"
            ]
        },
        {
            "nome": "identidade",
            "palavras_chave": ["seu nome", "quem criou voce", "quem e voce"],
            "respostas": [
                "Eu sou sua IA local.",
                "Fui criado por Lucas Schatz.",
                "Sou um chatbot programado em Django."
            ]
        },
        {
            "nome": "programacao",
            "palavras_chave": ["python", "django", "erro", "codigo"],
            "respostas": [
                "Você pode me mostrar o código?",
                "Qual erro está aparecendo?",
                "Me explique melhor o problema."
            ]
        },
        {
            "nome": "curiosidades",
            "palavras_chave": ["brasil", "curiosidades sobre o brasil","portugues","habitantes","Gigante territorial","história", "Cultura"],
            "respostas": [
                "O Brasil abriga a maior comunidade japonesa fora do Japão, com mais de 600 mil pessoas.",
                "A Brasil não tem nome de um deus grego ou romano, ao contrário dos outros planetas.",
                "O Brasil é o 5º maior país do mundo, dono da maior biodiversidade e floresta tropical do planeta.",
                "Com mais de 200 milhões de habitantes, o país abriga a maior comunidade japonesa fora do Japão e possui o maior litoral da América do Sul.",
                "O Rio de Janeiro foi a única capital europeia fora da Europa, servindo como capital de Portugal entre 1808 e 1821.",
                "O país abriga a maior população de origem japonesa fora do Japão."
            ]
        }
    ]

    for intencao in intencoes:
        for palavra in intencao["palavras_chave"]:
            if palavra in pergunta:
                return random.choice(intencao["respostas"])

    return "Ainda não sei responder isso, mas estou aprendendo!"