# purefa_hg - Manage Host Groups on Pure Storage FlashArray

## Synopsis

This module manages host groups on Pure Storage FlashArray.

## Requirements

- `purestorage` library (>= 1.19)
- Ansible (>= 2.9)

## Parameters

| Parameter             | Required | Default     | Choices            | Description                                           |
|-----------------------|----------|-------------|--------------------|-------------------------------------------------------|
| `state`               | No       | `"present"` | `present`, `absent`| The desired state of the resource.                    |
| `hosts`               | Yes      |             |                    | List of hosts to add to or remove from the host group |
| `name`                | Yes      |             |                    | The name of the resource.                             |
| `connection_info`     | Yes      |             |                    | Configuration settings for the gateway.               |
| `storage_system_info` | Yes      |             |                    | Configuration settings for the storage.               |

**Connection Info Object**

| Parameter   | Required | Default | Choices | Description                |
|-------------|----------|---------|---------|----------------------------|
| `address`   | Yes      |         |         | The IP address of gateway. |
| `api_token` | Yes      |         |         | The token.                 |

## Notes

- This module requires the purestorage Python library to be installed.
- If the hosts parameter is not provided when state=present, the host group will be created without any hosts.

## Examples

### Ensure a host group exists

```yaml
- name: Create host group hg1
  purefa_hg:
    name: hg1
    state: present
    hosts:
      - host1
      - host2
```

### Ensure a host group does not exist

```yaml
- name: Delete host group hg1
  purefa_hg:
    name: hg1
    state: absent
```

## Return Values

| Key         | Returned             | Description                       |
|-------------|----------------------|-----------------------------------|
| `changed`   | always               | Whether the module made any changes |
| `hostgroup` | When `state=present` | Information about the host group |
| `msg`       | When `state=absent`  | Message about the host group deletion|

### Example Return Value

**When state=present**

```yaml
{
  "changed": true,
  "hostgroup": {
    "name": "hg1",
    "hosts": ["host1", "host2", "host3", "host4"]
  }
}
```

**When state=absent**

```yaml
{
  "changed": true,
  "msg": "Host group hg1 deleted"
}
```

**When there is an error**

```yaml
{
  "changed": false,
  "msg": "Invalid parameter value",
  "exception": "InvalidParameterError"
}
```
