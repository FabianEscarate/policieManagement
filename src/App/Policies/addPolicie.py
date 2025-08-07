from src.App.Policies.Domain.Policie import Policie
from src.Context.Repository.Policie.policieRepository import policieRepository

class addPolicie():

    repository = policieRepository()

    def run(self, policie:Policie):
        idPolicie = policie.id
        checkPolicie = self.repository.getPolicieById(idPolicie)
        if checkPolicie:
            return {"code":5001,"message": 'policie already exist'}
        return self.repository.addPolicie(policie)