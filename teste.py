import pytest
from principal import somar 
from principal import subtrair

def teste_somar():
    assert somar(2,4)==6

def teste_subtrair():
    assert subtrair(9,5)==5