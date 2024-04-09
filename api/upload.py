import os
import random
import string
from .app import app
from flask import request, make_response, send_from_directory, jsonify
from os import path
from PIL import Image
from math import floor
import pillow_avif  # add support for avif image files


UPLOAD_FOLDER = "./images"
ALLOWED_FILE_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "avif", "webp"}
MAX_IMAGE_SIZE = 2048


def is_allowed_file(filename: str) -> bool:
    return (
        "." in filename
        and filename.rsplit(sep=".", maxsplit=1)[1].lower() in ALLOWED_FILE_EXTENSIONS
    )


def generate_unique_filename():
    def get_random_filename():
        random_strings = [
            "".join(random.choices(string.ascii_lowercase + string.digits, k=4))
            for i in range(3)
        ]

        return "_".join(random_strings) + ".webp"

    filename = get_random_filename()

    # for the unlikely case that two files would have the same generated filename
    while filename in os.listdir("./images"):
        filename = get_random_filename()

    return filename


def resize_image(image: Image.Image):
    if any(side > MAX_IMAGE_SIZE for side in image.size):
        resizing_factor = min(
            MAX_IMAGE_SIZE / image.width, MAX_IMAGE_SIZE / image.height
        )

        new_size = (
            floor(image.width * resizing_factor),
            floor(image.height * resizing_factor),
        )

        return image.resize(new_size, resample=Image.LANCZOS)

    return image


def save_file(requestFile):
    pil_image = Image.open(requestFile)

    # resize image if it's bigger than the max size
    pil_image = resize_image(pil_image)

    filename = generate_unique_filename()
    path = UPLOAD_FOLDER + "/" + filename

    # save in webp format
    pil_image.save(path, "webp")

    return filename


@app.post("/upload")
def upload_file():
    if "file" not in request.files:
        # bad request
        return make_response("No file part", 400)
    file = request.files["file"]

    if file.filename == "":
        return make_response("No selected file", 400)

    if is_allowed_file(file.filename):
        # filename = secure_filename(file.filename)
        # file.save(path.join(app.config["UPLOAD_FOLDER"], filename))

        generated_filename = save_file(file)

        return jsonify(
            {
                "filename": generated_filename,
                "link": f"http://localhost:5000/uploads/" + generated_filename,
            }
        )

    # unsupported media type
    return make_response("File extension not supported", 415)


@app.get("/uploads/<filename>")
def get_uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)
