import tempfile

from fastapi import Depends, Form, UploadFile
from fastapi.exceptions import HTTPException
from starlette.responses import FileResponse, Response
from pydub import AudioSegment

from database.db_sync import get_session


async def create_audio(
        uploadfile: UploadFile, user_id: int = Form(), uuid: str = Form(),
        session=Depends(get_session)
):
    if uploadfile.content_type not in ['audio/wave', 'audio/wav', 'audio/x-wav']:
        raise HTTPException(422, detail="Invalid file type. Only .wav")

    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
        AudioSegment.from_file_using_temporary_files(uploadfile.file).export(f, format='mp3')
        return FileResponse(f.name,
                            filename=f.name.split('/')[-1],
                            media_type="application/octet-stream")



async def get_audio():
    return FileResponse("public/index.html",
                        filename="mainpage.html",
                        media_type="application/octet-stream")
