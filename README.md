# TCPIPY - Representação Prática do Modelo TCP/IP

Este projeto é uma **simulação prática do modelo TCP/IP**, demonstrando as camadas envolvidas em uma comunicação real de rede. Ele exibe, de maneira didática, o que ocorre em cada camada do modelo TCP/IP ao realizar uma requisição HTTP. A proposta é oferecer uma compreensão visual e interativa do funcionamento do protocolo TCP/IP.

## Funcionalidades

Ao rodar o programa, ele simula a comunicação TCP/IP real, apresentando o que acontece em cada uma das camadas do modelo:

- **Camada de Aplicação**: Faz uma requisição HTTP real a um servidor e exibe o status da resposta.
- **Camada de Transporte**: Captura a **porta TCP local** usada durante a conexão e exibe as informações da camada de transporte.
- **Camada de Rede**: Resolve o domínio para um **endereço IP**, simulando o processo de resolução DNS.
- **Camada de Enlace**: Exibe a **interface de rede** usada na conexão (Ethernet, Wi-Fi, etc.).

## Instalação

### 1. Via PyPI:

```bash
pip install tcpipy
```

### 1. Clonar o Repositório

```bash
git clone https://github.com/bogeabr/tcpipy.git
cd tcpipy
poetry install
```
### Ou


```bash
git clone https://github.com/bogeabr/tcpipy.git
cd tcpipy
python -m venv .venv
source .venv/bin/activate  # ou .venv\Scripts\activate no Windows
pip install -e .
```

![Saida do programa](https://github.com/bogeabr/tcpipy/blob/c3e90f3ce9eb95babdb39f00da8accb4244fcc9d/assets/capitura.png)
