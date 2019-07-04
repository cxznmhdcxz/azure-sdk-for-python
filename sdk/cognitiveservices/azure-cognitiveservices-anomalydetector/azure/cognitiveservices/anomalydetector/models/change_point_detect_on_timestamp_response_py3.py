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


class ChangePointDetectOnTimestampResponse(Model):
    """ChangePointDetectOnTimestampResponse.

    All required parameters must be populated in order to send to Azure.

    :param period: Required. Frequency extracted from the series, zero means
     no recurrent pattern has been found.
    :type period: int
    :param change_point: Required. The closest change point's timestamp.
    :type change_point: datetime
    :param confidence_score: Required. The change point confidence score.
    :type confidence_score: float
    :param timestamp: Required. Timestamp of a data point (ISO8601 format).
    :type timestamp: datetime
    """

    _validation = {
        'period': {'required': True},
        'change_point': {'required': True},
        'confidence_score': {'required': True},
        'timestamp': {'required': True},
    }

    _attribute_map = {
        'period': {'key': 'period', 'type': 'int'},
        'change_point': {'key': 'changePoint', 'type': 'iso-8601'},
        'confidence_score': {'key': 'confidenceScore', 'type': 'float'},
        'timestamp': {'key': 'timestamp', 'type': 'iso-8601'},
    }

    def __init__(self, *, period: int, change_point, confidence_score: float, timestamp, **kwargs) -> None:
        super(ChangePointDetectOnTimestampResponse, self).__init__(**kwargs)
        self.period = period
        self.change_point = change_point
        self.confidence_score = confidence_score
        self.timestamp = timestamp
