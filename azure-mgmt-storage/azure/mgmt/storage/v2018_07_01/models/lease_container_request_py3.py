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


class LeaseContainerRequest(Model):
    """Lease Container request schema.

    All required parameters must be populated in order to send to Azure.

    :param action: Required. Specifies the lease action. Can be one of the
     available actions. Possible values include: 'Acquire', 'Renew', 'Change',
     'Release', 'Break'
    :type action: str or ~azure.mgmt.storage.v2018_07_01.models.enum
    :param lease_id: Identifies the lease. Can be specified in any valid GUID
     string format.
    :type lease_id: str
    :param break_period: Optional. For a break action, proposed duration the
     lease should continue before it is broken, in seconds, between 0 and 60.
    :type break_period: int
    :param lease_duration: Required for acquire. Specifies the duration of the
     lease, in seconds, or negative one (-1) for a lease that never expires.
    :type lease_duration: int
    :param proposed_lease_id: Optional for acquire, required for change.
     Proposed lease ID, in a GUID string format.
    :type proposed_lease_id: str
    """

    _validation = {
        'action': {'required': True},
    }

    _attribute_map = {
        'action': {'key': 'action', 'type': 'str'},
        'lease_id': {'key': 'leaseId', 'type': 'str'},
        'break_period': {'key': 'breakPeriod', 'type': 'int'},
        'lease_duration': {'key': 'leaseDuration', 'type': 'int'},
        'proposed_lease_id': {'key': 'proposedLeaseId', 'type': 'str'},
    }

    def __init__(self, *, action, lease_id: str=None, break_period: int=None, lease_duration: int=None, proposed_lease_id: str=None, **kwargs) -> None:
        super(LeaseContainerRequest, self).__init__(**kwargs)
        self.action = action
        self.lease_id = lease_id
        self.break_period = break_period
        self.lease_duration = lease_duration
        self.proposed_lease_id = proposed_lease_id