# Desafio Azure App Service

## Descrição

Azure App Service é uma plataforma de hospedagem para aplicações web, APIs REST e backends móveis. Ele permite que desenvolvedores foquem em código, enquanto a Azure gerencia a infraestrutura. Neste desafio, você irá entender conceitos como escalabilidade automática, variáveis de ambiente (App Settings), slots de deployment para CI/CD e como tudo isso contribui para a entrega contínua de aplicações.

## Entrada

Uma string contendo um dos conceitos abaixo:

- App Service
- Escalabilidade
- Slot de Deployment
- CI/CD

## Saída

A entrada consistirá no conceito do Azure App Service para o qual você deve retornar a descrição. Nesse contexto, os seguintes conceitos são considerados válidos para este desafio de código:

- Serviço PaaS para hospedar apps na Azure
- Ajusta recursos automaticamente conforme uso
- Ambiente isolado para testes de novas versões
- Automatiza build e deploy de aplicações

## Exemplos

A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

| Entrada            | Saída                                         |
| ------------------ | --------------------------------------------- |
| App Service        | Serviço PaaS para hospedar apps na Azure      |
| Escalabilidade     | Ajusta recursos automaticamente conforme uso  |
| Slot de Deployment | Ambiente isolado para testes de novas versões |
| CI/CD              | Automatiza build e deploy de aplicações       |

**Atenção:** É extremamente importante que as entradas e saídas sejam exatamente iguais às descritas na descrição do desafio de código.

## Implementação Sugerida

```python
entrada = input()

def descrever_conceito(conceito):
  if conceito == "App Service":
    return "Serviço PaaS para hospedar apps na Azure"
  elif conceito == "Escalabilidade":
    return "Ajusta recursos automaticamente conforme uso"
  elif conceito == "Slot de Deployment":
    return "Ambiente isolado para testes de novas versões"
  elif conceito == "CI/CD":
    return "Automatiza build e deploy de aplicações"
  else:
    return None

print(descrever_conceito(entrada))
```

## Como Testar

Execute o código e digite um dos conceitos mencionados quando solicitado:

```bash
python desafios/desafio_appservice.py
```

Alternativamente, você pode verificar se sua implementação está correta executando os testes automatizados:

```bash
pytest testes/test_desafio_appservice.py -v
```

## Recursos Adicionais

Para aprofundar seu conhecimento sobre Azure App Service:

- [Documentação oficial do Azure App Service](https://docs.microsoft.com/pt-br/azure/app-service/)
- [Slots de implantação no Azure App Service](https://docs.microsoft.com/pt-br/azure/app-service/deploy-staging-slots)
- [Configuração de CI/CD para App Service](https://docs.microsoft.com/pt-br/azure/app-service/deploy-continuous-deployment)
