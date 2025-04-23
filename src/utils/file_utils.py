import os
import shutil
from fastapi import UploadFile
from datetime import datetime

def save_upload_file(upload_file: UploadFile, folder: str) -> str:
    # Create folder if it doesn't exist
    os.makedirs(folder, exist_ok=True)
    
    # Generate unique filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_extension = os.path.splitext(upload_file.filename)[1]
    filename = f"{timestamp}{file_extension}"
    
    # Create full file path
    file_path = os.path.join(folder, filename)
    
    # Save the file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)
    
    return filename