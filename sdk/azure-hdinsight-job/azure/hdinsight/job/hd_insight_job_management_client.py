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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.job_operations import JobOperations
from . import models


class HDInsightJobManagementClientConfiguration(AzureConfiguration):
    """Configuration for HDInsightJobManagementClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param cluster_dns_name: The cluster dns name against which the job
     management is to be.
    :type cluster_dns_name: str
    :param username: The user name used for running job.
    :type username: str
    """

    def __init__(
            self, credentials, cluster_dns_name, username):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if cluster_dns_name is None:
            raise ValueError("Parameter 'cluster_dns_name' must not be None.")
        if username is None:
            raise ValueError("Parameter 'username' must not be None.")
        base_url = 'https://{clusterDnsName}'

        super(HDInsightJobManagementClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-hdinsight-job/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.cluster_dns_name = cluster_dns_name
        self.username = username


class HDInsightJobManagementClient(SDKClient):
    """The HDInsight Job Client.

    :ivar config: Configuration for client.
    :vartype config: HDInsightJobManagementClientConfiguration

    :ivar job: Job operations
    :vartype job: azure.hdinsight.job.operations.JobOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param cluster_dns_name: The cluster dns name against which the job
     management is to be.
    :type cluster_dns_name: str
    :param username: The user name used for running job.
    :type username: str
    """

    def __init__(
            self, credentials, cluster_dns_name, username):

        self.config = HDInsightJobManagementClientConfiguration(credentials, cluster_dns_name, username)
        super(HDInsightJobManagementClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2018-11-01-preview'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.job = JobOperations(
            self._client, self.config, self._serialize, self._deserialize)