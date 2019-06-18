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


class DdlName(Model):
    """A Data Lake Analytics DDL name item.

    :param first_part: the name of the table associated with this database and
     schema.
    :type first_part: str
    :param second_part: the name of the table associated with this database
     and schema.
    :type second_part: str
    :param third_part: the name of the table associated with this database and
     schema.
    :type third_part: str
    :param server: the name of the table associated with this database and
     schema.
    :type server: str
    """

    _attribute_map = {
        'first_part': {'key': 'firstPart', 'type': 'str'},
        'second_part': {'key': 'secondPart', 'type': 'str'},
        'third_part': {'key': 'thirdPart', 'type': 'str'},
        'server': {'key': 'server', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(DdlName, self).__init__(**kwargs)
        self.first_part = kwargs.get('first_part', None)
        self.second_part = kwargs.get('second_part', None)
        self.third_part = kwargs.get('third_part', None)
        self.server = kwargs.get('server', None)