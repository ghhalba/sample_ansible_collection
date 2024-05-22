# Hello World Ansible Collection

## Description

This is a simple Ansible collection that includes a "Hello World" module. The module prints "Hello, World!" to demonstrate the basics of creating and using a custom Ansible collection.

## Supported Platforms

- Pure Storage FlashArray with Purity 6.1.0 or later
- Certain modules and functionality require higher versions of Purity. Modules will inform you if your Purity version is not high enough to use a module.

## Requirements

- Ansible >= 2.9
- Python >= 3.15
- netaddr


## Idempotency
All modules are idempotent with the exception of modules that change or set passwords. Due to security requirements exisitng passwords can be validated against and therefore will always be modified, even if there is no change.

## Available Modules

- hv_lun - manages volumes
- hv_hostgroup - managers hostgroups

## Installation

### Installing the Collection

You can install this collection via Ansible Galaxy:

```bash
ansible-galaxy collection install ghhalba.sample_ansible_collection
```

## License

SomeLicense