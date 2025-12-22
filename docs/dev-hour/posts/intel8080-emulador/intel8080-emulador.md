---
date: 2025-01-01
categories:
    - Emulação
tags:
    - Intel 8080
    - Emulador
    - Assembly
---

# Criando um Emulador de Intel 8080

Recentemente eu apresentei meu TCC voltado para emulação, mais especificamente sobre o CHIP-8. Durante esse processo, me veio a vontade de fazer um de Game Boy também, apenas porque me interessei em todo esse processo de entender as coisas. Com isso, me deparei com a informação que o processador do GameBoy é bastante semelhante com o do Intel 8080. Por isso, irei fazer um deste sistema primeiro e depois seguir para o Gameboy 😁

# O que é o Intel 8080

O Intel 8080 é um microprocessador de 8 bits lançado pela Intel em abril de 1974, considerado o primeiro processador mainstream da empresa e um marco na história da computação. Desenvolvido por Federico Faggin e Masatoshi Shima, o 8080 veio em encapsulamento DIP de 40 pinos e custava US$ 360 inicialmente, impulsionando o mercado de microcomputadores.

> DIP significa Dual In-line Package, e é um nome que damos a um tipo de encapsulamento para circuitos integrados com pinos dispostos em duas fileiras paralelas.

# Arquitetura

O Intel 8080 é um microprocessador composto por cinco partes principais:

1. 7 registradores de propósito geral e 2 específicos.f
2. Memória.
5. Entrada/Saída (I/O).


## Registradores de Propósito Geral

O processador utiliza espaços de armazenamento interno chamados registradores e sinalizadores (flags) para realizar cálculos e tomar decisões. No 8080 eles são:

- **A (Acumulador)**: O registrador mais importante; é onde ocorrem quase todas as operações aritméticas e lógicas.
- **B, C, D, E**: Registradores de uso geral, frequentemente chamados de "scratchpad" para armazenamento temporário.
- **H e L**: Usados principalmente como um par de registradores de 16 bits para apontar para endereços de memória. O H armazena o byte mais significativo (MSB) e o L o menos significativo (LSB).

Além disso, temos dois registradores de controle:

- **Contador de Programa (PC)**: É um registrador de 16 bits que possui o endereço da próxima instrução a ser executada.
- **Ponteiro de Pilha (SP)**: É um registrador de 16 bits que aponta para o topo da "pilha" na memória, usado para sub-rotinas e salvamento de dados.

## Memória

- **Tamanho**: Possui 65 KB de memória, 0x00000 - 0xFFFFF (ou seja, cada endereço possui 16 bits)

### Modos de Endereçamento de Memória

- **Endereçamento Direto**: A instrução fornece o endereço exato da memória
- **Endereçamento por Par de Registradores**: Um registrador contém o endereço. O registrador H contém o byte mais significativo, L contém o byte menos significativo.
- **Endereçamento por Ponteiro de Pilha**: O endereço do ponteiro de pilha é usado. Veja **pop/push** na seção "Ponteiro de Pilha".
- **Endereçamento Imediato**: Carrega o próximo byte (byte após o byte da instrução) no registrador **A**.

## Instruções

O 8080 possui um rico conjunto de instruções que compreende mais de 70 instruções, incluindo transferência de dados, aritmética, operações lógicas e instruções de fluxo de controle. São basicamente 5 tipos de instruções:

- **Movimentação de Dados**: Movem bytes de um local para outro sem alterar seu valor.
- **Aritmético**: Realizam operações matemáticas básicas nos dados armazenados em registradores ou na memória.
- **Lógico**: Executam operações booleanas e manipulações de bits.
- **Desvio ou Controle**: Inclui saltos condicionais e incondicionais, chamadas de sub-rotina e retornos
- **Instruções I/O**: Estas instruções facilitam a comunicação com dispositivos periféricos.

## Outros detalhes

- **Velocidade do clock**: inicialmente oferecia velocidades de 1 MHz, mas as versões posteriores podiam atingir até 3 MHz.