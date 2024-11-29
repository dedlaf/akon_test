from typing import List

from db.sqlite import get_db
from fastapi import APIRouter, Depends, HTTPException
from models.models import Customer, Traffic
from schemas.schemas import CustomerTraffic, TrafficQuery
from sqlalchemy import func
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_model=List[CustomerTraffic])
async def get_traffic(
    db: Session = Depends(get_db),
    query: TrafficQuery = Depends()
):
    filters = [
        Customer.name == query.customer_name if query.customer_name else None,
        Traffic.date >= query.start_date if query.start_date else None,
        Traffic.date <= query.end_date if query.end_date else None,
        Traffic.ip == query.ip if query.ip else None,
    ]

    filters = [f for f in filters if f is not None]

    query = (
        db.query(
            Customer.name, func.sum(Traffic.received_traffic).label("total_traffic")
        )
        .join(Traffic)
        .filter(*filters)
        .group_by(Customer.name)
    )

    results = query.all()

    if not results:
        raise HTTPException(status_code=404, detail="No data found")

    return results
