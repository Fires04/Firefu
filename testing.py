import click
import subprocess
import sys
import os

@click.command()
@click.option('--target', required=True, help='Target host or IP address.')
@click.option('--nmap', is_flag=True, help='Run nmap on the target.')
@click.option('--ping', is_flag=True, help='Run ping on the target.')
def main(target, nmap, ping):
    """
    Simple program to run commands on a target host or IP address.
    """
    click.echo(f"Target: {target}")

    if nmap:
        if is_nmap_installed():
            run_nmap(target)
        else:
            click.echo("nmap is not installed. Please install nmap to use this feature.")

    if ping:
        run_ping(target)

def is_nmap_installed():
    """
    Check if nmap is installed by attempting to run 'nmap --version'.
    """
    try:
        subprocess.check_output(["nmap", "--version"], stderr=subprocess.STDOUT)
        return True
    except subprocess.CalledProcessError:
        return False

def run_nmap(target):
    """
    Run the nmap command on the target.
    """
    click.echo("Running nmap command...")
    try:
        result = subprocess.check_output(["nmap", target])
        click.echo(result.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        click.echo(f"Error running nmap: {e} {result}")

def run_ping(target):
    """
    Run the ping command on the target.
    """
    click.echo("Running ping command...")
    try:
        process = subprocess.Popen(["ping", target], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        for line in process.stdout:
            sys.stdout.write(line)
        process.wait()
    except subprocess.CalledProcessError as e:
        click.echo(f"Error running ping: {e}")

if __name__ == '__main__':
    main()
