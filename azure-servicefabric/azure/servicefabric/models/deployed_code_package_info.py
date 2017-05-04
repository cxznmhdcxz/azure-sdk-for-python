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

from msrest.serialization import Model


class DeployedCodePackageInfo(Model):
    """Information about code package deployed on a Service Fabric node.

    :param name: The name of the code package.
    :type name: str
    :param version: The version of the code package specified in service
     manifest.
    :type version: str
    :param service_manifest_name: The name of service manifest that specified
     this code package.
    :type service_manifest_name: str
    :param service_package_activation_id:
    :type service_package_activation_id: str
    :param host_type: Possible values include: 'Invalid', 'ExeHost',
     'ContainerHost'
    :type host_type: str
    :param host_isolation_mode: Possible values include: 'None', 'Process',
     'HyperV'
    :type host_isolation_mode: str
    :param status: Possible values include: 'Invalid', 'Downloading',
     'Activating', 'Active', 'Upgrading', 'Deactivating'
    :type status: str
    :param run_frequency_interval: The interval at which code package is run.
     This is used for periodic code package.
    :type run_frequency_interval: str
    :param setup_entry_point:
    :type setup_entry_point: :class:`CodePackageEntryPoint
     <azure.servicefabric.models.CodePackageEntryPoint>`
    :param main_entry_point:
    :type main_entry_point: :class:`CodePackageEntryPoint
     <azure.servicefabric.models.CodePackageEntryPoint>`
    """ 

    _attribute_map = {
        'name': {'key': 'Name', 'type': 'str'},
        'version': {'key': 'Version', 'type': 'str'},
        'service_manifest_name': {'key': 'ServiceManifestName', 'type': 'str'},
        'service_package_activation_id': {'key': 'ServicePackageActivationId', 'type': 'str'},
        'host_type': {'key': 'HostType', 'type': 'str'},
        'host_isolation_mode': {'key': 'HostIsolationMode', 'type': 'str'},
        'status': {'key': 'Status', 'type': 'str'},
        'run_frequency_interval': {'key': 'RunFrequencyInterval', 'type': 'str'},
        'setup_entry_point': {'key': 'SetupEntryPoint', 'type': 'CodePackageEntryPoint'},
        'main_entry_point': {'key': 'MainEntryPoint', 'type': 'CodePackageEntryPoint'},
    }

    def __init__(self, name=None, version=None, service_manifest_name=None, service_package_activation_id=None, host_type=None, host_isolation_mode=None, status=None, run_frequency_interval=None, setup_entry_point=None, main_entry_point=None):
        self.name = name
        self.version = version
        self.service_manifest_name = service_manifest_name
        self.service_package_activation_id = service_package_activation_id
        self.host_type = host_type
        self.host_isolation_mode = host_isolation_mode
        self.status = status
        self.run_frequency_interval = run_frequency_interval
        self.setup_entry_point = setup_entry_point
        self.main_entry_point = main_entry_point
