# Ansible custom 'blue' test plugin
from ansible.module_utils.common.text.converters import to_native

def is_blue(string):
    """Check if the given string is 'blue'."""
    return to_native(string).lower() == 'blue'

class TestModule:
    """Ansible custom test plugin."""

    def tests(self):
        return {
            'blue': is_blue,
        }