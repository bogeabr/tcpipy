import http.client
import socket
import psutil
from rich import print
from rich.panel import Panel
from rich.console import Console 
from urllib.parse import urlparse   


console = Console()     

class ProtocolTCPIP:
    def __init__(self):
        self.server_ip = None
        self.local_port = None

    def application(self, url):
        # Camada de Aplicação - Faz a requisição HTTP real usando requests
        console.print(Panel.fit("[bold magenta]CAMADA DE APLICAÇÃO[/bold magenta]"))
        
        # Certifique-se de usar um domínio válido
        try:
            connection = http.client.HTTPConnection(url, 80)
            connection.request("GET", "/")
            response = connection.getresponse()
            console.print(f"[green]Requisição HTTP para [yellow]{url}[/yellow]")
            console.print(f"Status da resposta: [bold]{response.status} {response.reason}[/bold]")
            return connection
        except socket.gaierror as e:
            console.print(f"[red]Erro ao resolver o host {url}: {e}[/red]")
            return None

    def transport(self, connection):
        # Camada de Transporte - Exibe detalhes da conexão TCP
        if connection:
            console.print(Panel.fit("[bold cyan]CAMADA DE TRANSPORTE[/bold cyan]"))
            sock = connection.sock
            self.local_port = sock.getsockname()[1]
            console.print(f"[cyan]Usando conexão TCP com porta local: {self.local_port}[/cyan]")
        else:
            console.print("[red]A conexão não pôde ser estabelecida.[/red]")

    def network(self, host):
        try:
            self.server_ip = socket.gethostbyname(host)
            console.print(Panel.fit("[bold blue]CAMADA DE REDE (IP)[/bold blue]"))
            console.print(f"[blue]Domínio resolvido para o IP: [bold]{self.server_ip}[/bold]")
        except socket.gaierror as e:
            console.print(f"[red]Erro ao resolver o IP do host {host}: {e}[/red]") 

    def enlace(self):
        console.print(Panel.fit("[bold yellow]CAMADA DE ENLACE[/bold yellow]"))
        interfaces = psutil.net_if_addrs()
        active_interface = None
        for interface, addrs in interfaces.items():
            for addr in addrs:
                if addr.family == socket.AF_INET:
                    active_interface = interface
                    console.print(f"[yellow]Interface de rede usada: [bold]{interface}[/bold]")
                    break
            if active_interface:
                break
        if not active_interface:
            console.print("[red]Nenhuma interface de rede ativa encontrada")
                    

def main():
    url = 'www.google.com'      
    protocol = ProtocolTCPIP()
    connection = protocol.application(url)
    protocol.transport(connection)
    protocol.network(url)
    protocol.enlace()                             

if __name__ == '__main__':
    main()  