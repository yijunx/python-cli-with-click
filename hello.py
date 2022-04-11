import click


@click.command()
# @click.option('--string', default="World")  # hello --string nihao -> hello nihao # this is option..
@click.argument('who')  # hello nihao -> hello nihao  # so we can see the difference between argument and option
@click.option('--number', default=5, type=int, help="number of times it repeats")
@click.option('--weather', type=click.Choice(['sunny', 'rainy', 'snowy']))
def cli(who: str, number: int, weather: str):
    '''this is a cool cli
    '''

    # weather will be None if not set
    # there is be error if weather is not sunny rainy or snowy
    for _ in range(number):
        print(f"hello {who}, the weather is {weather if weather else 'not provided'}")


if __name__ == "__main__":
    # allows
    # python hello.py --string nihao
    # -> hello nihao

    # if we use argument.
    # python hello.py nihao 
    # -> hello nihao

    # so here is the difference between option and argument
    cli()

    # python hello.py --help
    # will be same as hello --help
    # of course this is after pip install --editable .


