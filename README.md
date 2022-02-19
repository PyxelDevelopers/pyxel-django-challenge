# pyxel-django-challenge

Desafio para programador front-end.

## Como enviar?

- Faça um clone do repositório.
- Crie uma branch com nome dev-nome-sobrenome.
- Faça um commit por tarefa.
- Solicite o invite antes de dar push.

## Case

Informações do projeto:

- O sistema é um catálogo de receitas onde o admin pode gerenciar adicionar, excluir, editar e favoritar receitas.
- A plataforma apresenta um sistema simples de login e cadastro de usuários, que podem ser adicionados como autores das receitas.

Rotas: /receitas /admin

Levantamento de requisitos Front-end:

### Obrigatório

- O sistema deve ser responsivo.
- Estilizar cada receita em formato de card.
- A tela de login e registro devem ser estilizados.
- É necessário um rodapé no sistema com nome do desenvolvedor, sempre colado na parte de baixo da tela.
- As receitas em destaque devem ser apresentados em um carousel. (Ao estilo netflix, pode usar lib) (Pelo menos tenta XD)

### Opcional

- Utilizar Bootstrap 5. (Recomendado caso queira facilitar responsividade e componentes como navbar ou modals)
- Animações são mais do que bem-vindas, botões, rolagem, o que achar necessário e sem exagero. (@keyframes ou JS, tanto faz)
- Criar uma landing page na rota "/". (Necessário mexer no back-end)

Caso queira entender melhor o Django, recomendo fazer o [tutorial da documentação]('https://docs.djangoproject.com/en/4.0/intro/tutorial01/').

## Explicando estrutura de uma aplicação Django:

- views.py -> Funções relacionadas a aplicação Django.
- urls.py -> Rotas que carregam cada função da view.
- models.py -> Modelos de banco de dados.
- /templates/nome_da_aplicacao/pages/ -> Possui arquivos de páginas HTML.
- /templates/nome_da_aplicacao/partials/ -> Possui arquivos HTML que representam "partes" de código, estes que podem ser importados pelas pages.
- /base_static/ -> Arquivos estáticos como JS e/ou CSS que são usados por mais de uma aplicação.
- /base_templates/ -> Arquivos HTML que são usados por mais de uma aplicação.

## Como executar o projeto?

- Requisito: Ter python e pip(Se for Windows vem junto ao Python) instalado na máquina e configurado no path.
- Instalar o Django (Se preferir pode usar o ambiente virtual do Python):
```
pip install django
```
- Instalar Pillow para reconhecimento de imagem:
```
pip install pillow
```
- Acessar raiz do projeto e executar:
```
py manage.py runserver
```
- Acessar localhost:8000.

Obs.:

Para acessar uma porta diferente basta adicionar a porta no final do comando, por exemplo, para rodar na porta 3000:
```
py manage.py runserver 3000
```

Qualquer dúvida pode chamar no zap!
