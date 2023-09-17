from fastapi import APIRouter, Depends

from app.web.schemas import ImportDataResult
from app.web.dependencies import make_import_data_service
from app.core.services import ImportBrandsService


router = APIRouter()


@router.post(
    '/import-data',
    summary='Import data',
    description='Starts importing data proccess',
    response_model=ImportDataResult
)
async def import_data(
    service: ImportBrandsService = Depends(make_import_data_service)
) -> ImportDataResult:
    
    service()
    return ImportDataResult(details=f'Importing data')
