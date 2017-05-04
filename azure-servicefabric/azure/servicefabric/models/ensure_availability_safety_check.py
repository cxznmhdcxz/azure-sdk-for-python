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

from .partition_safety_check import PartitionSafetyCheck


class EnsureAvailabilitySafetyCheck(PartitionSafetyCheck):
    """Safety check that waits for ensures the avaiability of the partition. It
    waits until there are replicas avaiabile such that bring down this
    replica will not cause avaiability loss for the partition.

    :param Kind: Polymorphic Discriminator
    :type Kind: str
    :param partition_id: Id of the partition which is undergoing the safety
     check.
    :type partition_id: str
    """ 

    _validation = {
        'Kind': {'required': True},
    }

    def __init__(self, partition_id=None):
        super(EnsureAvailabilitySafetyCheck, self).__init__(partition_id=partition_id)
        self.Kind = 'EnsureAvailability'
