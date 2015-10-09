from wand.image import Image


def convert(source_file, destination_file):
    with Image(filename=source_file) as img:
        print(img.size)
        with img.convert('jp2') as img:
            img.save(filename=destination_file)
