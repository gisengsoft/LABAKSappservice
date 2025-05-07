def descrever_conceito(conceito):
    """
    Retorna a descrição de um conceito relacionado ao Azure Kubernetes Service.
    
    Args:
        conceito (str): O conceito a ser descrito (AKS, Pod, Node ou Cluster)
        
    Returns:
        str: A descrição do conceito ou None se não for encontrado
    """
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

# Este código só executa quando o arquivo é executado diretamente
if __name__ == "__main__":
    entrada = input("Digite um conceito (AKS, Pod, Node, Cluster): ")
    print(descrever_conceito(entrada))