import pytest
import sys
import os

# Adiciona o diretório pai ao caminho do Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from desafios.desafio_appservice import descrever_conceito_appservice

def test_descricao_app_service():
    assert descrever_conceito_appservice("App Service") == "Serviço PaaS para hospedar apps na Azure"

def test_descricao_escalabilidade():
    assert descrever_conceito_appservice("Escalabilidade") == "Ajusta recursos automaticamente conforme uso"

def test_descricao_slot_deployment():
    assert descrever_conceito_appservice("Slot de Deployment") == "Ambiente isolado para testes de novas versões"

def test_descricao_cicd():
    assert descrever_conceito_appservice("CI/CD") == "Automatiza build e deploy de aplicações"

def test_conceito_desconhecido():
    assert descrever_conceito_appservice("Desconhecido") == None