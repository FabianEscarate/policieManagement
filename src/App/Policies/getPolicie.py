from src.App.Policies.Domain.Policie import Policie
from src.Context.Repository.Policie.policieRepository import policieRepository

class getPolicieById():

    repository = policieRepository()

    def run(self, idPolicie:str) -> Policie | None:
        policie = self.repository.getPolicieById(idPolicie)
        if not policie:
            return {"code": 5004, "message": "policie not found"}
        return policie