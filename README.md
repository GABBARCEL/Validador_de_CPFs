# ✅ Verificador de CPF

Um projeto simples em Python para validar números de CPF usando o algoritmo oficial de dígitos verificadores.

Este projeto foi feito com o objetivo de treinar:
- lógica de programação
- estruturação de funções
- tratamento de erros
- boas práticas básicas de desenvolvimento

---

## 🚀 Funcionalidades

- Validação de CPF sem formatação
- Verificação de tamanho correto (11 dígitos)
- Detecção de CPFs com todos os dígitos iguais (ex: 11111111111)
- Cálculo automático dos dois dígitos verificadores

---

## 📁 Estrutura do projeto

verificador-cpf/
├── main.py
└── functions.py

yaml
Copiar código

- `main.py` → interface com o usuário
- `functions.py` → lógica de validação do CPF

---

## 📥 Como executar

1. Clone o repositório:
```bash
git clone https://seu-repositorio-aqui
Entre na pasta do projeto:

bash
Copiar código
cd verificador-cpf
Execute o arquivo principal:

bash
Copiar código
python main.py
🧠 Como funciona a validação
O programa:

Verifica se o CPF possui exatamente 11 dígitos

Rejeita CPFs com todos os números iguais

Calcula o primeiro dígito verificador

Calcula o segundo dígito verificador

Compara com os dígitos informados

Se tudo bater, o CPF é considerado válido ✅

💡 Observações
O programa espera que o CPF seja digitado sem pontos ou traços.

Caracteres não numéricos são tratados na entrada.

Projeto feito com fins educacionais.

🧑‍💻 Autor
Desenvolvido por Gabriel Barcelos
