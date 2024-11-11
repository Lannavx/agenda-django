# 📒 Projeto Agenda

Bem-vindo ao **Projeto Agenda**, um sistema de gerenciamento de contatos desenvolvido em Python e Django! Este projeto foi criado com o objetivo de aprimorar minhas habilidades em desenvolvimento web, oferecendo funcionalidades práticas e uma interface amigável para adicionar, editar e gerenciar contatos.

## ✨ Funcionalidades

- Cadastro, edição e exclusão de contatos
- Upload de imagens para os contatos
- Login e registro de usuários
- Interface responsiva e intuitiva

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **Django 5.1.2**
- **SQLite** para banco de dados
- **Pillow** para manipulação de imagens
- **Faker** para gerar dados fictícios

## 🚀 Como Instalar e Executar o Projeto Localmente

### Pré-requisitos

- Python 3.10 ou superior instalado na sua máquina
- Pip (gerenciador de pacotes do Python)

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/lannavx/agenda-django.git
   ```

2. **Caminhe até a pasta do projetro e crie o ambiente virtual:**

   - **Windows:**
     ```bash
     python -m venv venv
     cd venv\scripts
     activate
     ```

   - **Linux/macOS:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Estando na pasta principal, instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Aplique as migrações do banco de dados:**
   ```bash
   python manage.py migrate
   ```

5. **Opcional - Execute o script para popular as tabelas do BD**
   ```bash
   python utils/create_contacts.py
   ```

6. **Opcional - Crie um superusuário para acessar o painel de administração:**
   ```bash
   python manage.py createsuperuser
   ```   
   Siga as instruções para definir um nome de usuário e senha.

7. **Inicie o servidor local:**
   ```bash
   python manage.py runserver
   ```

8. **Acesse o projeto no navegador:**

   Abra o link [http://127.0.0.1:8000](http://127.0.0.1:8000) para visualizar o sistema em funcionamento.

## 📚 Notas Adicionais

- O banco de dados padrão é o **SQLite**, mas você pode configurar outro banco de dados no arquivo `settings.py`.
- O projeto foi desenvolvido como parte de um curso de Python, com o front-end e o script de população do BD fornecido pelo professor [Luiz Otávio Miranda](https://beacons.ai/otaviomiranda).

## 🤝 Contribuição

Sinta-se à vontade para fazer um fork deste projeto e criar suas próprias funcionalidades. Toda contribuição é bem-vinda!

## 📬 Contato

Qualquer dúvida ou sugestão, fique à vontade para entrar em contato. Este projeto foi feito para fins educacionais, então aproveite e explore o código!
