# -*- coding: utf-8 -*-
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.action import ActionBase


class ActionModule(ActionBase):
    """Run oauth_token and treat a successful result as no_log.

    The module returns a freshly issued bearer token. Marking the result
    _ansible_no_log makes Ansible censor it in callback output and
    ansible-runner/navigator artifacts, regardless of the task's no_log setting,
    while the registered variable keeps the real value for later tasks.
    """

    def run(self, tmp=None, task_vars=None):
        result = super(ActionModule, self).run(tmp, task_vars)
        result.update(self._execute_module(task_vars=task_vars, tmp=tmp))
        # Failures carry no token, so keep their messages visible for debugging.
        if not result.get('failed') and 'access_token' in result:
            result['_ansible_no_log'] = True
        return result
