# 📘 Assignment: Hangman Game

## 🎯 Objetivo

Você aprenderá a criar um jogo clássico de adivinhação de palavras usando manipulação de strings, loops e entrada do usuário em Python.

## 📝 Tarefas

### 🛠️	Implementar Seleção Aleatória de Palavras

#### Description
Crie um mecanismo para selecionar aleatoriamente uma palavra de uma lista predefinida que será usada como palavra secreta do jogo.

#### Requirements
Completed program should:

- Ter uma lista com pelo menos 10 palavras
- Usar o módulo `random` para selecionar uma palavra aleatória
- Garantir que a palavra selecionada esteja disponível para toda a lógica do jogo


### 🛠️	Gerenciar Tentativas e Progresso do Jogador

#### Description
Implemente a lógica para aceitar palpites de letras, validar se estão corretas e exibir o progresso atual da palavra com letras reveladas e underscores.

#### Requirements
Completed program should:

- Aceitar uma letra como entrada do usuário
- Verificar se a letra está na palavra secreta
- Atualizar a exibição da palavra no formato `_ _ _` com letras acertadas reveladas
- Manter um histórico de letras já adivinhas
- Evitar contar o mesmo palpite duas vezes


### 🛠️	Implementar Lógica de Fim de Jogo

#### Description
Crie a lógica para determinar e comunicar claramente quando o jogo termina, seja por vitória (palavra completa) ou derrota (tentativas esgotadas).

#### Requirements
Completed program should:

- Rastrear o número de tentativas incorretas restantes
- Exibir uma mensagem de vitória quando a palavra for totalmente adivinhada
- Exibir uma mensagem de derrota quando as tentativas se esgotarem, revelando a palavra secreta
- Oferecer a opção de jogar novamente após o término do jogo