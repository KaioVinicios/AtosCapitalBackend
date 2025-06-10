# 🚀 Como iniciar este projeto Django localmente

Este guia explica passo a passo como configurar e rodar este projeto Django em ambiente local.

---

## 🧰 Pré-requisitos

* [Python 3.10+](https://www.python.org/downloads/)
* [Git](https://git-scm.com/)
* Editor de código (recomendado: [VS Code](https://code.visualstudio.com/))

---

## ⚙️ Passo a passo

### 1. Clone o repositório

```bash
git clone https://github.com/KaioVinicios/AtosCapitalBackend
cd AtosCapitalBackend
```

### 2. Crie o ambiente virtual

```bash
python -m venv .venv
```

### 3. Ative o ambiente virtual

* **Windows:**

  ```bash
  .venv\Scripts\activate
  ```

* **Mac/Linux:**

  ```bash
  source .venv/bin/activate
  ```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto seguindo o .env_exemple:

*⚠️ Altere os valores conforme sua configuração local.*

### 6. Rode as migrações do banco de dados

```bash
python manage.py migrate
```

### 7. Crie um superusuário (opcional)

```bash
python manage.py createsuperuser
```

### 8. Inicie o servidor local

```bash
python manage.py runserver
```

---

## ✅ Acesse a aplicação

Abra o navegador e vá até: [http://127.0.0.1:8000](http://127.0.0.1:8000)
