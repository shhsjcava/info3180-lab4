from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired

class UploadForm(FlaskForm):
    photo = FileField('Please upload Image here', validators=[FileRequired(''),FileAllowed(['jpg', 'png'], 'Images only!')
    ])