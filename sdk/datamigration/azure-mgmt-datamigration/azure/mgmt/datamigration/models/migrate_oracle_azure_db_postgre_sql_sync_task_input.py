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


class MigrateOracleAzureDbPostgreSqlSyncTaskInput(Model):
    """Input for the task that migrates Oracle databases to Azure Database for
    PostgreSQL for online migrations.

    All required parameters must be populated in order to send to Azure.

    :param selected_databases: Required. Databases to migrate
    :type selected_databases:
     list[~azure.mgmt.datamigration.models.MigrateOracleAzureDbPostgreSqlSyncDatabaseInput]
    :param target_connection_info: Required. Connection information for target
     Azure Database for PostgreSQL
    :type target_connection_info:
     ~azure.mgmt.datamigration.models.PostgreSqlConnectionInfo
    :param source_connection_info: Required. Connection information for source
     Oracle
    :type source_connection_info:
     ~azure.mgmt.datamigration.models.OracleConnectionInfo
    """

    _validation = {
        'selected_databases': {'required': True},
        'target_connection_info': {'required': True},
        'source_connection_info': {'required': True},
    }

    _attribute_map = {
        'selected_databases': {'key': 'selectedDatabases', 'type': '[MigrateOracleAzureDbPostgreSqlSyncDatabaseInput]'},
        'target_connection_info': {'key': 'targetConnectionInfo', 'type': 'PostgreSqlConnectionInfo'},
        'source_connection_info': {'key': 'sourceConnectionInfo', 'type': 'OracleConnectionInfo'},
    }

    def __init__(self, **kwargs):
        super(MigrateOracleAzureDbPostgreSqlSyncTaskInput, self).__init__(**kwargs)
        self.selected_databases = kwargs.get('selected_databases', None)
        self.target_connection_info = kwargs.get('target_connection_info', None)
        self.source_connection_info = kwargs.get('source_connection_info', None)
