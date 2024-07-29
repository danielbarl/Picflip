# Picflip Image Converter

**Picflip** is a simple and efficient script for converting images to WebP format with optional resizing and quality adjustment.

## Installation

### Prerequisites

Ensure you have Python installed. You can download it from the [official Python website](https://www.python.org/).

### Dependencies

Ensure you have Python installed. Download it from the [official Python website](https://www.python.org/).

Install the required Python packages:

```sh
pip install argparse pillow
```

### Clone the Repository

```sh
git clone https://github.com/yourusername/picflip.git
cd picflip
```

### Setup on different OS

#### Windows 
Add the Script Directory to Your PATH Variable:

1. Press <kbd>WIN</kbd> and type `env`
2. Click on `Edit the system environment variables`
3. Click on `Environment Variables...`
4. Under "System variables", find and select the Path variable, then click `Edit...`
5. Click `New` and add the directory where the script is located
6. Confirm with `OK` to close all dialog boxes

#### macOS and Linux

Add the Script Directory to PATH:

1. Open the shell profile file:
    ```sh
    nano ~/.bashrc  # or use .zshrc, .profile depending on your shell
    ``` 
2. Add the following line to the end of the file:
    ```sh
    export PATH="$PATH:/path/to/picflip"
    ```
3. Source the profile to update the PATH:
    ```sh
    source ~/.bashrc # or the respective profile file
    ```


## Usage

To see the available options and usage instructions, run:

```sh
picflip --help
```

### Example commands

- Convert a single image to WebP format with full size and full quality:
    ```sh
    picflip input.jpg output.webp
    ```
- Convert a single image with specific width (800px) and quality (80%):
    ```sh
    picflip input.png output.webp --width 800 --quality 80
    ```
- Convert all images in a directory to WebP format with default settings:
    ```sh
    picflip C:\input_dir C:\output_dir
    ```
- Convert all images in a directory with specific width and quality, removing metadata:
    ```sh
    picflip C:\input_dir C:\output_dir --width 1024 --quality 75 --remove-metadata
    ```

## Features

- Supported Formats: JPEG, PNG, BMP, GIF, WEBP
- Resizing: Maintain aspect ratio when resizing images
- Quality Adjustment: Set the quality of the output WebP image
- Metadata Removal: Optionally remove metadata from images

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.