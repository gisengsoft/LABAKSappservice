# Desafio Azure Kubernetes Service (AKS)

## Descrição

Azure Kubernetes Service (AKS) é um serviço gerenciado da Microsoft que simplifica a implantação, o gerenciamento e as operações do Kubernetes. O Kubernetes é uma plataforma de código aberto para automatizar a implantação, escalonamento e gerenciamento de aplicações em contêineres.

Neste desafio, você irá explorar conceitos fundamentais do AKS e Kubernetes, compreendendo como os diferentes componentes interagem para criar uma plataforma robusta de orquestração de contêineres.

## Entrada

Uma string contendo um dos conceitos abaixo:

- AKS
- Pod
- Node
- Cluster

## Saída

A entrada consistirá no conceito do Azure Kubernetes Service para o qual você deve retornar a descrição. Nesse contexto, os seguintes conceitos são considerados válidos para este desafio de código:

- Serviço gerenciado de orquestração de contêineres
- Unidade mínima de execução em um cluster Kubernetes
- Máquina (VM) onde os Pods são executados
- Conjunto de nós que executam aplicações containerizadas

## Exemplos

A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

| Entrada | Saída                                                   |
| ------- | ------------------------------------------------------- |
| AKS     | Serviço gerenciado de orquestração de contêineres       |
| Pod     | Unidade mínima de execução em um cluster Kubernetes     |
| Node    | Máquina (VM) onde os Pods são executados                |
| Cluster | Conjunto de nós que executam aplicações containerizadas |

**Atenção:** É extremamente importante que as entradas e saídas sejam exatamente iguais às descritas na descrição do desafio de código.

## Implementação Sugerida

```python
entrada = input()

def descrever_conceito(conceito):
  if conceito == "AKS":
    return "Serviço gerenciado de orquestração de contêineres"
  elif conceito == "Pod":
    return "Unidade mínima de execução em um cluster Kubernetes"
  elif conceito == "Node":
    return "Máquina (VM) onde os Pods são executados"
  elif conceito == "Cluster":
    return "Conjunto de nós que executam aplicações containerizadas"
  else:
    return None

print(descrever_conceito(entrada))
```

## Como Testar

Execute o código e digite um dos conceitos mencionados quando solicitado:

```bash
python desafios/desafio_aks.py
```

Alternativamente, você pode verificar se sua implementação está correta executando os testes automatizados:

```bash
pytest testes/test_desafio_aks.py -v
```
