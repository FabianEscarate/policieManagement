from src.App.Policies.Domain.Policie import Policie
from src.Context.Repository.Policie.policieRepository import policieRepository

class getPolicies():

    repository = policieRepository()

    def run(self) -> Policie | None:
        return self.repository.getManyPolicies()