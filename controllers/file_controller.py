from fastapi import APIRouter
from fastapi import File, UploadFile

router = APIRouter()


@router.post("/upload")
def upload_large_file(file: UploadFile = File(...)):
    print(file.filename)
    return None
