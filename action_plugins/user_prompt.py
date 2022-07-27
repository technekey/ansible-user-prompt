# code from plugins/action/normal.py
# (comments and most blank lines have been removed for brevity)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import json
import os
import sys
import termios
import tty
from os import isatty

from ansible.plugins.action import ActionBase
from ansible.utils.vars import merge_hash

try:
    from __main__ import display
except ImportError:
    from ansible.utils.display import Display
    display = Display()

class ActionModule(ActionBase):
   
    
   
    #user should provide these values 
    user_input_args = ['prompt','passing_response','abort_response']

    #these are the default values
    default_prompt = "Do you want to continue with the playbook execution?([yY]|[nN]|yes|YES|no|NO)?"
    default_passing_response = ['y','Y','yes','YES']
    default_abort_response = ['n','N','no','NO']
        
    BYPASS_HOST_LOOP = True

    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = dict()

        for arg in self._task.args:
            if arg not in self.user_input_args:
                return {"failed": True, "msg": "'%s' is not a valid option in user_prompt" % arg}
        
        #if the user has not provided prompt, fallback to default prompt
        if self._task.args.get('prompt') == None:
            prompt = self.default_prompt
        else:
            prompt = self._task.args.get('prompt')
     
        # if the user has not provided the passing responses, fallback to default passing responses
        if self._task.args.get('passing_response') == None:
            passing_response = self.default_passing_response
        else:
            passing_response = self._task.args.get('passing_response')

        # if the user has not provided the abort responses, fallback to default abort responses
        if self._task.args.get('abort_response') == None:
            abort_response = self.default_abort_response
        else:
            abort_response = self._task.args.get('abort_response')

        result = super(ActionModule, self).run(tmp, task_vars)
        #set the default values
        result.update(
            dict(
                changed=False,
                failed=False,
                msg='',
                skipped=False
            )
        )        

        #this is done to prevent EOF error while reading from stdin
        sys.stdin = open("/dev/tty")

        while True:
            user_response = input(f'{prompt}')
            if user_response in passing_response:
                return {"failed": False, "msg": f"Prompt response passed"}
                    
            elif user_response in abort_response:
                return {"failed": True, "msg": "User selected to abort."}
            else:
                print(f'Invalid response!, expecting one from {str(passing_response)} or {str(abort_response)}')


