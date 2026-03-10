🗄️ Organizador de Gavetas Virtual

Um pequeno sistema desenvolvido em Python para simular um organizador de gavetas de roupas via terminal.

O programa permite registrar roupas dentro de gavetas específicas e visualizar quais estão ocupadas ou vazias.

É um projeto simples, mas muito útil para praticar conceitos importantes de programação como:

Programação Orientada a Objetos (POO)

Classes e Objetos

Estruturas condicionais

Dicionários

Loops

Interação com o usuário via terminal

📌 Funcionalidades

O sistema possui três funções principais:

👕 Guardar roupa

O usuário pode digitar o nome de uma roupa e escolher em qual gaveta deseja guardá-la.

O sistema verifica se:

a gaveta existe

a gaveta está vazia

ou se já existe uma roupa guardada nela

Caso esteja ocupada, o sistema informa qual peça já está na gaveta.

📊 Ver status das gavetas

Mostra todas as gavetas do sistema com seu estado atual.

Exemplo:

STATUS DAS GAVETAS

Gaveta 9 - Camisa Polo → VAZIA
Gaveta 8 - Bermuda → EM USO | Roupa: Bermuda Jeans
Gaveta 7 - Cueca e Meia → VAZIA
Gaveta 6 - Camisa Social → EM USO | Roupa: Camisa Branca
🚪 Sair do sistema

Finaliza o programa.

🧠 Estrutura do Código

O sistema foi desenvolvido utilizando Programação Orientada a Objetos.

Ele possui duas classes principais:

Classe Gaveta

Representa uma gaveta do organizador.

Atributos:

numero → número identificador da gaveta

tipo → tipo de roupa destinado à gaveta

roupa → peça guardada na gaveta (inicia vazia)

Exemplo de criação de gaveta:

Gaveta("9", "Camisa Polo")
Classe Organizador

Responsável por controlar todas as gavetas.

Ela possui um dicionário de gavetas, onde cada gaveta é armazenada pelo número.

Exemplo:

self.gavetas = {
    "9": Gaveta("9", "Camisa Polo"),
    "8": Gaveta("8", "Bermuda"),
    "7": Gaveta("7", "Cueca e Meia"),
    "6": Gaveta("6", "Camisa Social")
}
⚙️ Métodos do Sistema
guardar_roupa()

Responsável por armazenar uma roupa na gaveta escolhida.

Ele verifica:

Se a gaveta existe

Se ela está vazia

Se estiver vazia:

Camisa Azul guardada na gaveta Camisa Polo

Se estiver ocupada:

A gaveta já está ocupada por Camisa Branca
mostrar_status()

Exibe o estado atual de todas as gavetas.

Mostra:

número da gaveta

tipo de roupa

se está vazia ou em uso

qual roupa está guardada

🖥️ Interface do Programa

O sistema roda em modo terminal e utiliza um menu interativo.

===== MENU =====
1 - Guardar roupa
2 - Ver status das gavetas
3 - Sair

O usuário escolhe uma opção digitando o número correspondente.

🗂️ Estrutura do Projeto
organizador-gavetas/
│
├── organizador.py
└── README.md
▶️ Como executar

1️⃣ Instale o Python (caso não tenha)

https://www.python.org/downloads/

2️⃣ Baixe ou clone o repositório

git clone https://github.com/seuusuario/organizador-gavetas

3️⃣ Execute o programa

python organizador.py
🎯 Objetivo do Projeto

Este projeto foi criado para praticar:

lógica de programação

manipulação de objetos

estrutura de menus em terminal

organização de código em classes

Também serve como exemplo didático de simulação de controle de recursos (gavetas).

🚀 Possíveis melhorias futuras

Algumas evoluções possíveis para o projeto:

remover roupas das gavetas

listar apenas gavetas ocupadas

salvar as roupas em arquivo

interface gráfica

adicionar mais tipos de gavetas

sistema de busca de roupas

👨‍💻 Autor
Sérgio Adriamo Faria
