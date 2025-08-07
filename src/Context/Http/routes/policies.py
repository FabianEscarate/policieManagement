from fastapi import APIRouter, status, HTTPException, Response
from uuid import UUID
from src.Context.Http.schemas.policiesPayload import createPolicie, Policie
from src.App.Policies.addPolicie import addPolicie
from src.App.Policies.getPolicie import getPolicieById

policieRoutes = APIRouter()


@policieRoutes.post("", status_code=status.HTTP_201_CREATED, response_model=Policie)
def postPolicie(policie: createPolicie):
    try:
        result = addPolicie().run(policie)
        return result
    except Exception as e:
        Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=e)
    
@policieRoutes.get("/{id}", status_code=status.HTTP_200_OK)
def getPolicie(id: UUID):
    policie = getPolicieById().run(id)
    if not policie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="policie not found")
    return policie
