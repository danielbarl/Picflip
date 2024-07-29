import argparse
from PIL import Image

SUPPORTED_FORMATS = ['JPEG', 'PNG']

def is_supported_format(input_file):
    try:
        image = Image.open(input_file)
        format = image.format
        if format not in SUPPORTED_FORMATS:
            print(f"Unsupported file format: {format}. Supported formats are: {', '.join(SUPPORTED_FORMATS)}")
            return False
        return True
    except Exception as e:
        print(f"Error opening image: {e}")
        return False

def convert_to_webp(input_file, output_file, width=None, quality=80, debug=False):
    if debug:
        print(f"Opening image file: {input_file}")
    try:
        image = Image.open(input_file)
        if debug:
            print(f"Image opened: {input_file}, format: {image.format}, size: {image.size}")
    except Exception as e:
        print(f"Error opening image: {e}")
        return

    if width:
        height = int((width / image.width) * image.height)
        if debug:
            print(f"Resizing image to width: {width}, height: {height}")
        image = image.resize((width, height), Image.LANCZOS)
        if debug:
            print(f"Image resized: new size: {image.size}")

    try:
        if debug:
            print(f"Saving image to {output_file} with quality {quality}")
        image.save(output_file, 'webp', quality=quality)
        print(f'Converted {input_file} to {output_file} with quality {quality}')
    except Exception as e:
        print(f"Error saving image: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert JPG or PNG images to WebP format')
    parser.add_argument('input', help='Input JPG or PNG file')
    parser.add_argument('output', help='Output WebP file')
    parser.add_argument('--width', type=int, help='Width of the output image (maintain aspect ratio)', default=None)
    parser.add_argument('--quality', type=int, help='Quality of the output image', default=80)
    parser.add_argument('--debug', action='store_true', help='Enable debug output')

    args = parser.parse_args()

    if args.debug:
        print("Parsing arguments...")
        print(f"Arguments parsed: input={args.input}, output={args.output}, width={args.width}, quality={args.quality}")

    if is_supported_format(args.input):
        convert_to_webp(args.input, args.output, args.width, args.quality, args.debug)

    if args.debug:
        print("Finished processing")
