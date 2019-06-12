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


class TokenInformation(Model):
    """The token information details.

    :param token: Token value.
    :type token: str
    :param expiry_time_in_utc_ticks: Expiry time of token.
    :type expiry_time_in_utc_ticks: long
    :param security_pin: Security PIN
    :type security_pin: str
    """

    _attribute_map = {
        'token': {'key': 'token', 'type': 'str'},
        'expiry_time_in_utc_ticks': {'key': 'expiryTimeInUtcTicks', 'type': 'long'},
        'security_pin': {'key': 'securityPIN', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(TokenInformation, self).__init__(**kwargs)
        self.token = kwargs.get('token', None)
        self.expiry_time_in_utc_ticks = kwargs.get('expiry_time_in_utc_ticks', None)
        self.security_pin = kwargs.get('security_pin', None)