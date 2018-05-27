import os

def get_image_folder_zgl(instance, filename):
    path = "media/images/zgloszenia/"
    print(filename)
    ext = str(os.path.splitext(filename)[1])
    files = str(instance.id) + ext
    return os.path.join(path, files)

def get_image_folder_cat(instance, filename):
    path = "media/images/kategorie/"
    print(filename)
    ext = str(os.path.splitext(filename)[1])
    files = str(instance.id) + ext
    return os.path.join(path, files)

def get_file_name(value):
    tab = value.split('/')
    return tab[-1]

def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpeg', '.jpg', '.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension.')