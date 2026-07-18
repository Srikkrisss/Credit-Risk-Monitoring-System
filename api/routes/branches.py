from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.database import get_db
from api.crud import get_branches, get_branch
from api.schemas import BranchResponse

router = APIRouter(
    prefix="/branches",
    tags=["Branches"]
)


@router.get("/", response_model=list[BranchResponse])
def read_branches(db: Session = Depends(get_db)):
    return get_branches(db)


@router.get("/{branch_id}", response_model=BranchResponse)
def read_branch(branch_id: int,
                db: Session = Depends(get_db)):
    return get_branch(db, branch_id)