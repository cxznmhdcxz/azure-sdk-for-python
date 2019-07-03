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


class ServiceBusBrokeredMessageProperties(Model):
    """ServiceBusBrokeredMessageProperties.

    :param content_type: Gets or sets the content type.
    :type content_type: str
    :param correlation_id: Gets or sets the correlation ID.
    :type correlation_id: str
    :param force_persistence: Gets or sets the force persistence.
    :type force_persistence: bool
    :param label: Gets or sets the label.
    :type label: str
    :param message_id: Gets or sets the message ID.
    :type message_id: str
    :param partition_key: Gets or sets the partition key.
    :type partition_key: str
    :param reply_to: Gets or sets the reply to.
    :type reply_to: str
    :param reply_to_session_id: Gets or sets the reply to session ID.
    :type reply_to_session_id: str
    :param scheduled_enqueue_time_utc: Gets or sets the scheduled enqueue time
     UTC.
    :type scheduled_enqueue_time_utc: datetime
    :param session_id: Gets or sets the session ID.
    :type session_id: str
    :param time_to_live: Gets or sets the time to live.
    :type time_to_live: timedelta
    :param to: Gets or sets the to.
    :type to: str
    :param via_partition_key: Gets or sets the via partition key.
    :type via_partition_key: str
    """

    _attribute_map = {
        'content_type': {'key': 'contentType', 'type': 'str'},
        'correlation_id': {'key': 'correlationId', 'type': 'str'},
        'force_persistence': {'key': 'forcePersistence', 'type': 'bool'},
        'label': {'key': 'label', 'type': 'str'},
        'message_id': {'key': 'messageId', 'type': 'str'},
        'partition_key': {'key': 'partitionKey', 'type': 'str'},
        'reply_to': {'key': 'replyTo', 'type': 'str'},
        'reply_to_session_id': {'key': 'replyToSessionId', 'type': 'str'},
        'scheduled_enqueue_time_utc': {'key': 'scheduledEnqueueTimeUtc', 'type': 'iso-8601'},
        'session_id': {'key': 'sessionId', 'type': 'str'},
        'time_to_live': {'key': 'timeToLive', 'type': 'duration'},
        'to': {'key': 'to', 'type': 'str'},
        'via_partition_key': {'key': 'viaPartitionKey', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ServiceBusBrokeredMessageProperties, self).__init__(**kwargs)
        self.content_type = kwargs.get('content_type', None)
        self.correlation_id = kwargs.get('correlation_id', None)
        self.force_persistence = kwargs.get('force_persistence', None)
        self.label = kwargs.get('label', None)
        self.message_id = kwargs.get('message_id', None)
        self.partition_key = kwargs.get('partition_key', None)
        self.reply_to = kwargs.get('reply_to', None)
        self.reply_to_session_id = kwargs.get('reply_to_session_id', None)
        self.scheduled_enqueue_time_utc = kwargs.get('scheduled_enqueue_time_utc', None)
        self.session_id = kwargs.get('session_id', None)
        self.time_to_live = kwargs.get('time_to_live', None)
        self.to = kwargs.get('to', None)
        self.via_partition_key = kwargs.get('via_partition_key', None)