import argparse
import os
import logging
from PIL import Image
from typing import Optional

SUPPORTED_FORMATS = ['JPEG', 'PNG', 'BMP', 'GIF', 'WEBP']

def setup_logging(debug: bool) -> None:
    level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(format='%(levelname)s: %(message)s', level=level)

def is_supported_format(input_file: str) -> bool:
    try:
        with Image.open(input_file) as img:
            if img.format not in SUPPORTED_FORMATS:
                logging.warning(f"Unsupported file format: {img.format}. Supported formats are: {', '.join(SUPPORTED_FORMATS)}")
                return False
            return True
    except Exception as e:
        logging.error(f"Error opening image {input_file}: {e}")
        return False

def convert_to_webp(input_file: str, output_file: str, width: Optional[int] = None, quality: int = 100, remove_metadata: bool = False) -> None:
    try:
        with Image.open(input_file) as img:
            if width:
                height = int((width / img.width) * img.height)
                img = img.resize((width, height), Image.LANCZOS)
                logging.debug(f"Resized image to {width}x{height}")
            if remove_metadata:
                img.info = {}  # Remove metadata
            img.save(output_file, 'webp', quality=quality)
            logging.info(f'Converted {input_file} to {output_file} with quality {quality}')
    except Exception as e:
        logging.error(f"Error processing image {input_file}: {e}")

def process_directory(input_dir: str, output_dir: str, width: Optional[int] = None, quality: int = 100, remove_metadata: bool = False) -> None:
    os.makedirs(output_dir, exist_ok=True)
    for root, _, files in os.walk(input_dir):
        for file in files:
            input_file = os.path.join(root, file)
            if is_supported_format(input_file):
                relative_path = os.path.relpath(root, input_dir)
                output_path = os.path.join(output_dir, relative_path)
                os.makedirs(output_path, exist_ok=True)
                output_file = os.path.join(output_path, f"{os.path.splitext(file)[0]}.webp")
                convert_to_webp(input_file, output_file, width, quality, remove_metadata)

def main() -> None:
    parser = argparse.ArgumentParser(description='Convert JPG or PNG images to WebP format')
    parser.add_argument('input', help='Input JPG or PNG file or directory')
    parser.add_argument('output', nargs='?', help='Output WebP file or directory')
    parser.add_argument('--width', type=int, help='Width of the output image (maintain aspect ratio)', default=None)
    parser.add_argument('--quality', type=int, help='Quality of the output image', default=100)
    parser.add_argument('--remove-metadata', action='store_true', help='Remove metadata from images')
    parser.add_argument('--debug', action='store_true', help='Enable debug output')

    args = parser.parse_args()
    setup_logging(args.debug)

    logging.debug(f"Arguments parsed: {args}")

    if os.path.isdir(args.input):
        output_dir = args.output if args.output else os.path.join(args.input, "webp")
        process_directory(args.input, output_dir, args.width, args.quality, args.remove_metadata)
    else:
        output_file = args.output if args.output else os.path.splitext(args.input)[0] + '.webp'
        if is_supported_format(args.input):
            convert_to_webp(args.input, output_file, args.width, args.quality, args.remove_metadata)

    logging.info("Finished processing")

if __name__ == "__main__":
    main()
