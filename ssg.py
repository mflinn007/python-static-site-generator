import typer

from ssg.site import Site

import ssg.parsers


def main(source='content', dest='dist'):
    config = {'source': source,
              'dest': dest,
              'parsers': [ssg.parsers.ResourceParser()]}

    # This unpacks the dictionary... for some reason doesnt work when passing the individual values
    Site(**config).build()


typer.run(main)
