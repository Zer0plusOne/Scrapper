# Metadata Extractor

This repository contains a Python script for extracting metadata from different types of files, including images, PDFs, audio files, and Word documents. The script allows users to view metadata directly in the console or save it in multiple formats (JSON, CSV, XML, or TXT) based on your preference.

## Author

Created by [Zer0plusOne](https://github.com/Zer0plusOne)

## Overview

This is the starter version of the project, aimed to provide a simple and versatile way to analyze and save metadata for different file types. The script identifies the file type based on its extension and processes it accordingly. It supports a wide range of formats, including `.jpg`, `.jpeg`, `.png`, `.pdf`, `.mp3`, `.wav`, `.flac`, and `.docx`. Unsupported formats will notify the user.

### Key Features

- **File Metadata Extraction**: Retrieve metadata from supported file types.
- **Output Options**: Save metadata in JSON, CSV, XML, or TXT format.
- **Command Line Interface**: Execute the script directly from the command line, passing file paths and output preferences as arguments.

## Clonation

Simply execute the following comand to clone this repository in your current directory:

```bash
git clone https://github.com/zer0plusone/Scrapper
```

Before going forward, remember to be inside the repository to use the program

```bash
cd Scrapper
```

## Installation

Give executable permisions to only the bash script:

```bash
chmod +x requirements.sh
```

Run the following bash script to install all necessary dependencies:

```bash
./requirements.sh
```

## Usage

To run the script, use:

```bash
python3 Scrapper.py <file_path> [-o <format>]
```

### Arguments

- `<file_path>`: The path to the file for which metadata needs to be extracted.
- `-o <format>`: Optional output format, can be `json`, `csv`, `xml`, or `txt`.

Example:

```bash
python3 Scrapper.py sample.pdf -o json
```

## Contributions

Contributions are welcome! Feel free to open issues or submit pull requests to improve this project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
