import json


def has_certificate(pkg):
    """
    Can be used in the template to determine if the package has a
    certificate. Returns a boolean.
    """

    extras = pkg.get('extras')

    if extras:
        for extra in extras:
            if extra.get('key') == 'odi-certificate' and\
               get_certificate_data(pkg) is not None:
                    return True


def get_certificate_data(pkg):
    """
    Returns the dictionary containing information about the certificate for the
    given package
    """

    extras = pkg.get('extras')

    if extras:
        for extra in extras:
            if extra.get('key') == 'odi-certificate':
                try:
                    return json.loads(extra.get('value'))
                except ValueError:
                    return None
