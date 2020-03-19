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

from ._configuration import DeploymentManagerClientConfiguration
from .operations import ServiceTopologiesOperations
from .operations import ServicesOperations
from .operations import ServiceUnitsOperations
from .operations import StepsOperations
from .operations import RolloutsOperations
from .operations import ArtifactSourcesOperations
from .operations import Operations
from . import models


class DeploymentManagerClient(SDKClient):
    """REST APIs for orchestrating deployments using the Azure Deployment Manager (ADM). See https://docs.microsoft.com/en-us/azure/azure-resource-manager/deployment-manager-overview for more information.

    :ivar config: Configuration for client.
    :vartype config: DeploymentManagerClientConfiguration

    :ivar service_topologies: ServiceTopologies operations
    :vartype service_topologies: azure.mgmt.deploymentmanager.operations.ServiceTopologiesOperations
    :ivar services: Services operations
    :vartype services: azure.mgmt.deploymentmanager.operations.ServicesOperations
    :ivar service_units: ServiceUnits operations
    :vartype service_units: azure.mgmt.deploymentmanager.operations.ServiceUnitsOperations
    :ivar steps: Steps operations
    :vartype steps: azure.mgmt.deploymentmanager.operations.StepsOperations
    :ivar rollouts: Rollouts operations
    :vartype rollouts: azure.mgmt.deploymentmanager.operations.RolloutsOperations
    :ivar artifact_sources: ArtifactSources operations
    :vartype artifact_sources: azure.mgmt.deploymentmanager.operations.ArtifactSourcesOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.deploymentmanager.operations.Operations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Subscription credentials which uniquely identify
     Microsoft Azure subscription. The subscription ID forms part of the URI
     for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = DeploymentManagerClientConfiguration(credentials, subscription_id, base_url)
        super(DeploymentManagerClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2019-11-01-preview'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.service_topologies = ServiceTopologiesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.services = ServicesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.service_units = ServiceUnitsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.steps = StepsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.rollouts = RolloutsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.artifact_sources = ArtifactSourcesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
