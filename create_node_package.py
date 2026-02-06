import gradio as gr
import os
import zipfile
import json
from datetime import datetime
import re


def sanitize_filename(name):
    """Sanitize the node name to be a valid filename"""
    return re.sub(r'[^a-zA-Z0-9_-]', '_', name)


def generate_complete_node_package(node_name, category, prompts_list):
    """Generate a complete ComfyUI node package as a ZIP file"""
    # Validate inputs
    if not node_name.strip():
        raise gr.Error("Node name cannot be empty")
    
    if not prompts_list.strip():
        raise gr.Error("Please enter at least one prompt")
    
    # Sanitize the node name for use as filename
    sanitized_node_name = sanitize_filename(node_name)
    
    # Parse the prompts list
    prompts = [p.strip() for p in prompts_list.split('\n') if p.strip()]
    if not prompts:
        raise gr.Error("Please enter at least one valid prompt")
    
    # Create the main node file content
    node_content = f'''import random

class {node_name}:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {{
            "required": {{
                "select": ("INT", {{"default": 0, "min": 0, "max": {len(prompts)-1}, "step": 1}}),
                "mode": (["sequential", "random"], {{}}),
            }},
        }}

    RETURN_TYPES = ("STRING",)
    FUNCTION = "select_prompt"
    OUTPUT_NODE = True
    CATEGORY = "{category}"

    def select_prompt(self, select, mode):
        prompts = {json.dumps(prompts)}
        
        if mode == "random":
            selected_prompt = random.choice(prompts)
        else:  # sequential
            index = select % len(prompts)
            selected_prompt = prompts[index]
        
        return (selected_prompt,)


NODE_CLASS_MAPPINGS = {{
    "{node_name}": {node_name}
}}

NODE_DISPLAY_NAME_MAPPINGS = {{
    "{node_name}": "{node_name}"
}}
'''
    
    # Create the __init__.py file content
    init_content = f'''from .{sanitized_node_name.lower()} import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
'''
    
    # Create the LICENSE.md content
    license_content = '''MIT License

Copyright (c) 2023

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
    
    # Create the README.md content
    readme_content = f'''# {node_name}

A custom node for ComfyUI that allows selection of prompts from a predefined list.

## Features

- Sequential prompt selection
- Random prompt selection
- Configurable prompt list

## Installation

1. Copy this folder to your ComfyUI `custom_nodes` directory
2. Restart ComfyUI

## Usage

The node provides two modes:
- Sequential: Select prompts by index in order
- Random: Select a random prompt from the list

## License

This project is licensed under the MIT License.
'''
    
    # Create a temporary directory structure
    temp_dir = f"temp_{sanitized_node_name}"
    node_dir = os.path.join(temp_dir, sanitized_node_name)
    
    # Create directories
    os.makedirs(node_dir, exist_ok=True)
    
    # Write files to the directory
    with open(os.path.join(node_dir, f"{sanitized_node_name.lower()}.py"), 'w', encoding='utf-8') as f:
        f.write(node_content)
    
    with open(os.path.join(node_dir, '__init__.py'), 'w', encoding='utf-8') as f:
        f.write(init_content)
    
    with open(os.path.join(node_dir, 'LICENSE.md'), 'w', encoding='utf-8') as f:
        f.write(license_content)
    
    with open(os.path.join(node_dir, 'README.md'), 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    # Create the ZIP file
    zip_filename = f"{sanitized_node_name}.zip"
    
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                file_path = os.path.join(root, file)
                # Calculate the archive name (relative to temp_dir)
                archive_name = os.path.relpath(file_path, temp_dir)
                zipf.write(file_path, archive_name)
    
    # Clean up temporary directory
    import shutil
    shutil.rmtree(temp_dir)
    
    return zip_filename, f"Complete node package created: {zip_filename}"


def generate_prompt_selector_node_with_zip(node_name, category, prompts_list):
    """Wrapper function that generates the complete node package"""
    return generate_complete_node_package(node_name, category, prompts_list)


with gr.Blocks(title="Complete Prompt Selector Node Generator") as demo:
    gr.Markdown("# Complete Prompt Selector Node Generator")
    gr.Markdown("Create a complete ComfyUI node package with all necessary files")
    
    with gr.Row():
        node_name = gr.Textbox(label="Node Name", placeholder="Enter node name (e.g., PromptSelector)")
        category = gr.Textbox(label="Category", placeholder="Enter category (e.g., Custom)", value="Custom")
    
    prompts_list = gr.TextArea(
        label="Prompts List (one per line)",
        placeholder="Enter prompts, one per line\nExample:\nA beautiful landscape\nA futuristic city\nA mystical forest",
        lines=10
    )
    
    generate_btn = gr.Button("Generate Complete Node Package")
    
    node_output = gr.Code(label="Generated Node Code Preview", language="python")
    status_output = gr.Textbox(label="Status", interactive=False)
    download_output = gr.File(label="Download Node Package", visible=True)
    
    def generate_and_preview(node_name, category, prompts_list):
        zip_filename, status = generate_prompt_selector_node_with_zip(node_name, category, prompts_list)
        
        # Also return a preview of the node code
        if node_name.strip() and prompts_list.strip():
            sanitized_node_name = sanitize_filename(node_name)
            prompts = [p.strip() for p in prompts_list.split('\n') if p.strip()]
            
            node_content = f'''import random

class {node_name}:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {{
            "required": {{
                "select": ("INT", {{"default": 0, "min": 0, "max": {len(prompts)-1}, "step": 1}}),
                "mode": (["sequential", "random"], {{}}),
            }},
        }}

    RETURN_TYPES = ("STRING",)
    FUNCTION = "select_prompt"
    OUTPUT_NODE = True
    CATEGORY = "{category}"

    def select_prompt(self, select, mode):
        prompts = {json.dumps(prompts)}
        
        if mode == "random":
            selected_prompt = random.choice(prompts)
        else:  # sequential
            index = select % len(prompts)
            selected_prompt = prompts[index]
        
        return (selected_prompt,)


NODE_CLASS_MAPPINGS = {{
    "{node_name}": {node_name}
}}

NODE_DISPLAY_NAME_MAPPINGS = {{
    "{node_name}": "{node_name}"
}}
'''
            return node_content, status, zip_filename
        else:
            return "", status, zip_filename
    
    generate_btn.click(
        fn=generate_and_preview,
        inputs=[node_name, category, prompts_list],
        outputs=[node_output, status_output, download_output]
    )


if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7861)