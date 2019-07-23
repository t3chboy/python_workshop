import logging
def extract_address(location_data = None):
    """
    Gives the address
    :param location_data:
    :return:
    """
    if location_data is not None:
        address = location_data.split(',')
    return address

try:
    a = extract_address(location_data)
except NameError as e:
    FORMAT = '%(filename)s - %(levelname)s - %(message)s'
    logging.basicConfig(format=FORMAT)
    logging.error(e)