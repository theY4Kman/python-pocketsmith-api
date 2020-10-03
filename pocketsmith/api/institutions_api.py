# coding: utf-8

"""
    PocketSmith

    The public PocketSmith API  # noqa: E501

    The version of the OpenAPI document: 2.0
    Contact: api@pocketsmith.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from pocketsmith.api_client import ApiClient
from pocketsmith.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class InstitutionsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_institution(self, id, **kwargs):  # noqa: E501
        """Create institution in user  # noqa: E501

        Creates an institution belonging to a user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_institution(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int id: The unique identifier of the user (required)
        :param InlineObject13 inline_object13:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Institution
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_institution_with_http_info(id, **kwargs)  # noqa: E501

    def create_institution_with_http_info(self, id, **kwargs):  # noqa: E501
        """Create institution in user  # noqa: E501

        Creates an institution belonging to a user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_institution_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int id: The unique identifier of the user (required)
        :param InlineObject13 inline_object13:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Institution, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'id',
            'inline_object13'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_institution" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `create_institution`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'inline_object13' in local_var_params:
            body_params = local_var_params['inline_object13']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['developerKey']  # noqa: E501

        return self.api_client.call_api(
            '/users/{id}/institutions', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Institution',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_institution(self, id, **kwargs):  # noqa: E501
        """Delete institution  # noqa: E501

        Deletes an institution and all data within. Alternatively, another institution can be provided to merge the data into to avoid losing it.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_institution(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int id: The unique identifier of the institution. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_institution_with_http_info(id, **kwargs)  # noqa: E501

    def delete_institution_with_http_info(self, id, **kwargs):  # noqa: E501
        """Delete institution  # noqa: E501

        Deletes an institution and all data within. Alternatively, another institution can be provided to merge the data into to avoid losing it.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_institution_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int id: The unique identifier of the institution. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_institution" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `delete_institution`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['developerKey']  # noqa: E501

        return self.api_client.call_api(
            '/institutions/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_institution(self, id, **kwargs):  # noqa: E501
        """Get institution  # noqa: E501

        Gets an institution by its ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_institution(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int id: The unique identifier of the institution. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Institution
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_institution_with_http_info(id, **kwargs)  # noqa: E501

    def get_institution_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get institution  # noqa: E501

        Gets an institution by its ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_institution_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int id: The unique identifier of the institution. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Institution, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_institution" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `get_institution`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['developerKey']  # noqa: E501

        return self.api_client.call_api(
            '/institutions/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Institution',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_institutions(self, id, **kwargs):  # noqa: E501
        """List institutions in user  # noqa: E501

        Lists all the institutions belonging to the user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_institutions(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int id: The unique identifier of the user (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[Institution]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_institutions_with_http_info(id, **kwargs)  # noqa: E501

    def list_institutions_with_http_info(self, id, **kwargs):  # noqa: E501
        """List institutions in user  # noqa: E501

        Lists all the institutions belonging to the user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_institutions_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int id: The unique identifier of the user (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[Institution], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_institutions" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `list_institutions`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['developerKey']  # noqa: E501

        return self.api_client.call_api(
            '/users/{id}/institutions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Institution]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_institution(self, id, **kwargs):  # noqa: E501
        """Update institution  # noqa: E501

        Updates the title and currency code for an institution.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_institution(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int id: The unique identifier of the institution. (required)
        :param InlineObject4 inline_object4:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Institution
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.update_institution_with_http_info(id, **kwargs)  # noqa: E501

    def update_institution_with_http_info(self, id, **kwargs):  # noqa: E501
        """Update institution  # noqa: E501

        Updates the title and currency code for an institution.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_institution_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int id: The unique identifier of the institution. (required)
        :param InlineObject4 inline_object4:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Institution, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'id',
            'inline_object4'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_institution" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `update_institution`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'inline_object4' in local_var_params:
            body_params = local_var_params['inline_object4']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['developerKey']  # noqa: E501

        return self.api_client.call_api(
            '/institutions/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Institution',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
