# this is an example of entry group

import click


@click.group()
def cli():  # well it has to be cli
    pass

@cli.group()
def lunch():
    ...

@cli.group()
def dinner():
    ...

@click.command()
@click.option("--quantity", default=5, type=int, help="how many burgers..")
def burger(quantity: int):
    print(f"here is {quantity} burger")

# cannot dinner.command() cannot double up bro
@lunch.command()
def noodle():
    """noodle is lunch only!!
    """
    print("some noodles for you")


# if we want to serve burger for both lunch and dinner
# need to use add_command here..
lunch.add_command(burger)
dinner.add_command(burger)

if __name__ == "__main__":
    cli()

    # in this case, we can use
    # python restaurant.py
    # python restaurant.py dinner
    # python restaurant.py dinner burger -> enjoy your burger