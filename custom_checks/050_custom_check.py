from typing import Dict, List, Any

from checkov.common.util.type_forcers import force_list
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck
from checkov.common.models.enums import CheckResult, CheckCategories


class FailingCheck(BaseResourceCheck):
    def __init__(self) -> None:
        name = 'test, should fail'
        id = "FAILING_CHECK"
        supported_resources = ["AWS::S3::BucketPolicy"]
        categories = [CheckCategories.ENCRYPTION]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf: Dict[str, Any]) -> CheckResult:
        return CheckResult.FAILED


check = FailingCheck()
