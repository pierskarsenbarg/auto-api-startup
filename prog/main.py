import sys
import json
import pulumi
from pulumi import automation as auto
from pulumi_azure_native import resources


def pulumi_program():
    resource_group = resources.ResourceGroup("resource_group")


def main():
    project_name = "pierstest"
    stack_name = "dev"

    stack = auto.create_or_select_stack(stack_name=stack_name,
                                    project_name=project_name,
                                    program=pulumi_program)
    
    stack.workspace.install_plugin("azure-native", "v2.50.1")
    stack.set_config("azure-native:location", auto.ConfigValue(value="uksouth"))
    stack.up(on_output=print)

    #stack.destroy(on_output=print)

if __name__ == '__main__':
    main()