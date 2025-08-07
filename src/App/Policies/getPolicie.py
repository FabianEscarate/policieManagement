from src.App.Policies.Domain.Policie import Policie
from src.Context.Repository.Policie.policieRepository import policieRepository

class getPolicieById():

    repository = policieRepository()

    def run(self, idPolicie:str) -> Policie | None:
        return self.repository.getPolicieById(idPolicie)