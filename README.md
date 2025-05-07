# Azure Hands-On: AKS e App Service

> Este projeto implementa desafios práticos para entender conceitos fundamentais do Azure Kubernetes Service (AKS) e Azure App Service, com testes automatizados e documentação detalhada.

![Azure Logo](https://ms-azuretools.gallerycdn.vsassets.io/extensions/ms-azuretools/vscode-azureappservice/0.24.2/1671055454061/Microsoft.VisualStudio.Services.Icons.Default)
![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Pytest](https://img.shields.io/badge/Pytest-8.3+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📝 Descrição do Projeto

Este repositório contém implementações de desafios práticos relacionados a dois importantes serviços da Microsoft Azure:

- **Azure Kubernetes Service (AKS)**: Serviço gerenciado de orquestração de contêineres baseado no Kubernetes
- **Azure App Service**: Plataforma PaaS (Platform as a Service) para hospedagem de aplicações web

Cada desafio consiste em uma implementação prática que demonstra o entendimento de conceitos-chave destes serviços.

## 🔍 Estrutura do Repositório

```
LABAKSappservice/
├── desafios/
│   ├── desafio_aks.py          # Implementação do desafio AKS
│   ├── desafio_appservice.py   # Implementação do desafio App Service
├── testes/
│   ├── test_desafio_aks.py     # Testes automatizados para o desafio AKS
│   ├── test_desafio_appservice.py  # Testes automatizados para o desafio App Service
├── docs/
│   ├── LAB_AKS_PASSO_1.md      # Documentação do desafio AKS
│   ├── LAB_AKS_PASSO_2.md      # Documentação do desafio App Service
├── README.md                   # Este arquivo
├── LICENSE.md                  # Licença do projeto
└── CHANGELOG.md                # Histórico de alterações
```

## 🚀 Como Executar

### Pré-requisitos

- Python 3.7 ou superior
- Pytest (para executar os testes)

### Instalação

```bash
# Clone o repositório
git clone https://github.com/gisengsoft/LABAKSappservice.git
cd LABAKSappservice

# Instale as dependências
pip install pytest
```

### Executando os Desafios

**Desafio AKS:**
```bash
python desafios/desafio_aks.py
```

**Desafio App Service:**
```bash
python desafios/desafio_appservice.py
```

### Executando os Testes

```bash
# Executar todos os testes
pytest testes/ -v

# Executar apenas testes do AKS
pytest testes/test_desafio_aks.py -v

# Executar apenas testes do App Service
pytest testes/test_desafio_appservice.py -v
```

## 📋 Detalhes dos Desafios

Para mais informações sobre cada desafio, consulte:
- Documentação do Desafio AKS
- Documentação do Desafio App Service

## 👥 Como Contribuir

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Faça commit das suas alterações (`git commit -m 'Adiciona nova feature'`)
4. Faça push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a Licença MIT.