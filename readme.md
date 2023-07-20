Meu primeiro projeto em Python, uma calculadora para computador com as operações de multiplicar, dividir, somar e subtrair, com botões clicáveis e um visor de cálculo, utilizando Tkinter.

O projeto consiste nas seguintes funções:

1. Click(num): esta função recebe um parâmetro numérico. Ele primeiro converte o número para string e, em seguida, a função anexa a string (a “op”) e exibe o valor final de “op” na área de entrada da calculadora.

2. evaluate(): Esta função é executada toda vez que o usuário clica em “=”, ou seja, quando precisamos calcular a equação. Eval () é uma função embutida em python que recebe um argumento de string (equação) e retorna uma string (a saída da equação). Portanto, esta função apenas chama o método “eval” e exibe a saída.

3. clearDisplay(): Essa função limpa a área de entrada.

“C” chama ‘clearDisplay()’.

“=“ chama ‘evaluate ()’

Os demais botões chamam ‘click()’ quando clicados.
