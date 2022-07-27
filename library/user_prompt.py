#!/usr/bin/python
DOCUMENTATION = '''
---
module: prompt_user
short_description: This module would prompt the user for Yes/NO and on exit the playbook when NO is selected.

version_added: "2.8"
description:
    - "Sometimes the playbook developer wants to force the user to make an educated decision of executing the playbook"
    - "var_prompts" does the job but have several restrictions, like the usage of variables in the prompt, etc"
     - "This module is flexible and can be called from any place of the playbook"
options:
    prompt:
        description:
            - The prompt string
        required: true
    passing_response:
        description:
            - A list of inputs to let the playbook proceed with the execution
        required: optional
    abort_response:
        description:
            - A list of inputs to let the playbook abort the execution
        required: optional
author:
    - https://technekey.com
examples:
- hosts: localhost
  gather_facts: False
  vars:
    activity: "deletion of cluster"
  tasks: 
  - name: "Prompt for user response"
    user_prompt:
      prompt: "Do you want to continue with {{ activity}}?(y/n)?"
      passing_response: ['y','yes']
      abort_response: ['n','N','no','NO']

  - name: "Task next to the prompt"
    debug:
      msg: "Hello, user agrees to run me!"

- hosts: localhost
  gather_facts: False
  tasks:
  - name: "Task in another play "
    debug:
      msg: "Hello from another play!"

'''

