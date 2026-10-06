from dataclasses import asdict
from app.models.policy import Policy

from app.repositories.policy_repository import PolicyRepository


class PolicyService:

    def __init__(self, repository: PolicyRepository):
        self.repository = repository

    def get_all_policies(self):
        policies = self.repository.get_all()
        return [asdict(policy) for policy in policies]

    def get_policy_by_id(self, id:int):
        policy=self.repository.get_policy(id)
        return asdict(policy)

    def create_policy(self , policy:Policy):
        return self.repository.create_policy(policy)

    def update_policy(self, id:int,policy:Policy):
        policy =self.repository.update_policy(id,policy)
        return asdict(policy)

    def delete_policy(self,id:int):
        deletedcount=self.repository.delete_policy(id)
        return deletedcount