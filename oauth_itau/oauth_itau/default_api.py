# coding: utf-8

"""
    oAuth

    oAuth para produção  # noqa: E501

    OpenAPI spec version: 1.40.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from oauth_itau.api_client import ApiClient


class DefaultApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def postoauthtoken(self, **kwargs):  # noqa: E501
        """post /oauth/token  # noqa: E501

        Operação responsável por recuperar o tokem de acesso  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.postoauthtoken(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str client_id: 
        :param str client_secret: 
        :param str grant_type: 
        :param str scope: 
        :return: OauthCred
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.postoauthtoken_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.postoauthtoken_with_http_info(**kwargs)  # noqa: E501
            return data

    def postoauthtoken_with_http_info(self, **kwargs):  # noqa: E501
        """post /oauth/token  # noqa: E501

        Operação responsável por recuperar o tokem de acesso  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.postoauthtoken_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str client_id: 
        :param str client_secret: 
        :param str grant_type: 
        :param str scope: 
        :return: OauthCred
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['client_id', 'client_secret', 'grant_type', 'scope']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method postoauthtoken" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'client_id' in params:
            form_params.append(('client_id', params['client_id']))  # noqa: E501
        if 'client_secret' in params:
            form_params.append(('client_secret', params['client_secret']))  # noqa: E501
        if 'grant_type' in params:
            form_params.append(('grant_type', params['grant_type']))  # noqa: E501
        if 'scope' in params:
            form_params.append(('scope', params['scope']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/oauth/token', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OauthCred',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
