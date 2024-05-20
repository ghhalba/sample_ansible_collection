# Hello World Ansible Collection Plugins

## Overview

This directory contains plugins for the "Hello World" Ansible collection. Plugins are the core components of an Ansible collection and extend the functionality of Ansible by providing reusable units of work, such as modules, lookups, filters, and more.

## Modules

### sample_module.py

**Description**: The `sample_module` module prints a "Hello, World!" message or a custom greeting.

**Options**:

| Parameter | Required | Default   | Choices | Description                      |
|-----------|----------|-----------|---------|----------------------------------|
| `name`    | No       | `"World"` |         | The name to use in the greeting. |

**Example Usage**:

```yaml
- name: Print Hello World
  my_namespace.hello_world.hello:
    name: "Ansible User"
