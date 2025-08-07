from src.App.Policies.Domain.Policie import Policie, policieStatus
from src.Context.Repository.Policie.policieRepository import policieRepository

class changeStatusPolicie():

    repository = policieRepository()

    def nextState(currentState:policieStatus):
        if currentState == policieStatus.issued:
            return policieStatus.active
        if currentState == policieStatus.active:
            return policieStatus.annulled
        if currentState == policieStatus.annulled:
            return policieStatus.annulled  

    def run(self, id: str, newState: policieStatus | None):
        policie = self.repository.getPolicieById(id)

        if not policie:
            return {"code":5004,"message": 'policie not found'}
        
        if not newState:
            policie.estado = changeStatusPolicie.nextState(policie.estado)
        elif newState:
            policie.estado = newState

        return self.repository.updatePolicie(id, policie)