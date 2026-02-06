import gradio as gr
import json


# Default negative prompt for Text-to-Image
DEFAULT_NEGATIVE = "blurry, low quality, bad anatomy, deformed, cartoon, anime"


def generate_text_to_image_node(node_name, category, prompts_dict, 
                                  hair_lengths, hair_colors, facial_expressions, 
                                  facial_hairs, clothing_styles):
    """Generate ComfyUI node for Text-to-Image prompts with customizable parameters"""
    
    if not node_name.strip():
        raise gr.Error("Node name cannot be empty")
    
    if not prompts_dict:
        raise gr.Error("Please add at least one prompt")
    
    # Add "none" option if not present
    if "none" not in prompts_dict:
        prompts_dict = {"none": ("", "")} | prompts_dict
    
    # Parse parameter lists
    hair_length_list = [x.strip() for x in hair_lengths.split(',') if x.strip()]
    hair_color_list = [x.strip() for x in hair_colors.split(',') if x.strip()]
    facial_expr_list = [x.strip() for x in facial_expressions.split(',') if x.strip()]
    facial_hair_list = [x.strip() for x in facial_hairs.split(',') if x.strip()]
    clothing_list = [x.strip() for x in clothing_styles.split(',') if x.strip()]
    
    # Generate node code
    node_content = f'''import folder_paths
import re

class {node_name}:
    PROMPT_DICT = {json.dumps(prompts_dict, indent=8)}
    
    @classmethod
    def INPUT_TYPES(cls):
        return {{
            "required": {{
                "prompt_choice": (list(cls.PROMPT_DICT.keys()), {{"default": "none"}}),
                "hair_length": ({json.dumps(hair_length_list)}, {{"default": {json.dumps(hair_length_list[0])}}}),
                "hair_color": ({json.dumps(hair_color_list)}, {{"default": {json.dumps(hair_color_list[0])}}}),
                "facial_expression": ({json.dumps(facial_expr_list)}, {{"default": {json.dumps(facial_expr_list[0])}}}),
                "facial_hair": ({json.dumps(facial_hair_list)}, {{"default": {json.dumps(facial_hair_list[0])}}}),
                "clothing_style": ({json.dumps(clothing_list)}, {{"default": {json.dumps(clothing_list[0])}}}),
            }}
        }}
        
    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive", "negative")
    FUNCTION = "get_prompt"
    CATEGORY = "{category}"
    DESCRIPTION = "Text-to-Image prompt selector with customizable parameters"
    
    def get_prompt(self, prompt_choice, hair_length, hair_color, 
                   facial_expression, facial_hair, clothing_style):
        
        pos, neg = self.PROMPT_DICT.get(prompt_choice, ("", ""))
        
        # Replace placeholder variables
        pos = pos.replace("{{hair_length}}", hair_length)
        pos = pos.replace("{{hair_color}}", hair_color)
        pos = pos.replace("{{facial_hair}}", facial_hair)
        pos = pos.replace("{{facial_expression}}", facial_expression)
        pos = pos.replace("{{clothing_style}}", clothing_style)
        
        return (pos, neg)


NODE_CLASS_MAPPINGS = {{
    "{node_name}": {node_name}
}}

NODE_DISPLAY_NAME_MAPPINGS = {{
    "{node_name}": "{node_name}"
}}
'''
    
    return node_content


