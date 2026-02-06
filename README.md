# ComfyUI Node Generators

This repository contains two Gradio applications for generating custom ComfyUI nodes:

## 1. Main Node Generator (app.py)

The main application provides advanced node generation capabilities:
- Text-to-Image Prompt Selector nodes
- Voice + Music Generator nodes
- Customizable parameters and prompts
- Real-time preview of generated code

### Features:
- Multiple prompt types with placeholders
- Customizable parameters (hair length/color, expressions, etc.)
- Voice and music generation nodes
- Live code preview

## 2. Complete Node Package Generator (create_node_package.py)

This application generates a complete ComfyUI node package as a ZIP file:
- Creates a complete folder structure with the node name
- Includes all necessary files (__init__.py, LICENSE.md, README.md)
- Packages everything in a downloadable ZIP file
- Ready for direct installation in ComfyUI

### Generated ZIP Structure:
```
MyNodeName.zip
├── MyNodeName/
│   ├── mynodename.py
│   ├── __init__.py
│   ├── LICENSE.md
│   └── README.md
```

## How to Run

### Using Batch Files:
1. `start_app.bat` - Runs the main node generator
2. `start_complete_generator.bat` - Runs the complete package generator

### Manual Execution:
1. Activate your conda environment
2. Install dependencies: `pip install gradio`
3. Run the desired application:
   - `python app.py` for the main generator
   - `python create_node_package.py` for the complete package generator

## Installation in ComfyUI

1. Download the generated ZIP file from the complete package generator
2. Extract it to your ComfyUI `custom_nodes` directory
3. Restart ComfyUI
4. The new node will appear in the specified category

## Requirements

- Python 3.10+
- Gradio
- Conda (for batch file execution)