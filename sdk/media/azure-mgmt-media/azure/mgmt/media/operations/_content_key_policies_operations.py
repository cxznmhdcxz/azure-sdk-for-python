# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import uuid
from msrest.pipeline import ClientRawResponse

from .. import models


class ContentKeyPoliciesOperations(object):
    """ContentKeyPoliciesOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: The Version of the API to be used with the client request. Constant value: "2018-07-01".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2018-07-01"

        self.config = config

    def list(
            self, resource_group_name, account_name, filter=None, top=None, orderby=None, custom_headers=None, raw=False, **operation_config):
        """List Content Key Policies.

        Lists the Content Key Policies in the account.

        :param resource_group_name: The name of the resource group within the
         Azure subscription.
        :type resource_group_name: str
        :param account_name: The Media Services account name.
        :type account_name: str
        :param filter: Restricts the set of items returned.
        :type filter: str
        :param top: Specifies a non-negative integer n that limits the number
         of items returned from a collection. The service returns the number of
         available items up to but not greater than the specified value n.
        :type top: int
        :param orderby: Specifies the key by which the result collection
         should be ordered.
        :type orderby: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of ContentKeyPolicy
        :rtype:
         ~azure.mgmt.media.models.ContentKeyPolicyPaged[~azure.mgmt.media.models.ContentKeyPolicy]
        :raises:
         :class:`ApiErrorException<azure.mgmt.media.models.ApiErrorException>`
        """
        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'accountName': self._serialize.url("account_name", account_name, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
                if filter is not None:
                    query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
                if top is not None:
                    query_parameters['$top'] = self._serialize.query("top", top, 'int')
                if orderby is not None:
                    query_parameters['$orderby'] = self._serialize.query("orderby", orderby, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def internal_paging(next_link=None):
            request = prepare_request(next_link)

            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                raise models.ApiErrorException(self._deserialize, response)

            return response

        # Deserialize response
        header_dict = None
        if raw:
            header_dict = {}
        deserialized = models.ContentKeyPolicyPaged(internal_paging, self._deserialize.dependencies, header_dict)

        return deserialized
    list.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/contentKeyPolicies'}

    def get(
            self, resource_group_name, account_name, content_key_policy_name, custom_headers=None, raw=False, **operation_config):
        """Get a Content Key Policy.

        Get the details of a Content Key Policy in the Media Services account.

        :param resource_group_name: The name of the resource group within the
         Azure subscription.
        :type resource_group_name: str
        :param account_name: The Media Services account name.
        :type account_name: str
        :param content_key_policy_name: The Content Key Policy name.
        :type content_key_policy_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ContentKeyPolicy or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.media.models.ContentKeyPolicy or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ApiErrorException<azure.mgmt.media.models.ApiErrorException>`
        """
        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'accountName': self._serialize.url("account_name", account_name, 'str'),
            'contentKeyPolicyName': self._serialize.url("content_key_policy_name", content_key_policy_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 404]:
            raise models.ApiErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('ContentKeyPolicy', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/contentKeyPolicies/{contentKeyPolicyName}'}

    def create_or_update(
            self, resource_group_name, account_name, content_key_policy_name, options, description=None, custom_headers=None, raw=False, **operation_config):
        """Create or update an Content Key Policy.

        Create or update a Content Key Policy in the Media Services account.

        :param resource_group_name: The name of the resource group within the
         Azure subscription.
        :type resource_group_name: str
        :param account_name: The Media Services account name.
        :type account_name: str
        :param content_key_policy_name: The Content Key Policy name.
        :type content_key_policy_name: str
        :param options: The Key Policy options.
        :type options: list[~azure.mgmt.media.models.ContentKeyPolicyOption]
        :param description: A description for the Policy.
        :type description: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ContentKeyPolicy or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.media.models.ContentKeyPolicy or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ApiErrorException<azure.mgmt.media.models.ApiErrorException>`
        """
        parameters = models.ContentKeyPolicy(description=description, options=options)

        # Construct URL
        url = self.create_or_update.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'accountName': self._serialize.url("account_name", account_name, 'str'),
            'contentKeyPolicyName': self._serialize.url("content_key_policy_name", content_key_policy_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(parameters, 'ContentKeyPolicy')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 201]:
            raise models.ApiErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('ContentKeyPolicy', response)
        if response.status_code == 201:
            deserialized = self._deserialize('ContentKeyPolicy', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/contentKeyPolicies/{contentKeyPolicyName}'}

    def delete(
            self, resource_group_name, account_name, content_key_policy_name, custom_headers=None, raw=False, **operation_config):
        """Delete a Content Key Policy.

        Deletes a Content Key Policy in the Media Services account.

        :param resource_group_name: The name of the resource group within the
         Azure subscription.
        :type resource_group_name: str
        :param account_name: The Media Services account name.
        :type account_name: str
        :param content_key_policy_name: The Content Key Policy name.
        :type content_key_policy_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ApiErrorException<azure.mgmt.media.models.ApiErrorException>`
        """
        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'accountName': self._serialize.url("account_name", account_name, 'str'),
            'contentKeyPolicyName': self._serialize.url("content_key_policy_name", content_key_policy_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 204]:
            raise models.ApiErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/contentKeyPolicies/{contentKeyPolicyName}'}

    def update(
            self, resource_group_name, account_name, content_key_policy_name, options, description=None, custom_headers=None, raw=False, **operation_config):
        """Update a Content Key Policy.

        Updates an existing Content Key Policy in the Media Services account.

        :param resource_group_name: The name of the resource group within the
         Azure subscription.
        :type resource_group_name: str
        :param account_name: The Media Services account name.
        :type account_name: str
        :param content_key_policy_name: The Content Key Policy name.
        :type content_key_policy_name: str
        :param options: The Key Policy options.
        :type options: list[~azure.mgmt.media.models.ContentKeyPolicyOption]
        :param description: A description for the Policy.
        :type description: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ContentKeyPolicy or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.media.models.ContentKeyPolicy or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ApiErrorException<azure.mgmt.media.models.ApiErrorException>`
        """
        parameters = models.ContentKeyPolicy(description=description, options=options)

        # Construct URL
        url = self.update.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'accountName': self._serialize.url("account_name", account_name, 'str'),
            'contentKeyPolicyName': self._serialize.url("content_key_policy_name", content_key_policy_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(parameters, 'ContentKeyPolicy')

        # Construct and send request
        request = self._client.patch(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ApiErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('ContentKeyPolicy', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/contentKeyPolicies/{contentKeyPolicyName}'}

    def get_policy_properties_with_secrets(
            self, resource_group_name, account_name, content_key_policy_name, custom_headers=None, raw=False, **operation_config):
        """Get a Content Key Policy with secrets.

        Get a Content Key Policy including secret values.

        :param resource_group_name: The name of the resource group within the
         Azure subscription.
        :type resource_group_name: str
        :param account_name: The Media Services account name.
        :type account_name: str
        :param content_key_policy_name: The Content Key Policy name.
        :type content_key_policy_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ContentKeyPolicyProperties or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.media.models.ContentKeyPolicyProperties or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ApiErrorException<azure.mgmt.media.models.ApiErrorException>`
        """
        # Construct URL
        url = self.get_policy_properties_with_secrets.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'accountName': self._serialize.url("account_name", account_name, 'str'),
            'contentKeyPolicyName': self._serialize.url("content_key_policy_name", content_key_policy_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 404]:
            raise models.ApiErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('ContentKeyPolicyProperties', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_policy_properties_with_secrets.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/contentKeyPolicies/{contentKeyPolicyName}/getPolicyPropertiesWithSecrets'}
