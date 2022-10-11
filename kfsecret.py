import click
import secrets
from string import printable
from string import ascii_lowercase as letters


@click.command()
@click.option('--iterations','-i',help="Number of iterations to do",type=click.INT)
@click.option('--output','-o',help="Output file")

def main(iterations, output):

    character_list = printable
    character_list.remove('\r')

    kf_secret = []
    for i in range(iterations):
        kf_secret.append(character_list[secrets.randbelow(len(character_list))])

    with open(output, 'w') as f:
        f.write(''.join(kf_secret))


if __name__ == '__main__':
    main()
