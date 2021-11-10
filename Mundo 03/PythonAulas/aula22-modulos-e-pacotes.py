"""
Pro Python todo arquivo .py pode ser um modulo
desde que tenha  funções dentro dele.

Se você importar duas funções com o mesmo nome
from uteis import fatorial, dobro
from frufrus import cores, dobro
O Python realizará o dobro importado por ultimo
no caso, o de frufrus. Por isso é recomendavel
importar o modulo inteiro para não haver questões
de conflito.

>> VANTAGENS DA MODULARIZAÇÃO

    > Organização do código.< Perceba que quando
    a gente modulariza a gente divide o código,
    a gente divide um problema maior em problemas
    menores.
    > Facilita na manutenção.< Caso alguma função
    pare de funcionar ou caso você pense numa
    solução melhor pra ela. É só, por exemplo,
    você entrar no módulo uteis e alterar a função.
    Todos os projetos e locais que eu utilizar essa
    função vão se beneficiar dessa nova versão da função.
    > Ocultação de código detalhado.<
    > Reutilização em outros projetos.<

Quando um módulo fica muito grande, ou você fica
com muitos módulos, a solução é pacotes.
Em outras linguagens de programação isso se chama
bibliotecas, mas no Python se chama pacotes.

Exemplo, se dentro de uteis.py eu tiver muitas
mas muitas funções mesmo?  módulo uteis vai ficar
muito sobrecarregado e isso vai acabar dificultando
a minha legibilidade, a manutenção e a gente
acabou jogando o problema pra frente/ com a barriga.

Pois além de criar varios módulos, podemos unir
esses módulos e separa-los por assunto em um
>> PACOTE <<
como se fosse uma pasta organizada com varias pastas.
Pra chamar um pacote:
import uteis
pra chamar um assunto especifico do pacote:
from uteis import datas  #sendo datas um assunto q contem varias funções que tratam datas

COMO CRIAR UM PACOTE?
Todo arquivo .py pode ser um modulo,
e toda pasta pode ser considerada um pacote.

Existe um sintaxe pra nomes de arquivos dentro
de pacotes, inclusive um arquivo especial que
tem de aparecer em cada pasta, sendo a principal
ou as subpastas.
__init__.py
No PyCharm ele é criado automaticamente
New > Python Package

"""
