"""
    PocketSmith

    The public PocketSmith API  # noqa: E501

    The version of the OpenAPI document: 2.0+0.3.3
    Contact: api@pocketsmith.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from pocketsmith.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from pocketsmith.exceptions import ApiAttributeError


def lazy_import():
    from pocketsmith.model.data_feeds_connection_user import DataFeedsConnectionUser
    from pocketsmith.model.provider import Provider
    globals()['DataFeedsConnectionUser'] = DataFeedsConnectionUser
    globals()['Provider'] = Provider


class DataFeedsConnection(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'id': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'name': (str, none_type,),  # noqa: E501
            'status': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'status_changed_at': (datetime, none_type,),  # noqa: E501
            'status_changed_at_hash': (str, none_type,),  # noqa: E501
            'error_detail': (str, none_type,),  # noqa: E501
            'user_interaction_likely': (bool,),  # noqa: E501
            'categorisation': (bool,),  # noqa: E501
            'automatic_syncing': (bool,),  # noqa: E501
            'automatic_syncing_overridden': (bool,),  # noqa: E501
            'pending_transactions': (bool,),  # noqa: E501
            'login_form': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'interactive_login_form': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'external_authorisation_url': (str, none_type,),  # noqa: E501
            'external_syncing_url': (str, none_type,),  # noqa: E501
            'last_successful_sync_at': (datetime, none_type,),  # noqa: E501
            'next_sync_possible_at': (datetime, none_type,),  # noqa: E501
            'next_background_sync_at': (datetime, none_type,),  # noqa: E501
            'accounts_updated_at': (datetime, none_type,),  # noqa: E501
            'soft_locked_until': (datetime, none_type,),  # noqa: E501
            'user': (DataFeedsConnectionUser,),  # noqa: E501
            'provider': (Provider,),  # noqa: E501
            'created_at': (datetime, none_type,),  # noqa: E501
            'updated_at': (datetime, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'name': 'name',  # noqa: E501
        'status': 'status',  # noqa: E501
        'status_changed_at': 'status_changed_at',  # noqa: E501
        'status_changed_at_hash': 'status_changed_at_hash',  # noqa: E501
        'error_detail': 'error_detail',  # noqa: E501
        'user_interaction_likely': 'user_interaction_likely',  # noqa: E501
        'categorisation': 'categorisation',  # noqa: E501
        'automatic_syncing': 'automatic_syncing',  # noqa: E501
        'automatic_syncing_overridden': 'automatic_syncing_overridden',  # noqa: E501
        'pending_transactions': 'pending_transactions',  # noqa: E501
        'login_form': 'login_form',  # noqa: E501
        'interactive_login_form': 'interactive_login_form',  # noqa: E501
        'external_authorisation_url': 'external_authorisation_url',  # noqa: E501
        'external_syncing_url': 'external_syncing_url',  # noqa: E501
        'last_successful_sync_at': 'last_successful_sync_at',  # noqa: E501
        'next_sync_possible_at': 'next_sync_possible_at',  # noqa: E501
        'next_background_sync_at': 'next_background_sync_at',  # noqa: E501
        'accounts_updated_at': 'accounts_updated_at',  # noqa: E501
        'soft_locked_until': 'soft_locked_until',  # noqa: E501
        'user': 'user',  # noqa: E501
        'provider': 'provider',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
        'updated_at': 'updated_at',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """DataFeedsConnection - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            id (bool, date, datetime, dict, float, int, list, str, none_type): The unique identifier of the data connection. [optional]  # noqa: E501
            name (str, none_type): User-defined nickname for the data connection. [optional]  # noqa: E501
            status (bool, date, datetime, dict, float, int, list, str, none_type): Sync/auth status of the data connection. [optional]  # noqa: E501
            status_changed_at (datetime, none_type): When the data connection's status last changed. [optional]  # noqa: E501
            status_changed_at_hash (str, none_type): MD5 hash of the status_changed_at field. [optional]  # noqa: E501
            error_detail (str, none_type): ?. [optional]  # noqa: E501
            user_interaction_likely (bool): GUESSING: Whether syncing this data connection is likely to require user interaction. [optional]  # noqa: E501
            categorisation (bool): Whether automatic categorisation of transactions is enabled. [optional]  # noqa: E501
            automatic_syncing (bool): Whether the data connection will automatically sync when logged in to PocketSmith. [optional]  # noqa: E501
            automatic_syncing_overridden (bool): UNKNOWN. [optional]  # noqa: E501
            pending_transactions (bool): Whether to receive pending transactions from this data connection, if available. [optional]  # noqa: E501
            login_form (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            interactive_login_form (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            external_authorisation_url (str, none_type): UNKNOWN. [optional]  # noqa: E501
            external_syncing_url (str, none_type): UNKNOWN. [optional]  # noqa: E501
            last_successful_sync_at (datetime, none_type): When the data connection last synced successfully. [optional]  # noqa: E501
            next_sync_possible_at (datetime, none_type): When the data connection is next allowed to sync at. [optional]  # noqa: E501
            next_background_sync_at (datetime, none_type): When the data connection is scheduled to sync in the background next. [optional]  # noqa: E501
            accounts_updated_at (datetime, none_type): When the accounts tied to the data connection were last updated. [optional]  # noqa: E501
            soft_locked_until (datetime, none_type): UNKNOWN. [optional]  # noqa: E501
            user (DataFeedsConnectionUser): [optional]  # noqa: E501
            provider (Provider): [optional]  # noqa: E501
            created_at (datetime, none_type): When the data connection was created. [optional]  # noqa: E501
            updated_at (datetime, none_type): When the data connection was last updated. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """DataFeedsConnection - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            id (bool, date, datetime, dict, float, int, list, str, none_type): The unique identifier of the data connection. [optional]  # noqa: E501
            name (str, none_type): User-defined nickname for the data connection. [optional]  # noqa: E501
            status (bool, date, datetime, dict, float, int, list, str, none_type): Sync/auth status of the data connection. [optional]  # noqa: E501
            status_changed_at (datetime, none_type): When the data connection's status last changed. [optional]  # noqa: E501
            status_changed_at_hash (str, none_type): MD5 hash of the status_changed_at field. [optional]  # noqa: E501
            error_detail (str, none_type): ?. [optional]  # noqa: E501
            user_interaction_likely (bool): GUESSING: Whether syncing this data connection is likely to require user interaction. [optional]  # noqa: E501
            categorisation (bool): Whether automatic categorisation of transactions is enabled. [optional]  # noqa: E501
            automatic_syncing (bool): Whether the data connection will automatically sync when logged in to PocketSmith. [optional]  # noqa: E501
            automatic_syncing_overridden (bool): UNKNOWN. [optional]  # noqa: E501
            pending_transactions (bool): Whether to receive pending transactions from this data connection, if available. [optional]  # noqa: E501
            login_form (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            interactive_login_form (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            external_authorisation_url (str, none_type): UNKNOWN. [optional]  # noqa: E501
            external_syncing_url (str, none_type): UNKNOWN. [optional]  # noqa: E501
            last_successful_sync_at (datetime, none_type): When the data connection last synced successfully. [optional]  # noqa: E501
            next_sync_possible_at (datetime, none_type): When the data connection is next allowed to sync at. [optional]  # noqa: E501
            next_background_sync_at (datetime, none_type): When the data connection is scheduled to sync in the background next. [optional]  # noqa: E501
            accounts_updated_at (datetime, none_type): When the accounts tied to the data connection were last updated. [optional]  # noqa: E501
            soft_locked_until (datetime, none_type): UNKNOWN. [optional]  # noqa: E501
            user (DataFeedsConnectionUser): [optional]  # noqa: E501
            provider (Provider): [optional]  # noqa: E501
            created_at (datetime, none_type): When the data connection was created. [optional]  # noqa: E501
            updated_at (datetime, none_type): When the data connection was last updated. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")