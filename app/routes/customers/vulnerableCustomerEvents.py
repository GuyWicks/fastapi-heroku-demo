from fastapi import APIRouter, Depends, HTTPException
from app.models.user import User, get_current_active_user

router = APIRouter()


@router.get("/{customerId}/vulnerableCustomerEvents")
async def read_vulnerableCustomerEvents(
    customerId: str,
    current_user: User = Depends(get_current_active_user)
):
    return


@router.get("/vulnerableCustomerEvents/thirdPartyUpdates")
async def read_vulnerable_customer_cvents_third_party_updates(
    current_user: User = Depends(get_current_active_user)
):
    return


@router.put("/{customerId}/vulnerableCustomerEvents/{eventType}")
async def put_vulnerable_customer_cvents_third_party_updates(
    customerId: str,
    eventType: str,
    current_user: User = Depends(get_current_active_user)
):
    return
