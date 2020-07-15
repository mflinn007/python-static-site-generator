import typer

from ssg.site import Site
from ssg import parsers


def main(source='content', dest='dist'):
    config = {'source': source,
              'dest': dest,
              'parsers': parsers.ResourceParser()}

    # This unpacks the dictionary... for some reason doesnt work when passing the individual values
    Site(**config).build()


typer.run(main)
