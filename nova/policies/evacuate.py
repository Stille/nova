# Copyright 2016 Cloudbase Solutions Srl
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from oslo_policy import policy

from nova.policies import base


BASE_POLICY_NAME = 'os_compute_api:os-evacuate'
POLICY_ROOT = 'os_compute_api:os-evacuate:%s'


evacuate_policies = [
    policy.RuleDefault(
        name=POLICY_ROOT % 'discoverable',
        check_str=base.RULE_ANY),
    base.create_rule_default(
        BASE_POLICY_NAME,
        base.RULE_ADMIN_API,
        "Evacuate a server from a failed host to a new host",
        [
            {
                'path': '/servers/{server_id}/action (evacuate)',
                'method': 'POST'
            }
        ]),
]


def list_rules():
    return evacuate_policies
