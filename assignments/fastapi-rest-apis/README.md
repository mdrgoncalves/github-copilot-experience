# 📘 Assignment: Construindo APIs REST com FastAPI

## 🎯 Objetivo

Você aprenderá a construir APIs REST robustas e eficientes usando o framework FastAPI em Python. Ao final dessa tarefa, você compreenderá os conceitos fundamentais de APIs REST, será capaz de criar endpoints HTTP, validar dados de entrada e trabalhar com respostas estruturadas.

## 📝 Tarefas

### 🛠️ Criar uma API REST Básica

#### Description
Desenvolva uma API REST simples usando FastAPI que gerencie uma coleção de livros. A API deve permitir criação, leitura, atualização e exclusão de livros (operações CRUD básicas).

#### Requirements
Completed program should:

- Implementar endpoints HTTP GET, POST, PUT e DELETE
- Validar dados de entrada utilizando modelos Pydantic
- Armazenar dados em uma estrutura em memória (lista ou dicionário)
- Retornar respostas apropriadas com códigos de status HTTP corretos
- Documentação automática gerada pelo FastAPI estar acessível


### 🛠️ Adicionar Validação e Tratamento de Erros

#### Description
Expanda a API anterior adicionando validação robusta de dados e tratamento apropriado de erros. Implementar validações customizadas e retornar mensagens de erro descritivas aos clientes.

#### Requirements
Completed program should:

- Validar tipos de dados e limites (ex: comprimento de strings, valores numéricos)
- Implementar tratamento de exceções com mensagens de erro personalizadas
- Retornar códigos de status HTTP apropriados para diferentes cenários (404, 422, 400, etc)
- Fornecer mensagens de erro claras e úteis aos clientes da API
- Demonstrar casos de uso para validação que falha e é aceita


### 🛠️ Implementar Autenticação Simples

#### Description
Adicione um sistema básico de autenticação à sua API usando tokens. Crie um endpoint de login que retorna um token e proteja endpoints que modificam dados (POST, PUT, DELETE).

#### Requirements
Completed program should:

- Implementar um endpoint de login que valida credenciais
- Gerar tokens de autenticação simples para usuários autenticados
- Proteger endpoints sensíveis exigindo autenticação via token
- Retornar erro 401 Unauthorized para requisições sem autenticação válida
- Documentar o processo de autenticação no código e/ou comments
