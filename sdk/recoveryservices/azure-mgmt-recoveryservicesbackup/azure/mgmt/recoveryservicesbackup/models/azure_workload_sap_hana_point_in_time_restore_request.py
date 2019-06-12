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

from .azure_workload_sap_hana_restore_request import AzureWorkloadSAPHanaRestoreRequest


class AzureWorkloadSAPHanaPointInTimeRestoreRequest(AzureWorkloadSAPHanaRestoreRequest):
    """AzureWorkload SAP Hana -specific restore. Specifically for PointInTime/Log
    restore.

    All required parameters must be populated in order to send to Azure.

    :param object_type: Required. Constant filled by server.
    :type object_type: str
    :param recovery_type: OLR/ALR, RestoreDisks is invalid option. Possible
     values include: 'Invalid', 'OriginalLocation', 'AlternateLocation',
     'RestoreDisks'
    :type recovery_type: str or
     ~azure.mgmt.recoveryservicesbackup.models.RecoveryType
    :param source_resource_id: Fully qualified ARM ID of the VM on which
     workload that was running is being recovered.
    :type source_resource_id: str
    :param property_bag: Workload specific property bag.
    :type property_bag: dict[str, str]
    :param target_info: Details of target database
    :type target_info:
     ~azure.mgmt.recoveryservicesbackup.models.TargetRestoreInfo
    :param point_in_time: PointInTime value
    :type point_in_time: datetime
    """

    _validation = {
        'object_type': {'required': True},
    }

    _attribute_map = {
        'object_type': {'key': 'objectType', 'type': 'str'},
        'recovery_type': {'key': 'recoveryType', 'type': 'str'},
        'source_resource_id': {'key': 'sourceResourceId', 'type': 'str'},
        'property_bag': {'key': 'propertyBag', 'type': '{str}'},
        'target_info': {'key': 'targetInfo', 'type': 'TargetRestoreInfo'},
        'point_in_time': {'key': 'pointInTime', 'type': 'iso-8601'},
    }

    def __init__(self, **kwargs):
        super(AzureWorkloadSAPHanaPointInTimeRestoreRequest, self).__init__(**kwargs)
        self.point_in_time = kwargs.get('point_in_time', None)
        self.object_type = 'AzureWorkloadSAPHanaPointInTimeRestoreRequest'