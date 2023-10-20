import click
import hashlib
from collections import Counter
from tabulate import tabulate

@click.command()
@click.argument('input_string')
def hash_frequency(input_string):
    """Calculate and display the most common hash values for a given string."""
    hash_algorithms = [hashlib.md5, hashlib.sha1, hashlib.sha256, hashlib.sha512]
    hash_counts = {algorithm().name: algorithm(input_string.encode()).hexdigest() for algorithm in hash_algorithms}
    print(hash_counts)

    headers = ['Algorithm', 'Hash Value']
    hash_table = [[algo, hash_val] for algo, hash_val in hash_counts.items()]

    print(tabulate(hash_table, headers, tablefmt='grid'))

if __name__ == '__main__':
    hash_frequency()