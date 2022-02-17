# pyxel-django-challenge

Desafio para programador back-end e front-end.

## Como enviar?

- Faça um clone do repositório.
- Crie uma branch com nome dev-nome-sobrenome.
- Faça um commit por tarefa.
- Faça push de tudo.

## Case

Informações do projeto:

- O sistema deve gerenciar receitas em geral.
- Cada receita deve conter nome, modo de preparo, ingredientes, imagem.
- Deve ser possível selecionar receitas para destacar no site.
- O projeto usa arquitetura MTV. (Explicação da estrutura mais abaixo)

Front-end:

Rotas: GET /receitas, /receitas/:id

- [ ] O sistema deve apresentar cada receita em um card.
- [ ] As receitas em destaque, seria interessante colocar em um carousel. (Opcional)
- [ ] Cliente gosta de animações, mas sem exagero.
- [ ] Cliente gostaria de uma landing page, falando um pouco sobre seu blog de receitas. (Necessário configurar view, url e template).

Back-end:

- [ ] Usar paginação para apresentar as receitas.
- [ ] Categorizar receitas e criar rota /receitas/categorias para listar categorias e /receitas/categorias/:categoria para apresentar produtos da categoria.
- [ ] Criar um sistema de cadastro simples e requerir login para acessar blog de receitas.
- [ ] Criar um CRUD personalizado para cadastrar as receitas. (Pode criar uma tela a parte ou personalizar o admin)

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