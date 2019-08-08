import logging

import djclick as click
from apps.customers.tests.factories import CustomerFactory

logger = logging.getLogger('add_test_data')


def add_test_data():
    CustomerFactory.create_batch(10000)


@click.command()
def command():
    logger.info('starting add_test_data')
    add_test_data()
    logger.info('add_test_data complete')
