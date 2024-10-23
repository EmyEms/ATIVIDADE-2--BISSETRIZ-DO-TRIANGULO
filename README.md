

# Projeto: Verificação de Propriedades das Bissetrizes Interna e Externa em Triângulos

Este repositório contém um programa em Python que explora as propriedades das bissetrizes interna e externa em triângulos. O programa calcula a divisão dos lados de um triângulo com base nas proporções geradas pelas bissetrizes e exibe o resultado.

## Objetivo

O objetivo deste projeto é aplicar os conceitos e teoremas das bissetrizes interna e externa em um triângulo, com implementações em Python que realizam cálculos matemáticos para verificar suas propriedades.

### Descrição da Atividade

1. **Bissetriz Interna**: O teorema da bissetriz interna afirma que a bissetriz de um ângulo de um triângulo divide o lado oposto em segmentos proporcionais aos lados adjacentes ao ângulo.
2. **Bissetriz Externa**: O teorema da bissetriz externa afirma que a bissetriz externa de um triângulo divide o lado oposto de forma que a razão entre os segmentos criados seja igual à razão dos outros dois lados do triângulo.

## Parte A – Bissetriz Interna

### Hipótese e Tese

- **Hipótese**: A bissetriz de um ângulo interno divide o lado oposto em partes proporcionais aos lados adjacentes.
- **Tese**: Se \(AD\) é a bissetriz do ângulo \(A\) no triângulo \(ABC\), então:

  \[
  \frac{BD}{DC} = \frac{AB}{AC}
  \]

### Passo a passo

1. **Entrada**: O usuário fornece os lados do triângulo \(AB\), \(AC\) e \(BC\).
2. **Processamento**: A função `bissetriz_interna` calcula a divisão do lado \(BC\) em dois segmentos proporcionais.
3. **Saída**: O programa exibe o resultado da divisão.

---

## Parte B – Bissetriz Externa

### Hipótese e Tese

- **Hipótese**: A bissetriz externa divide o lado oposto em partes proporcionais aos lados adjacentes.
- **Tese**: Se \(AD\) é a bissetriz externa, então a razão entre os segmentos do lado oposto segue a mesma proporção dos lados adjacentes.

### Passo a passo

1. **Entrada**: O usuário fornece os lados do triângulo \(AB\), \(AC\) e \(BC\).
2. **Processamento**: A função `bissetriz_externa` realiza a divisão do lado \(BC\) conforme o teorema da bissetriz externa.
3. **Saída**: O programa exibe o resultado da divisão.

---

## Parte C – Esboço Geométrico no GeoGebra

### Bissetriz Interna e Externa

O esboço geométrico abaixo, feito no GeoGebra, ilustra as propriedades das bissetrizes interna e externa. A divisão dos lados do triângulo foi calculada com base nas proporções estabelecidas pelos teoremas.

[Link para a imagem](https://raw.githubusercontent.com/EmyEms/ATIVIDADE-2--BISSETRIZ-DO-TRIANGULO/refs/heads/main/PRINT.jpeg)

### Link do GeoGebra

Veja as medidas e construções dos triângulos diretamente no GeoGebra:

[Link para o GeoGebra](https://www.geogebra.org/calculator/ejxud2fw)

---

