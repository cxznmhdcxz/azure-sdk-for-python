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


class JobsSummary(Model):
    """Summary of the replication job data for this vault.

    :param failed_jobs: Count of failed jobs.
    :type failed_jobs: int
    :param suspended_jobs: Count of suspended jobs.
    :type suspended_jobs: int
    :param in_progress_jobs: Count of in-progress jobs.
    :type in_progress_jobs: int
    """

    _attribute_map = {
        'failed_jobs': {'key': 'failedJobs', 'type': 'int'},
        'suspended_jobs': {'key': 'suspendedJobs', 'type': 'int'},
        'in_progress_jobs': {'key': 'inProgressJobs', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(JobsSummary, self).__init__(**kwargs)
        self.failed_jobs = kwargs.get('failed_jobs', None)
        self.suspended_jobs = kwargs.get('suspended_jobs', None)
        self.in_progress_jobs = kwargs.get('in_progress_jobs', None)