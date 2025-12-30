from PIL import Image
import io


ALLOWED_FORMATS = ["JPEG", "PNG"]
MAX_SIZE = (1024, 1024)


def validate_and_prepare_image(image_path: str) -> bytes:
    """
    Validates image format and resizes if necessary.
    Returns image bytes suitable for API upload.
    """
    try:
        image = Image.open(image_path)
    except Exception:
        raise ValueError("Invalid image file.")

    if image.format not in ALLOWED_FORMATS:
        raise ValueError("Only JPG and PNG images are supported.")

    image.thumbnail(MAX_SIZE)

    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format=image.format)
    return img_byte_arr.getvalue()