def generate_voice_music_node(node_name, category, prompts_dict,
                               voices, music_styles, moods, instruments):
    """Generate ComfyUI node for Voice + Music generation"""
    
    if not node_name.strip():
        raise gr.Error("Node name cannot be empty")
    
    if not prompts_dict:
        raise gr.Error("Please add at least one voice prompt")
    
    # Add "none" option if not present
    if "none" not in prompts_dict:
        prompts_dict = {"none": ""} | prompts_dict
    
    # Parse parameter lists
    voice_list = [x.strip() for x in voices.split(',') if x.strip()]
    style_list = [x.strip() for x in music_styles.split(',') if x.strip()]
    mood_list = [x.strip() for x in moods.split(',') if x.strip()]
    
    # Generate node code
    node_content = f'''import folder_paths

class {node_name}:
    PROMPT_DICT = {json.dumps(prompts_dict, indent=8)}
    
    @classmethod
    def INPUT_TYPES(cls):
        return {{
            "required": {{
                "base_prompt": (list(cls.PROMPT_DICT.keys()), {{"default": "none"}}),
                "voice_type": ({json.dumps(voice_list)}, {{"default": {json.dumps(voice_list[0])}}}),
                "music_style": ({json.dumps(style_list)}, {{"default": {json.dumps(style_list[0])}}}),
                "mood": ({json.dumps(mood_list)}, {{"default": {json.dumps(mood_list[0])}}}),
                "tempo": (["slow", "medium", "fast"], {{"default": "medium"}}),
                "bpm": ("INT", {{"default": 120, "min": 60, "max": 200, "step": 1}}),
            }},
            "optional": {{
                "instrument_piano": ("BOOLEAN", {{"default": False}}),
                "instrument_guitar": ("BOOLEAN", {{"default": False}}),
                "instrument_synthesizer": ("BOOLEAN", {{"default": False}}),
                "instrument_drums": ("BOOLEAN", {{"default": False}}),
                "instrument_bass": ("BOOLEAN", {{"default": False}}),
                "instrument_strings": ("BOOLEAN", {{"default": False}}),
                "instrument_bongos": ("BOOLEAN", {{"default": False}}),
                "instrument_brass": ("BOOLEAN", {{"default": False}}),
                "additional_tags": ("STRING", {{"default": "", "multiline": False}}),
            }}
        }}
        
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("music_prompt",)
    FUNCTION = "generate_music_prompt"
    CATEGORY = "{category}"
    DESCRIPTION = "Voice + Music generation prompt builder"
    
    def generate_music_prompt(self, base_prompt, voice_type, music_style, mood, 
                             tempo, bpm,
                             instrument_piano=False, instrument_guitar=False,
                             instrument_synthesizer=False, instrument_drums=False,
                             instrument_bass=False, instrument_strings=False,
                             instrument_bongos=False, instrument_brass=False,
                             additional_tags=""):
        
        # Start with base prompt
        base = self.PROMPT_DICT.get(base_prompt, "")
        
        # Build prompt components
        components = []
        
        if base:
            components.append(base)
        
        # Add voice type
        components.append(voice_type)
        
        # Add music style
        components.append(music_style)
        
        # Add mood
        components.append(mood)
        
        # Add tempo
        components.append(tempo)
        
        # Add BPM
        components.append(f"{{bpm}} BPM")
        
        # Add selected instruments
        instruments = []
        if instrument_piano:
            instruments.append("piano")
        if instrument_guitar:
            instruments.append("guitar")
        if instrument_synthesizer:
            instruments.append("synthesizer")
        if instrument_drums:
            instruments.append("drums")
        if instrument_bass:
            instruments.append("bass")
        if instrument_strings:
            instruments.append("strings")
        if instrument_bongos:
            instruments.append("bongos")
        if instrument_brass:
            instruments.append("brass")
        
        if instruments:
            components.extend(instruments)
        
        # Add additional tags
        if additional_tags.strip():
            components.append(additional_tags.strip())
        
        # Join all components
        final_prompt = ", ".join(components)
        
        return (final_prompt,)


NODE_CLASS_MAPPINGS = {{
    "{node_name}": {node_name}
}}

NODE_DISPLAY_NAME_MAPPINGS = {{
    "{node_name}": "{node_name}"
}}
'''
    
    return node_content


def save_node_files(node_code, node_name):
    """Save the generated node code to files"""
    node_filename = f"{node_name.lower()}.py"
    
    # Save the node file
    with open(node_filename, 'w', encoding='utf-8') as f:
        f.write(node_code)
    
    # Create __init__.py
    init_content = f'''from .{node_name.lower()} import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
'''
    
    with open('__init__.py', 'w', encoding='utf-8') as f:
        f.write(init_content)
    
    return f"✓ Files created: {node_filename} and __init__.py"


