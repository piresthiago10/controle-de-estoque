# Controle de Estoque
Simples controle de estoque

django-admin startproject controle_de_estoque . (ponto para não criar sublevel)
python3 manage.py migrate
python3 manage.py makemigrtions
python manage.py createsuperuser --email admin@example.com --username admin
python manage.py startapp produto
python manage.py startapp categoria
python manage.py startapp usuario
python manage.py startapp tipo_usuario
python manage.py startapp estoque_entrada
python manage.py startapp estoque_saida