# sample_module.py

DOCUMENTATION = '''
---
module: sample_module
short_description: This is a sample module for demonstration.
version_added: "1.0.0"
description:
    - This is a detailed description of the sample module.
options:
    parameter_name:
        description:
            - This is the description of the parameter.
        required: true
        type: str
author:
    - Your Name (@yourGitHub)
'''

EXAMPLES = '''
- name: Sample task using sample_module
  sample_module:
    parameter_name: value
'''

RETURN = '''
output_name:
    description: The description of the output.
    returned: success
    type: str
    sample: 'output_value'
'''

from ansible.module_utils.basic import AnsibleModule

def run_module():
    module_args = dict(
        name=dict(type='str', required=True)
    )

    result = dict(
        changed=False,
        original_message='',
        message=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    name = module.params['name']
    result['original_message'] = name
    result['message'] = 'Hello, {0}!'.format(name)

    if module.check_mode:
        return result

    result['changed'] = True

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
