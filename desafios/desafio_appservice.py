def descrever_conceito_appservice(conceito):
    """
    Retorna a descrição de um conceito relacionado ao Azure App Service.
    
    Args:
        conceito (str): O conceito a ser descrito (App Service, Escalabilidade, 
                        Slot de Deployment ou CI/CD)
        
    Returns:
        str: A descrição do conceito ou None se não for encontrado
    """
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

# Este código só executa quando o arquivo é executado diretamente
if __name__ == "__main__":
    entrada = input("Digite um conceito (App Service, Escalabilidade, Slot de Deployment, CI/CD): ")
    print(descrever_conceito_appservice(entrada))