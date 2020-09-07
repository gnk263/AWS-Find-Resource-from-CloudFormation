import sys
import boto3
from typing import List, Dict

cfn = boto3.client('cloudformation')


def finder(target_resource_id):
    stacks = get_stacks()
    found = False

    for stack in stacks:
        stack_name = stack['StackName']
        resources = get_stack_resources(stack_name)

        for item in resources:
            physical_resource_id = item['PhysicalResourceId']
            resource_type = item['ResourceType']
            if target_resource_id in physical_resource_id:
                print(f'{stack_name}: {resource_type}, {physical_resource_id}')
                found = True
    
    if found is False:
        print(f'{target_resource_id} is not found in CloudFormation resources.')

def get_stacks(token: str=None) -> List[Dict]:
    """スタック一覧を取得する"""
    option = {
        'StackStatusFilter': [
            'CREATE_COMPLETE',
            'UPDATE_COMPLETE',
            'ROLLBACK_COMPLETE'
        ]
    }

    if token is not None:
        option['NextToken'] = token

    res = cfn.list_stacks(**option)
    stacks = res.get('StackSummaries', [])

    if 'NextToken' in res:
        stacks += get_stacks(res['NextToken'])
    return stacks


def get_stack_resources(stack_name: str, token: str=None) -> List[Dict]:
    """指定したスタックのリソース一覧を取得する"""
    option = {
        'StackName': stack_name
    }

    if token is not None:
        option['NextToken'] = token

    res = cfn.list_stack_resources(**option)
    resources = res.get('StackResourceSummaries', [])

    if 'NextToken' in res:
        resources += get_stack_resources(res['NextToken'])
    return resources


if __name__ == "__main__":
    args = sys.argv
    if len(args) == 2:
        finder(args[1])
