# SGRH - Sistema de Gerenciamento de Recursos Humanos

Este repositório contém o código fonte para um Sistema de Gerenciamento de Recursos Humanos (SGRH). O sistema visa facilitar a gestão de funcionários, incluindo informações pessoais, salários, cargos, departamentos e outras funcionalidades relacionadas a RH.
Um sitema web simples, o objetivo deste projeto foi demonstrar como é feito na prática a ligação das camadas até chegar ao banco de dados. Um exercicio fullstack para compreender cada camada de um sistema web.

## Tecnologias Utilizadas

* Linguagem de Programação: [Python]
* Framework: [Django]
* Banco de Dados: [PostgreSQL]
* Frontend: [HTML,Bootstrap]
* Outras ferramentas: [Git]

## Instalando as Dependências do Projeto

**Etapas para Instalação:**

1. **Clone o Repositório:**
   ```bash
   git clone https://github.com/Benicioslz/SGRH.git
   ```

2. **Navegue até o Diretório do Projeto:**
   ```bash
   cd <nome do diretório do projeto>
   ```

3. **Crie um Ambiente Virtual (Recomendado):**
   - **Windows:**
     ```bash
     python -m venv .venv
     ```
   - **Linux/macOS:**
     ```bash
     python3 -m venv .venv
     ```

4. **Ative o Ambiente Virtual:**
   - **Windows:**
     ```bash
     .venv\Scripts\activate
     ```
   - **Linux/macOS:**
     ```bash
     source .venv/bin/activate
     ```

5. **Instale as Dependências:**
   ```bash
   pip install -r requirements.txt
   ```
6. **Configurar o Banco de Dados para o Sistema: App/settings.py**

  **POSTGRESQL**
   ```bash
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nome_do_banco_de_dados',
        'USER': 'nome_do_usuario',
        'PASSWORD': 'senha_do_usuario',
        'HOST': 'localhost',
        'PORT': '5432',
    }
  }
  ```
  
  **DBSQLITE3**
   ```bash
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
  }
  ```
  
  **MYSQL**
  ```bash
  DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.mysql',
       'NAME': '<nome_do_banco>',
       'USER': '<nome_do_usuario>',
       'PASSWORD': '<senha_do_usuario>',
       'HOST': 'localhost',
       'PORT': '3306',
      }
  }
  ```

## Rodar o projeto

Após instalar as dependências e configurar a comunicação com o banco, aplique as migrations no banco de dados com o comando:
```bash
python manage.py migrate
```

Criar um usuário admin com o comando no terminal:
```bash
python manage.py createsuperuser
```

Agora o projeto já pode ser inicializado com o comando:
```bash
python manage.py runserver
```

Após isso, o sistema estará pronto para ser acessado em:
[http://localhost:8000](http://localhost:8000)
