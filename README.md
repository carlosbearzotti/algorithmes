# Algorithmes

Coleção de soluções de algoritmos e experimentos de machine learning em múltiplas linguagens.

## Estrutura

| Diretório | Linguagem | Conteúdo |
|-----------|-----------|----------|
| `C/` | C | FizzBuzz |
| `CSharp/` | C# | FizzBuzz |
| `Java/` | Java | FizzBuzz |
| `php/` | PHP | FizzBuzz, Two Sum |
| `Python/` | Python | FizzBuzz, Two Sum, algoritmos de busca, ML (Gradiente Descendente, KMeans, PCA, XGBoost), desafios HackerRank (Q1-Q6), testes MBI 2025 |
| `LogicaProgramacao/` | Python, PHP, Java | Calculadora de comissão (teste lógico) |

## Algoritmos

- **FizzBuzz** — Implementado em C, C#, Java, PHP e Python
- **Two Sum** — PHP e Python (hash map)
- **Busca Binária/Linear** — Contagem de previsões abaixo de limiares
- **Gradiente Descendente** — Regressão linear do zero
- **Rede Neural 1 neurônio** — Regressão linear com SGD
- **K-Means** — Clustering com scikit-learn
- **PCA** — Redução de dimensionalidade
- **XGBoost** — Classificação com SHAP (credit risk / fraud detection)

## Como usar

```bash
# Python
pip install -r requirements.txt
python Python/fizzBuzz.py

# C
gcc C/fizzBuzz.c -o fizzBuzz && ./fizzBuzz

# Java
javac Java/fizzBuzz/FizzBuzz.java && java Java/fizzBuzz.FizzBuzz

# C#
csc CSharp/fizzBuzz.cs && mono CSharp/fizzBuzz.exe

# PHP
php php/fizzBuzz.php
```
