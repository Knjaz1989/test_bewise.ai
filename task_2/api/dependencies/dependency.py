from tempfile import NamedTemporaryFile


def create_temp_file():
    with NamedTemporaryFile(suffix='.mp3') as tmp:
        yield tmp
