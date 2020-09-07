# AWS-Find-Resource-from-CloudFormation

AWSリソース名を入力すると、どのCloudFormationスタックで作成したのかを調べます。

Enter the name of an AWS resource to investigate which CloudFormation stack it was created in.

## install

```bash
pipenv install
```

## usage

### created AWS resource by CloudFormation

```bash
$ pipenv run python finder.py xxx-function
Chouseisan-Reminder-Stack: AWS::Lambda::Function, chouseisan-reminder-function
```

### created AWS resource by Manualy

```bash
$ pipenv run python finder.py zzz-function
zzz-function is not found in CloudFormation resources.
```
