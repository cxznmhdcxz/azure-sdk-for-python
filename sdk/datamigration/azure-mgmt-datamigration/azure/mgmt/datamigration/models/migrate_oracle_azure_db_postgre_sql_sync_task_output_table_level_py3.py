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

from .migrate_oracle_azure_db_postgre_sql_sync_task_output_py3 import MigrateOracleAzureDbPostgreSqlSyncTaskOutput


class MigrateOracleAzureDbPostgreSqlSyncTaskOutputTableLevel(MigrateOracleAzureDbPostgreSqlSyncTaskOutput):
    """MigrateOracleAzureDbPostgreSqlSyncTaskOutputTableLevel.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Result identifier
    :vartype id: str
    :param result_type: Required. Constant filled by server.
    :type result_type: str
    :ivar table_name: Name of the table
    :vartype table_name: str
    :ivar database_name: Name of the database
    :vartype database_name: str
    :ivar cdc_insert_counter: Number of applied inserts
    :vartype cdc_insert_counter: long
    :ivar cdc_update_counter: Number of applied updates
    :vartype cdc_update_counter: long
    :ivar cdc_delete_counter: Number of applied deletes
    :vartype cdc_delete_counter: long
    :ivar full_load_est_finish_time: Estimate to finish full load
    :vartype full_load_est_finish_time: datetime
    :ivar full_load_started_on: Full load start time
    :vartype full_load_started_on: datetime
    :ivar full_load_ended_on: Full load end time
    :vartype full_load_ended_on: datetime
    :ivar full_load_total_rows: Number of rows applied in full load
    :vartype full_load_total_rows: long
    :ivar state: Current state of the table migration. Possible values
     include: 'BEFORE_LOAD', 'FULL_LOAD', 'COMPLETED', 'CANCELED', 'ERROR',
     'FAILED'
    :vartype state: str or
     ~azure.mgmt.datamigration.models.SyncTableMigrationState
    :ivar total_changes_applied: Total number of applied changes
    :vartype total_changes_applied: long
    :ivar data_errors_counter: Number of data errors occurred
    :vartype data_errors_counter: long
    :ivar last_modified_time: Last modified time on target
    :vartype last_modified_time: datetime
    """

    _validation = {
        'id': {'readonly': True},
        'result_type': {'required': True},
        'table_name': {'readonly': True},
        'database_name': {'readonly': True},
        'cdc_insert_counter': {'readonly': True},
        'cdc_update_counter': {'readonly': True},
        'cdc_delete_counter': {'readonly': True},
        'full_load_est_finish_time': {'readonly': True},
        'full_load_started_on': {'readonly': True},
        'full_load_ended_on': {'readonly': True},
        'full_load_total_rows': {'readonly': True},
        'state': {'readonly': True},
        'total_changes_applied': {'readonly': True},
        'data_errors_counter': {'readonly': True},
        'last_modified_time': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'result_type': {'key': 'resultType', 'type': 'str'},
        'table_name': {'key': 'tableName', 'type': 'str'},
        'database_name': {'key': 'databaseName', 'type': 'str'},
        'cdc_insert_counter': {'key': 'cdcInsertCounter', 'type': 'long'},
        'cdc_update_counter': {'key': 'cdcUpdateCounter', 'type': 'long'},
        'cdc_delete_counter': {'key': 'cdcDeleteCounter', 'type': 'long'},
        'full_load_est_finish_time': {'key': 'fullLoadEstFinishTime', 'type': 'iso-8601'},
        'full_load_started_on': {'key': 'fullLoadStartedOn', 'type': 'iso-8601'},
        'full_load_ended_on': {'key': 'fullLoadEndedOn', 'type': 'iso-8601'},
        'full_load_total_rows': {'key': 'fullLoadTotalRows', 'type': 'long'},
        'state': {'key': 'state', 'type': 'str'},
        'total_changes_applied': {'key': 'totalChangesApplied', 'type': 'long'},
        'data_errors_counter': {'key': 'dataErrorsCounter', 'type': 'long'},
        'last_modified_time': {'key': 'lastModifiedTime', 'type': 'iso-8601'},
    }

    def __init__(self, **kwargs) -> None:
        super(MigrateOracleAzureDbPostgreSqlSyncTaskOutputTableLevel, self).__init__(**kwargs)
        self.table_name = None
        self.database_name = None
        self.cdc_insert_counter = None
        self.cdc_update_counter = None
        self.cdc_delete_counter = None
        self.full_load_est_finish_time = None
        self.full_load_started_on = None
        self.full_load_ended_on = None
        self.full_load_total_rows = None
        self.state = None
        self.total_changes_applied = None
        self.data_errors_counter = None
        self.last_modified_time = None
        self.result_type = 'TableLevelOutput'
