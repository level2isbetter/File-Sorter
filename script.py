import os
import shutil

dir_path = os.path.dirname(os.path.realpath(__file__))

files = os.listdir(dir_path)

for file in files:
    file_ext = os.path.splitext(file)[1][1:]

    if file_ext in ['rar', 'zip', '7z']:
        if not os.path.exists(os.path.join(dir_path, 'rar')):
            os.makedirs(os.path.join(dir_path, 'rar'))

        if os.path.isfile(file):
            shutil.move(os.path.join(dir_path, file), os.path.join(dir_path, 'rar', file))
    elif file_ext in ['png', 'jpg', 'jpeg', 'gif']:
        if not os.path.exists(os.path.join(dir_path, 'images')):
            os.makedirs(os.path.join(dir_path, 'images'))

        if os.path.isfile(file):
            shutil.move(os.path.join(dir_path, file), os.path.join(dir_path, 'images', file))