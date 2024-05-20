# test_role

## Description

`test_role` is a simple Ansible role designed to demonstrate the structure and usage of roles within an Ansible collection. This role performs a basic task, such as creating a file with a specified content.

## Requirements

- Ansible >= 2.9

## Role Variables

### Default Variables

The following variables are defined in `defaults/main.yml`:

```yaml
# Path to the file to be created
test_role_file_path: "/tmp/hello_world.txt"

# Content to be written in the file
test_role_file_content: "Hello, World!"
