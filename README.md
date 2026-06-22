# Contact

Projeto que consome ZAPI ,com finalidade de mandar mensagens ao WhatsApp do destinatário a partir de consultas dentro de um banco da SupaBase

## 🛠 Tecnologias

- Python
- FastApi
- SqlAlchemy
- Async progrmaming
- PostgreSQL

## 📂 Project Structure


```bash
Contact/
├── .venv/
├── Database/
│   ├── __init__.py
│   └── database.py
├── Main/
│   ├── __init__.py
│   └── main.py
├── Model/
│   ├── Entity/
│   │   └── user.py
│   ├── Repository/
│   │   ├── userRepository.py
│   │   └── __init__.py
├── Routes/
│   ├── __init__.py
│   └── routes.py
├── Schema/
│   ├── __init__.py
│   └── userDTO.py
├── Services/
│   ├── Exceptions/
│   │   └── userException.py
│   ├── __init__.py
│   ├── userService.py
│   └── userZAPIService.py
```

## 🛢️ Tabela
  ```bash
TABELA USER
      ----------------------
       ID | NOME | TELEFONE
      ----------------------
```
  

## 📂 Instalação

```bash
pip install -r requirements.txt
```

## ▶️ Running the project

### 1. Ativar ambiente virtual

```bash
source venv/bin/activate
```

### 2. Start server

```bash
fastapi dev Main/main.py
```

### 3. Abrir documentação

```bash
http://127.0.0.1:8000/docs
```

## ❗ Atenção

Crie um arquivo .env que deve ser colocado exatamente o seguinte nome de variáveis de ambientes
```bash
SUPABASE_URL=postgresql+asyncpg://postgres.yktdnqmhqkpvssfsuxkq:[SUA_SENHA]@aws-1-us-west-2.pooler.supabase.com:5432/postgres
ZAPITOKEN=SEU_TOKEN
ZAPIID=SEU_ID
ZAPICTOKEN=SEU_TOKEN_DE_SEGURANÇA

Ex:
SUPABASE_URL=postgresql+asyncpg://postgres.yktdnqmhqkpvssfsuxkq:111111111111@aws-1-us-west-2.pooler.supabase.com:5432/postgres
ZAPITOKEN=abc
ZAPIID=ab42
ZAPICTOKEN=FgkU54
```
Essas váriaveis podem obtidas por meio do site SUPABASE e ZAPI

## 🔎 Observação

Connection Method dentro do seu database deve está marcado 'Session pooler' para conexões IPv6

Para conexões IPv4 deve está marcado 'Direct connection' e o link para acessar o database dever ser

```bash
SUPABASE_URL=postgresql://postgres:[SUA_SENHA]@db.yktdnqmhqkpvssfsuxkq.supabase.co:5432/postgres

Ex: postgresql://postgres:1111111111@db.yktdnqmhqkpvssfsuxkq.supabase.co:5432/postgres
```
