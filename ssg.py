import typer

from ssg.site import Site


def main(source='content', dest='dest'):
    config = {'source': source,
              'dest': dest}

    Site(config['source'], config['dest']).build()


typer.run(main())
