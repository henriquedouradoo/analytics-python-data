# -*- coding: utf-8 -*-
"""module_2_exercise.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SJ07dixIfHObcy6Q8B24ToVPTFfAKF1X

<img src="https://raw.githubusercontent.com/andre-marcos-perez/ebac-course-utils/main/media/logo/newebac_logo_black_half.png" alt="ebac-logo">

---

# **Módulo** | Python: Estruturas de Dados
Caderno de **Exercícios**<br>
Professor [André Perez](https://www.linkedin.com/in/andremarcosperez/)

---

# **Tópicos**

<ol type="1">
  <li>Listas;</li>
  <li>Conjuntos;</li>
  <li>Dicionários.</li>
</ol>

---

# **Exercícios**

## 1\. Listas

Criei uma lista chamada `filmes` com o nome dos 10 primeiros filmes mais bem avaliados no site no [IMDB](https://www.imdb.com/chart/top/). Imprima o resultado.
"""

filmes = ['O Poderoso Chefão',
          'Homem Aranha',
          'Batman',
          'Vingadores',
          'Clube da Luta',
          'Cruella' ]

print(filmes)

"""Simule a movimentação do *ranking*. Utilize os métodos `insert` e `pop` para trocar a posição do primeiro e do segundo filme da lista. Imprima o resultado.

---
"""

print(filmes)

filmes.pop(0)
filmes.insert(1, 'O Poderoso Chefão')

print(filmes)

"""## 2\. Conjuntos

Aconteceu um erro no seu *ranking*. Simule a duplicação dos três últimos filmes da lista. Imprima o resultado.
"""

filmes = ['O Poderoso Chefão',
          'Homem Aranha',
          'Batman',
          'Vingadores',
          'Clube da Luta',
          'Clube da Luta',
          'Cruella',
          'Cruella',]

print(filmes)
print(type(filmes))

"""Utiliza a conversão `set` e `list` para remover os valores duplicados. Imprima o resultado."""

filmes = list(set(filmes))
print(filmes)

"""---

## 3\. Dicionários

Repita os exercícios da parte 1 (listas). Os elementos da lista `filmes` devem ser dicionários no seguinte formato: `{'nome': <nome-do-filme>, 'ano': <ano do filme>}, 'sinopse': <sinopse do filme>}`.
"""

filmes = {
'nome': ['O Poderoso Chefão',
           'Homem Aranha',
          'Batman',
          'Vingadores',
          'Clube da Luta',
          'Cruella'],

'ano' : [1974, 2023, 2012, 2019, 2012, 2020],

}

print(filmes)