import os
import shutil
from fastapi import UploadFile
from datetime import datetime

def save_upload_file(upload_file: UploadFile, folder: str) -> str:
    os.makedirs(folder, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_extension = os.path.splitext(upload_file.filename)[1]
    filename = f"{timestamp}{file_extension}"
    
    file_path = os.path.join(folder, filename)
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)
    
    return filename