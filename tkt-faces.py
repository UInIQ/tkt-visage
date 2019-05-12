from app import create_app, db
from app.models import User, Person, Program, Face, Image, ImageFace, ImageStatus

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db,
        'User': User,
        'Person': Person,
        'Face': Face,
        'Image': Image,
        'Program': Program,
        'ImgFace': ImageFace,
        'ImageStatus' : ImageStatus
    }