# Gradio Interface
with gr.Blocks(title="ComfyUI Node Generator", theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🎨 ComfyUI Custom Node Generator")
    gr.Markdown("Generate custom ComfyUI nodes for Text-to-Image or Voice+Music generation")
    
    # State to store prompts
    t2i_prompts_state = gr.State({})
    voice_prompts_state = gr.State({})
    
    # Node Type Selection
    node_type = gr.Radio(
        choices=["Text-to-Image Prompt Selector", "Voice + Music Generator"],
        label="Node Type",
        value="Text-to-Image Prompt Selector"
    )
    
    # Common fields
    with gr.Row():
        node_name = gr.Textbox(label="Node Name", placeholder="e.g., MyPromptSelector", value="MyPromptSelector")
        category = gr.Textbox(label="Category", placeholder="e.g., Custom", value="Custom")
    
    # ==================== TEXT-TO-IMAGE SECTION ====================
    with gr.Group(visible=True) as t2i_group:
        gr.Markdown("### 📝 Text-to-Image Prompts")
        gr.Markdown("Fügen Sie Prompts einzeln hinzu. Verwenden Sie Platzhalter: `{hair_length}`, `{hair_color}`, `{facial_expression}`, `{facial_hair}`, `{clothing_style}`")
        
        # Current prompts display
        t2i_current_prompts = gr.Textbox(
            label="Aktuelle Prompts",
            interactive=False,
            lines=5,
            value="Keine Prompts hinzugefügt"
        )
        
        gr.Markdown("#### Neuen Prompt hinzufügen:")
        
        with gr.Row():
            t2i_prompt_name = gr.Textbox(label="Prompt Name", placeholder="z.B. Portrait")
        
        t2i_positive = gr.TextArea(
            label="Positive Prompt",
            placeholder="z.B. professional photo, {hair_color} {hair_length} hair, {facial_expression}",
            lines=3
        )
        
        t2i_negative = gr.TextArea(
            label="Negative Prompt (optional)",
            placeholder="Leer lassen für Standard-Wert",
            lines=2,
            value=DEFAULT_NEGATIVE
        )
        
        with gr.Row():
            t2i_add_btn = gr.Button("➕ Prompt hinzufügen", variant="secondary")
            t2i_clear_btn = gr.Button("🗑️ Alle Prompts löschen", variant="stop")
        
        gr.Markdown("### ⚙️ Anpassbare Parameter")
        
        with gr.Row():
            hair_lengths = gr.Textbox(
                label="Haarlängen (Komma getrennt)",
                value="short, medium, long, very long, shoulder-length, chin-length"
            )
            hair_colors = gr.Textbox(
                label="Haarfarben (Komma getrennt)",
                value="gray, brown, black, blonde, red, silver-gray, white"
            )
        
        with gr.Row():
            facial_expressions = gr.Textbox(
                label="Gesichtsausdrücke (Komma getrennt)",
                value="friendly warm smile, broad happy smile, stern serious expression, surprised wide eyes"
            )
            facial_hairs = gr.Textbox(
                label="Gesichtsbehaarung (Komma getrennt)",
                value="clean shaven, light stubble, groomed beard, full beard, mustache, goatee"
            )
        
        clothing_styles = gr.Textbox(
            label="Kleidungsstile (Komma getrennt)",
            value="dark business suit, casual wear, leather jacket, hoodie, elegant suit"
        )
    
    # ==================== VOICE + MUSIC SECTION ====================
    with gr.Group(visible=False) as voice_music_group:
        gr.Markdown("### 🎵 Voice + Music Prompts")
        gr.Markdown("Fügen Sie Musik-Prompts einzeln hinzu")
        
        # Current prompts display
        voice_current_prompts = gr.Textbox(
            label="Aktuelle Prompts",
            interactive=False,
            lines=5,
            value="Keine Prompts hinzugefügt"
        )
        
        gr.Markdown("#### Neuen Prompt hinzufügen:")
        
        with gr.Row():
            voice_prompt_name = gr.Textbox(label="Prompt Name", placeholder="z.B. Anime Song")
        
        voice_description = gr.TextArea(
            label="Beschreibung / Tags",
            placeholder="z.B. anime, kawaii pop, j-pop, childish",
            lines=2
        )
        
        with gr.Row():
            voice_add_btn = gr.Button("➕ Prompt hinzufügen", variant="secondary")
            voice_clear_btn = gr.Button("🗑️ Alle Prompts löschen", variant="stop")
        
        gr.Markdown("### 🎤 Voice & Music Parameter")
        
        voices = gr.Textbox(
            label="Stimmen-Typen (Komma getrennt)",
            value="soft female vocals, deep male vocals, Till Lindemann style, AC/DC rock voice, Europa 80s singer, 2Pac style, Eminem style, Latino singer, opera classical, raspy blues voice"
        )
        
        music_styles = gr.Textbox(
            label="Musikstile (Komma getrennt)",
            value="Techno, Lo-Fi, Cinematic, Ambient, Rock, Heavy Metal, Rock Ballade, Kawaii Pop, J-Pop, Reggaeton, Bongo Flava, Rap, Latino Hit"
        )
        
        moods = gr.Textbox(
            label="Stimmungen (Komma getrennt)",
            value="Energetic, Dark, Happy, Calm, Cheerful, Lighthearted, Aggressive, Romantic, Melancholic"
        )
        
        gr.Markdown("**Instrumente:** Piano, Guitar, Synthesizer, Drums, Bass, Strings, Bongos, Brass (werden als Checkboxen in der Node)")
    
    # ==================== GENERATE BUTTON ====================
    generate_btn = gr.Button("🚀 FERTIG - Node generieren", variant="primary", size="lg")
    
    # Output
    with gr.Group():
        node_output = gr.Code(label="Generierter Node Code", language="python", lines=20)
        status_output = gr.Textbox(label="Status", interactive=False)
    
    # ==================== LOGIC FUNCTIONS ====================
    
    # Add T2I prompt
    def add_t2i_prompt(prompts_dict, name, positive, negative):
        if not name.strip():
            return prompts_dict, "⚠️ Bitte geben Sie einen Prompt-Namen ein", "", "", DEFAULT_NEGATIVE
        
        if not positive.strip():
            return prompts_dict, "⚠️ Bitte geben Sie einen positiven Prompt ein", name, positive, negative
        
        # Use default negative if empty
        if not negative.strip():
            negative = DEFAULT_NEGATIVE
        
        # Add to dictionary
        prompts_dict[name.strip()] = (positive.strip(), negative.strip())
        
        # Create display text
        display_text = "\n\n".join([f"🔹 {k}:\n   Positive: {v[0][:80]}...\n   Negative: {v[1][:60]}..." 
                                     for k, v in prompts_dict.items()])
        
        return prompts_dict, display_text, "", "", DEFAULT_NEGATIVE
    
    # Clear T2I prompts
    def clear_t2i_prompts():
        return {}, "Keine Prompts hinzugefügt"
    
    # Add Voice prompt
    def add_voice_prompt(prompts_dict, name, description):
        if not name.strip():
            return prompts_dict, "⚠️ Bitte geben Sie einen Prompt-Namen ein", "", ""
        
        if not description.strip():
            return prompts_dict, "⚠️ Bitte geben Sie eine Beschreibung ein", name, description
        
        # Add to dictionary
        prompts_dict[name.strip()] = description.strip()
        
        # Create display text
        display_text = "\n\n".join([f"🔹 {k}: {v}" for k, v in prompts_dict.items()])
        
        return prompts_dict, display_text, "", ""
    
    # Clear Voice prompts
    def clear_voice_prompts():
        return {}, "Keine Prompts hinzugefügt"
    
    # Switch node type visibility
    def update_visibility(node_type):
        if node_type == "Text-to-Image Prompt Selector":
            return gr.update(visible=True), gr.update(visible=False)
        else:
            return gr.update(visible=False), gr.update(visible=True)
    
    # Generate node
    def generate_node(node_type, node_name, category, 
                     t2i_prompts, hair_lengths, hair_colors, facial_expressions, facial_hairs, clothing_styles,
                     voice_prompts, voices, music_styles, moods):
        
        try:
            if node_type == "Text-to-Image Prompt Selector":
                if not t2i_prompts:
                    return "", "❌ Bitte fügen Sie mindestens einen Prompt hinzu"
                
                code = generate_text_to_image_node(
                    node_name, category, t2i_prompts,
                    hair_lengths, hair_colors, facial_expressions, facial_hairs, clothing_styles
                )
            else:
                if not voice_prompts:
                    return "", "❌ Bitte fügen Sie mindestens einen Prompt hinzu"
                
                code = generate_voice_music_node(
                    node_name, category, voice_prompts,
                    voices, music_styles, moods, ""
                )
            
            status = save_node_files(code, node_name)
            return code, f"✅ {status}\n\n📝 Prompts: {len(t2i_prompts or voice_prompts)}"
            
        except Exception as e:
            return "", f"❌ Error: {str(e)}"
    
    # ==================== EVENT HANDLERS ====================
    
    node_type.change(
        fn=update_visibility,
        inputs=[node_type],
        outputs=[t2i_group, voice_music_group]
    )
    
    t2i_add_btn.click(
        fn=add_t2i_prompt,
        inputs=[t2i_prompts_state, t2i_prompt_name, t2i_positive, t2i_negative],
        outputs=[t2i_prompts_state, t2i_current_prompts, t2i_prompt_name, t2i_positive, t2i_negative]
    )
    
    t2i_clear_btn.click(
        fn=clear_t2i_prompts,
        outputs=[t2i_prompts_state, t2i_current_prompts]
    )
    
    voice_add_btn.click(
        fn=add_voice_prompt,
        inputs=[voice_prompts_state, voice_prompt_name, voice_description],
        outputs=[voice_prompts_state, voice_current_prompts, voice_prompt_name, voice_description]
    )
    
    voice_clear_btn.click(
        fn=clear_voice_prompts,
        outputs=[voice_prompts_state, voice_current_prompts]
    )
    
    generate_btn.click(
        fn=generate_node,
        inputs=[
            node_type, node_name, category,
            t2i_prompts_state, hair_lengths, hair_colors, facial_expressions, facial_hairs, clothing_styles,
            voice_prompts_state, voices, music_styles, moods
        ],
        outputs=[node_output, status_output]
    )


if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
