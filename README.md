# Canal Cidadão

Projeto feito com Django para organizar informações relacionadas a denúncias da comunidade.

## Funcionalidades

- Cadastro, edição, listagem e remoção de categorias, bairros e usuários.
- Banco de dados SQLite configurado no Django.
- Modelos para denúncias, anexos, notificações e histórico de status.

## Como executar

1. Instale o Python e o Django.
2. Abra o terminal na pasta do projeto.
3. Crie as tabelas do banco de dados:

   ```powershell
   python manage.py migrate
   ```

4. Inicie o servidor:

   ```powershell
   python manage.py runserver
   ```

5. Acesse `http://127.0.0.1:8000/` no navegador.
