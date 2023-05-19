from tempfile import NamedTemporaryFile

from fastapi import Depends, Form, UploadFile
from fastapi.exceptions import HTTPException
from starlette.responses import FileResponse
from pydub import AudioSegment

from database.db_sync import get_session
from database.handlers.audio_handlers import select_audio, add_audio


def create_temp_file():
    with NamedTemporaryFile(suffix='.mp3') as tmp:
        yield tmp


async def create_audio(
    uploadfile: UploadFile,
    user_id: int = Form(),
    uuid: str = Form(),
    tempfile=Depends(create_temp_file),
    session=Depends(get_session)
):
    if uploadfile.content_type not in ['audio/wave', 'audio/wav', 'audio/x-wav']:
        raise HTTPException(422, detail="Invalid file type. Only .wav")

    AudioSegment.from_file_using_temporary_files(uploadfile.file).export(
        tempfile, format='mp3')
    old_name = uploadfile.filename
    new_name = old_name[0: old_name.rfind('.')]
    audio_id = await add_audio(
        session, new_name, tempfile.file.read(), user_id
    )
    return f"http://localhost:8000/record/?id={audio_id['id']}&user_id={user_id}"


async def get_audio(
    user_id: int,
    id: int,
    temp_file: NamedTemporaryFile = Depends(create_temp_file),
    session=Depends(get_session)
):
    audio = await select_audio(session, user_id, id)
    temp_file.write(audio.data)
    return FileResponse(temp_file.name,
                        filename=audio.name,
                        media_type="application/octet-stream")
