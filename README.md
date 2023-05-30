# minitwitter

# API README

Este é o README do projeto API, que fornece informações sobre os endpoints disponíveis.

# BaseURL `https://minitwitter.onrender.com/`

## Endpoints da API

### Cadastro - POST

Endpoint para cadastrar um novo usuário.

- **Path:** `api/users`
- **Método:** POST
- **Body:**
  - username: string (obrigatório)
  - email: string (obrigatório)
  - password: string (obrigatório)

### Login - POST

Endpoint para autenticar um usuário.

- **Path:** `api/login`
- **Método:** POST
- **Body:**
  - username: string (obrigatório)
  - password: string (obrigatório)

### Posts - GET

Endpoint para obter todos os posts.

- **Path:** `api/posts`
- **Método:** GET

### Posts - POST

Endpoint para criar um novo post.

- **Path:** `api/posts`
- **Método:** POST
- **Body:**
  - content: string (obrigatório)
  - author: integer (obrigatório)

## Considerações Finais

Esses são os endpoints disponíveis nesta API. Certifique-se de fornecer os dados corretos ao realizar as requisições e utilize os métodos HTTP adequados para interagir com os endpoints. Lembre-se de autenticar-se antes de acessar os endpoints que exigem autenticação.
