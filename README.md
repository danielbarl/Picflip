# Picflip Image Converter

Picflip is a simple and efficient script for converting images to WebP format with optional resizing and quality adjustment.

## Installation

### Windows

1. Install necessary prerequisites:
    ```sh
    pip install argparse && pip install pillow
    ```
2. Add the Script Directory to Your PATH Variable:
    - Press <kbd>WIN</kbd> and type `env`
    - Click on <kbd>Edit the system environment variables</kbd>
    - Click on <kbd>Environment Variables...</kbd>
    - Under "System variables", find and select the Path variable, then click <kbd>Edit...</kbd>
    - Click <kbd>New</kbd> and add the directory where the script is located
    - Click <kbd>OK</kbd> to close all dialog boxes
3. Use the Script without the File Extension (picflip --help)
    - Append the `PATHEXT` system environment variable with `.py`
    - To do this, under "System variables", find and select the `PATHEXT` variable, then click <kbd>Edit...</kbd>
    - Add `.PY` to the list (ensure each extension is separated by a semicolon)
    - Click <kbd>OK</kbd> to close all dialog boxes
    - Verify the change by running `echo %PATHEXT%` in the Command Prompt. The output shoudl look something like that `.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC;.PY`


## Usage

To see the available options and usage instructions, run:

```sh
picflip --help
```

### Example Commands

- Convert an image to WebP format with full size and full quality:
    ```sh
    picflip input.jpg output.webp
    ```
- Convert an image with specific width (800px) and quality (80%):
    ```sh
    picflip input.png output.webp --width 800 --quality 80
    ```

