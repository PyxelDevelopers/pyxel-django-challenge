# pyxel-django-challenge

Desafio para programador back-end e front-end.

## Como enviar?

- Faça um clone do repositório.
- Crie uma branch com nome dev-nome-sobrenome.
- Faça um commit por tarefa.
- Faça push de tudo.

## Case (Sistema já funciona 100%, faltando apenas a estilização)

Informações do projeto:

- O sistema é um catálogo de receitas.
- O sistema possui login e cadastro, que também deve ser estilizado.
- Nele é possível cadastrar receitas e selecionar destaques através do painel admin.

Levantamento de requisitos Front-end:

Rotas: GET /receitas, /receitas/:id

- O sistema deve ser responsivo.
- As receitas em destaque devem ser apresentados em um carousel.

Levantamento de requisitos Back-end: (Em breve)

## Explicando estrutura de uma aplicação Django:

- views.py -> Funções relacionadas a aplicação Django.
- urls.py -> Rotas que carregam cada função da view.
- /templates/nome_da_aplicacao/pages/ -> Possui arquivos HTML que serão renderizados na view.py.
- /templates/nome_da_aplicacao/partials/ -> Possui arquivos HTML que representam "partes" de código, estes que podem ser importados pelas pages.
- /static/ -> Arquivos estáticos como JS e/ou CSS.
- /ROOT/base_template/ -> Carrega configurações e partials que podem ser usados por mais de uma aplicação, por exemplo, barra de navegação ou a própria estrutura base do HTML.

## Como executar o projeto?

- Requisito: Ter python e pip(Se for Windows vem junto ao Python) instalado na máquina e configurado no path.
- Instalar o Django (Se preferir pode usar o ambiente virtual do Python):
```
pip install django
```
- Acessar raiz do projeto e executar:
```
py manage.py migrate
py manage.py runserver
```
- Acessar localhost:8000.

Obs.:

Credenciais no /admin:

user: admin - password: admin.