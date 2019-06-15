from __future__ import absolute_import
from six import string_types
from .errors import InvalidRequestError

def required(attr):
    """
    Parameters
    ----------
    attr : str
    Returns
    -------
    """
    def wrapper(func):
        def validate(self):
            if getattr(self, attr, None) is None:
                raise InvalidRequestError("'{0}' property is required.".format(attr))
            return func(self)

        return validate

    return wrapper

def max_value(attr, value):
    """
    Parameters
    ----------
    attr : int or str
    value : int
    Returns
    -------
    """
    def wrapper(func):
        def validate(self):
            if hasattr(self, attr):
                attr_val = getattr(self, attr)
                if isinstance(attr_val, int) and attr_val > value:
                    raise InvalidRequestError(
                        "'{0}' property should be lower than '{1}'. Current value: '{2}'.".format(attr, value,
                                                                                                  attr_val))
                elif isinstance(attr_val, string_types) and len(attr_val) > value:
                    raise InvalidRequestError(
                        "'{0}' property should be lower than '{1}' characters. Current value: '{2}', len'{3}'.".format(
                            attr,
                            value,
                            attr_val,
                            len(attr_val)))
                return func(self)

        return validate

    return wrapper


class BaseRequest:
    def __init__(self):
        pass

    def validate(self):
        """
        Validates request simply
        Raises
        -------
        InvalidRequestError
        """
        pass

    def decode(self):
        """
        Generates api request parameters from Request object
        Returns
        -------
        dict
        """
        return self.__dict__.copy()
