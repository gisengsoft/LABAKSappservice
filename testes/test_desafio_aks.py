import pytest
import sys
import os

# Adiciona o diretório pai ao caminho do Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from desafios.desafio_aks import descrever_conceito

def test_descricao_aks():
    assert descrever_conceito("AKS") == "Serviço gerenciado de orquestração de contêineres"

def test_descricao_pod():
    assert descrever_conceito("Pod") == "Unidade mínima de execução em um cluster Kubernetes"

def test_descricao_node():
    assert descrever_conceito("Node") == "Máquina (VM) onde os Pods são executados"

def test_descricao_cluster():
    assert descrever_conceito("Cluster") == "Conjunto de nós que executam aplicações containerizadas"

def test_conceito_desconhecido():
    assert descrever_conceito("Desconhecido") == None