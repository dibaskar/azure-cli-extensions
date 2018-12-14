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


class WsfcDomainCredentials(Model):
    """Domain credentials for setting up Windows Server Failover Cluster for SQL
    availability group.

    :param cluster_bootstrap_account_password: Cluster bootstrap account
     password.
    :type cluster_bootstrap_account_password: str
    :param cluster_operator_account_password: Cluster operator account
     password.
    :type cluster_operator_account_password: str
    :param sql_service_account_password: SQL service account password.
    :type sql_service_account_password: str
    """

    _attribute_map = {
        'cluster_bootstrap_account_password': {'key': 'clusterBootstrapAccountPassword', 'type': 'str'},
        'cluster_operator_account_password': {'key': 'clusterOperatorAccountPassword', 'type': 'str'},
        'sql_service_account_password': {'key': 'sqlServiceAccountPassword', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(WsfcDomainCredentials, self).__init__(**kwargs)
        self.cluster_bootstrap_account_password = kwargs.get('cluster_bootstrap_account_password', None)
        self.cluster_operator_account_password = kwargs.get('cluster_operator_account_password', None)
        self.sql_service_account_password = kwargs.get('sql_service_account_password', None)