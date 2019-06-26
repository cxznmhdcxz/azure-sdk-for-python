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

from .trigger import Trigger


class ChainingTrigger(Trigger):
    """Trigger that schedules pipeline runs based on dependent pipelines
    successful completion.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param description: Trigger description.
    :type description: str
    :ivar runtime_state: Indicates if trigger is running or not. Updated when
     Start/Stop APIs are called on the Trigger. Possible values include:
     'Started', 'Stopped', 'Disabled'
    :vartype runtime_state: str or
     ~azure.mgmt.datafactory.models.TriggerRuntimeState
    :param annotations: List of tags that can be used for describing the
     trigger.
    :type annotations: list[object]
    :param type: Required. Constant filled by server.
    :type type: str
    :param pipeline: Required. Pipeline for which runs are created when all
     dependent pipelines complete successfully.
    :type pipeline: ~azure.mgmt.datafactory.models.TriggerPipelineReference
    :param depends_on: Required. Dependent Pipelines.
    :type depends_on: list[~azure.mgmt.datafactory.models.PipelineReference]
    :param retry_policy: Retry policy that will be applied for failed pipeline
     runs.
    :type retry_policy: ~azure.mgmt.datafactory.models.RetryPolicy
    :param run_dimension: Required. Run Dimenstion property that needs to be
     emitted by dependent pipelines.
    :type run_dimension: str
    """

    _validation = {
        'runtime_state': {'readonly': True},
        'type': {'required': True},
        'pipeline': {'required': True},
        'depends_on': {'required': True},
        'run_dimension': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'description': {'key': 'description', 'type': 'str'},
        'runtime_state': {'key': 'runtimeState', 'type': 'str'},
        'annotations': {'key': 'annotations', 'type': '[object]'},
        'type': {'key': 'type', 'type': 'str'},
        'pipeline': {'key': 'pipeline', 'type': 'TriggerPipelineReference'},
        'depends_on': {'key': 'typeProperties.dependsOn', 'type': '[PipelineReference]'},
        'retry_policy': {'key': 'typeProperties.retryPolicy', 'type': 'RetryPolicy'},
        'run_dimension': {'key': 'typeProperties.runDimension', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ChainingTrigger, self).__init__(**kwargs)
        self.pipeline = kwargs.get('pipeline', None)
        self.depends_on = kwargs.get('depends_on', None)
        self.retry_policy = kwargs.get('retry_policy', None)
        self.run_dimension = kwargs.get('run_dimension', None)
        self.type = 'ChainingTrigger'