from fastapi import APIRouter, Depends

from app.web.schemas import ImportDataResult, FetchBrands, Brand
from app.web.dependencies import (
    make_import_data_service, 
    make_fetch_brands_service
)
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


@router.get(
    '/brands',
    summary='Fetch brands',
    description='Fetch brands stored in DB',
    response_model=FetchBrands
)
async def import_data(
    service: ImportBrandsService = Depends(make_fetch_brands_service)
) -> ImportDataResult:
    
    brands = service()
    return FetchBrands(brands=[Brand(**brand) for brand in brands])
