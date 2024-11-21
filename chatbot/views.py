from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
 
import json
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

 
 #Configuração do chatbot
chatbot = ChatBot('DjangoBot')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.portuguese')



 
# O dicionário de etapas da conversa
etapas_conversa = {
    'inicio': {
        'pergunta': "Olá! Bem-vindo ao sistema de artigos. Como posso te ajudar hoje?",
        'opcoes': {
            '1': "Buscar Artigos",
            '2': "Criar Artigo",
            '3': "Listar Artigos",
            '4': "Dúvidas sobre o Sistema",
            '5': "Sair"
        },
        'proxima_etapa': {
            '1': 'buscar_artigos', '2': 'criar_artigo', '3': 'listar_artigos', '4': 'duvidas', '5': 'encerrar'
        }
    },
    'buscar_artigos': {
        'pergunta': "Digite uma palavra-chave para buscar artigos:",
        'opcoes': {},
        'proxima_etapa': {
            'sair': 'inicio'
        }
    },
    'criar_artigo': {
        'pergunta': "Vamos criar um novo artigo! Por favor, me diga o título do artigo:",
        'opcoes': {},
        'proxima_etapa': {
            'titulo': 'definir_conteudo'
        }
    },
    'definir_conteudo': {
        'pergunta': "Ótimo! Agora, insira o conteúdo do artigo:",
        'opcoes': {},
        'proxima_etapa': {
            'conteudo': 'escolher_categoria'
        }
    },
    'escolher_categoria': {
        'pergunta': "Agora, qual a categoria do artigo?",
        'opcoes': {
            '1': "Tecnologia",
            '2': "Saúde",
            '3': "Educação",
            '4': "Negócios"
        },
        'proxima_etapa': {
            '1': 'finalizar_artigo', '2': 'finalizar_artigo', '3': 'finalizar_artigo', '4': 'finalizar_artigo'
        }
    },
    'finalizar_artigo': {
        'pergunta': "O artigo foi criado com sucesso! Você deseja salvar ou adicionar outro artigo?",
        'opcoes': {
            '1': "Salvar Artigo",
            '2': "Criar Novo Artigo"
        },
        'proxima_etapa': {
            '1': 'inicio', '2': 'criar_artigo'
        }
    },
    'listar_artigos': {
        'pergunta': "Aqui estão os artigos disponíveis. Deseja ver mais detalhes de algum?",
        'opcoes': {},
        'proxima_etapa': {
            'sair': 'inicio'
        }
    },
    'duvidas': {
        'pergunta': "Como posso te ajudar com dúvidas sobre o sistema?",
        'opcoes': {},
        'proxima_etapa': {
            'sair': 'inicio'
        }
    },
    'encerrar': {
        'pergunta': "Obrigado por usar o sistema de artigos. Até logo!",
        'opcoes': {},
        'proxima_etapa': {}
    }
}

# Função para obter a próxima etapa com base na resposta do usuário
def obter_proxima_etapa(etapa_atual, resposta):
    if resposta in etapas_conversa[etapa_atual]['proxima_etapa']:
        return etapas_conversa[etapa_atual]['proxima_etapa'][resposta]
    return etapa_atual  # Se a resposta não for válida, fica na mesma etapa

 


# View para renderizar o template HTML
def chatbot_page(request):
    return render(request, 'chatbot.html')   

# View para a API do chatbot (responde às mensagens do usuário)
#( # Isso é necessário para permitir requisições POST de fontes externas (como Postman))

@csrf_exempt
def chatbot_view(request):
    if request.method == 'POST':
        # Obtendo os dados enviados via POST
        data = json.loads(request.body)
        etapa_atual = data.get('etapa_atual')
        resposta = data.get('resposta')

        # Verificando se a etapa e a resposta existem
        if etapa_atual in etapas_conversa:
            etapa = etapas_conversa[etapa_atual]
            proxima_etapa = etapa['proxima_etapa'].get(resposta)
            
            if proxima_etapa:
                # Se houver uma próxima etapa, vamos passar para ela
                proxima_pergunta = etapas_conversa[proxima_etapa]['pergunta']
                opcoes = etapas_conversa[proxima_etapa].get('opcoes', {})
                
                return JsonResponse({
                    'pergunta': proxima_pergunta,
                    'opcoes': opcoes,
                    'etapa': proxima_etapa
                })
            else:
                # Se a resposta não for válida ou não houver uma próxima etapa, voltar para a etapa atual
                return JsonResponse({
                    'pergunta': etapa['pergunta'],
                    'opcoes': etapa['opcoes'],
                    'etapa': etapa_atual
                })
        
        return JsonResponse({'pergunta': 'Desculpe, não entendi.', 'opcoes': {}, 'etapa': etapa_atual})
    
    return JsonResponse({'pergunta': 'Método não suportado.', 'opcoes': {}, 'etapa': 'inicio'})









