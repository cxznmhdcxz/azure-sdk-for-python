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


class ResumeApplicationUpgradeDescription(Model):
    """Describes the parameters for resuming an unmonitored manual Service Fabric
    application upgrade.

    :param upgrade_domain_name: The name of the upgrade domain in which to
     resume the upgrade.
    :type upgrade_domain_name: str
    """ 

    _validation = {
        'upgrade_domain_name': {'required': True},
    }

    _attribute_map = {
        'upgrade_domain_name': {'key': 'UpgradeDomainName', 'type': 'str'},
    }

    def __init__(self, upgrade_domain_name):
        self.upgrade_domain_name = upgrade_domain_name
