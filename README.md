# Agenda Medicar

## Backend

Instale a versão 3.x do Python e o Virtualenv:

<ol>
<li>Clone este repositório : git clone https://github.com/DebolaOliver/medicar.git
<li>Vá para o repositório : cd medicar
<li>Crie um ambiente de desenvolvimento : virtualenv --python $( which python3 ) py3;
<li>Instale as dependências : pip install -r requirements.txt;
<li>Crie a base de dados : python manage.py migrate
<li>Suba o servidor : python manage.py runserver
<li>Acesse o programa em 127.0.0.1:8000
</ol>