import click

import click

@click.command()
@click.option('--nmap', help='Standard nmap scan: ')
@click.option('--target',prompt='Target',help='Target ip or DNS name')
def nmap():
    
        

if __name__ == '__main__':
    hello()