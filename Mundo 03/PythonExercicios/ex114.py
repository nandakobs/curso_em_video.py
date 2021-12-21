"""
# funciona apenas no linux (notebook idosinho com linux tava travando dms mas rodou isso aq de boas)

import requests


def veja_pudim():
    try:
        checar = requests.get('http://www.pudim.com.br/', timeout=5)
        return True
    except requests.ConnectionError:
        print("Pudim indisponivel no momento")
    return False


if veja_pudim():
    print('Pudim acessado com sucesso!')

"""
# Resolução da aula

import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:  # except urllib.error.URLError   porém Python reclama de "error"
    print('O site pudim não está acessível no momento.')
else:
    print('Consegui acessar o site pudim com sucesso.')
    # print(site.read()) # traz o conteudo HTML do site todinho
