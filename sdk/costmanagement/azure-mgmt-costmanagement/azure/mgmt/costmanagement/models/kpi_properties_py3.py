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


class KpiProperties(Model):
    """Each KPI must contain a 'type' and 'enabled' key.

    :param type: KPI type (Forecast, Budget). Possible values include:
     'Forecast', 'Budget'
    :type type: str or ~azure.mgmt.costmanagement.models.KpiTypeType
    :param id: ID of resource related to metric (budget).
    :type id: str
    :param enabled: show the KPI in the UI?
    :type enabled: bool
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'enabled': {'key': 'enabled', 'type': 'bool'},
    }

    def __init__(self, *, type=None, id: str=None, enabled: bool=None, **kwargs) -> None:
        super(KpiProperties, self).__init__(**kwargs)
        self.type = type
        self.id = id
        self.enabled = enabled