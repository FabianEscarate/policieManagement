from src.App.Policies.Domain.Policie import Policie
from src.Context.Repository.Policie.policieRepository import policieRepository

class addPolicie():

    repository = policieRepository()

    def run(self, policie:Policie):
        return self.repository.addPolicie(policie)