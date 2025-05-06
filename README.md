# FastaNexus

Conversor de ficheiros FASTA para o formato NEXUS, com testes unitários.

Este repositório contém um script (`FastaNexus.py`) que converte ficheiros de sequências de DNA no formato FASTA para o formato NEXUS, frequentemente utilizado em análises filogenéticas (como no software PAUP*, MrBayes ou BEAST).

## Estrutura

- `FastaNexus.py`: Script principal que lê um ficheiro FASTA e imprime o conteúdo convertido para o formato NEXUS.
- `UnittestFasNex.py`: Script de testes unitários que valida o correto funcionamento das funções de conversão.

## Como usar

### Executar conversão de FASTA para NEXUS

```bash
python FastaNexus.py caminho/para/o/ficheiro.fasta

#Executar os testes unitários
python UnittestFasNex.py


Motivação
O objetivo deste projeto é facilitar a conversão de formatos de ficheiros biológicos, promovendo a integração com ferramentas de análise filogenética. A automatização da conversão permite uma transição mais rápida e segura entre ferramentas bioinformáticas.
