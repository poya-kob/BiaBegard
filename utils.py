import os
import string
import random
import datetime


def get_file_name(filepath):
    size = 8
    chars = string.ascii_uppercase + string.digits
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    name = ''.join(random.choice(chars) for _ in range(size))
    return name, ext


def upload_image_path(instance, filename):
    date = datetime.datetime.now()
    name, ext = get_file_name(filename)
    new_name = f"{name}{ext}"
    if type(instance).__name__ == "Products":
        return f"product/{date.year}/{date.month}/{date.day}/{new_name}"
    elif type(instance).__name__ == "ProductsGalleries":
        return f"Products_Galleries/{date.year}/{date.month}/{date.day}/{new_name}"
    elif type(instance).__name__ == "Brands":
        return f"Brands/{date.year}/{date.month}/{date.day}/{new_name}"
