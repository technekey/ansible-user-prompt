#### ansible-user-prompt

This repo contains a simple ansible action pugin to extend ansible by providing a custom user prompt with great customization options. 

#### Setup:
You must have two directories at the same level as your playbook. For example, both of the following directories will have a file called `user_prompt.py`; however, the content of those two files is **different**.
You must copy and paste the content of these files in respective directories to their corresponding directories. 


````
- action_plugins
- library
````
##### Setup Example:
In the following example, My playbook is ````example-1.yml````, so I have created ````action_plugins```` and ````library```` directory at the ****same level.****

````
tree
.
├── action_plugins
│   └── user_prompt.py   <---------+
├── example-1.yml                  |
├── example-2.yml                  |
├── example-3.yml                  | --------NAME must be same, but the content is different.
├── example-4.yml                  |
├── example-5.yml                  |
└── library                        |
    └── user_prompt.py  <----------+

2 directories, 7 files
````


The task may look as simple as:
````
  - name: "Prompt for user response"
    user_prompt:
````

OR it may use custom values

````
  - name: "Prompt for user response"
    user_prompt:
      prompt: "Do you want to continue with {{action}} of {{user}} user?(y/n)?"
      passing_response: ['y','yes']
      abort_response: ['n','no']
    vars:
      action: "deletion"
      user: "foobar"
````
#### Execution Example:

When incorrect input is supplied, the playbook would keep prompting until a right input is supplied. Later, "no" is provided causing playbook to abort.
````
ansible-playbook  example-1.yml 

PLAY [A sample playbook showing user prompt] ****************************************************************************************************************************************************************************************

TASK [Prompt for user response] *****************************************************************************************************************************************************************************************************
Do you want to continue with the playbook execution?([yY]|[nN]|yes|YES|no|NO)?saldnhasjkldhasl
Invalid response!, expecting one from ['y', 'Y', 'yes', 'YES'] or ['n', 'N', 'no', 'NO']
Do you want to continue with the playbook execution?([yY]|[nN]|yes|YES|no|NO)?no
fatal: [localhost]: FAILED! => {"changed": false, "msg": "User selected to abort."}

NO MORE HOSTS LEFT ******************************************************************************************************************************************************************************************************************

PLAY RECAP **************************************************************************************************************************************************************************************************************************
localhost                  : ok=0    changed=0    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0   

````
When "yes" is supplied to the playbook.

````
ansible-playbook  example-1.yml 

PLAY [A sample playbook showing user prompt] ****************************************************************************************************************************************************************************************

TASK [Prompt for user response] *****************************************************************************************************************************************************************************************************
Do you want to continue with the playbook execution?([yY]|[nN]|yes|YES|no|NO)?yes
ok: [localhost]

TASK [Task next to the prompt] ******************************************************************************************************************************************************************************************************
ok: [localhost] => {
    "msg": "Hello, user agrees to run me!"
}

PLAY RECAP **************************************************************************************************************************************************************************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

````

Example-2: Showing a custom string in the prompt
````
ansible-playbook  example-2.yml 

PLAY [A sample playbook showing custom input configured for prompt string and allowing/failing the prompt] **************************************************************************************************************************

TASK [Prompt for user response] *****************************************************************************************************************************************************************************************************
Do you want to continue with the playbook execution??? This once more...... ?(y/n)?y
ok: [localhost]

TASK [Task next to the prompt] ******************************************************************************************************************************************************************************************************
ok: [localhost] => {
    "msg": "Hello, user agrees to run me!"
}

PLAY RECAP **************************************************************************************************************************************************************************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
````

Example-3: When there multiple play present in the playbook, the subsequent play will also exit, unlike ````meta: end_play````

````
ansible-playbook  example-3.yml 
PLAY [A sample playbook showing when there are multiple play in the same playbook] **************************************************************************************************************************************************

TASK [Prompt for user response] *****************************************************************************************************************************************************************************************************
Do you want to continue with the playbook execution??? This once more...... ?(y/n)?n
fatal: [localhost]: FAILED! => {"changed": false, "msg": "User selected to abort."}

NO MORE HOSTS LEFT ******************************************************************************************************************************************************************************************************************

PLAY RECAP **************************************************************************************************************************************************************************************************************************
localhost                  : ok=0    changed=0    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0   
````

Example-4: Showing the prompt can be disable using when clause for `ci/cd` execution

````
ansible-playbook  example-4.yml  -e disable_prompt=True

PLAY [A sample playbook showing that prompt can be controlled by when clause] *******************************************************************************************************************************************************

TASK [Prompt for user response] *****************************************************************************************************************************************************************************************************
skipping: [localhost]

TASK [Task next to the prompt] ******************************************************************************************************************************************************************************************************
ok: [localhost] => {
    "msg": "Hello, user agrees to run me!"
}

PLAY RECAP **************************************************************************************************************************************************************************************************************************
localhost                  : ok=1    changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
````
#### more info:

https://technekey.com/user-prompt-in-ansible-playbook/
