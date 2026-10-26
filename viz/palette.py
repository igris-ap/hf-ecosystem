"""Colours and family names shared by the charts and the family tree.

Categorical slots are a validated palette, used in this fixed order (never
cycled). Checked with a colour-vision validator (worst-case pairs, protan/deutan
simulation and normal vision):
  - up to 4 slots in bars, stacks and lines: pass. Aqua and yellow are below
    3:1 contrast on the light surface, so those charts carry visible labels,
    and every chart's numbers are also in results/*.csv.
  - in a network graph EVERY pair of colours sits side by side, and only the
    first 3 slots pass that test. With 7 families, blue vs violet is too close
    even for full colour vision. So the family tree colours at most 3
    families and shows the rest in grey (identified by label, shape, tooltip).
"""

# categorical slots, light surface
SLOTS = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#6250d6", "#e34948"]
MAX_NETWORK_COLOURS = 3          # all-pairs-safe slots (see docstring)

SURFACE = "#fcfcfb"
INK = "#0b0b0b"                 # primary text
INK_2 = "#52514e"               # secondary text
MUTED = "#898781"               # axis labels, notes
GRID = "#e1e0d9"                # hairline gridlines
AXIS = "#c3c2b7"                # baseline
NEUTRAL = "#b5b3ab"             # "other" / not highlighted

# Relation colours: one fixed slot each, the same in every chart.
RELATION_COLOUR = dict(zip(("finetune", "adapter", "quantized", "merge"), SLOTS))

# The brief's seven model families. Several seeds belong to one family.
SEED_FAMILY = {
    "meta-llama/Llama-3.1-8B": "Llama",
    "meta-llama/Llama-3.2-1B": "Llama",
    "mistralai/Mistral-7B-v0.1": "Mistral",
    "Qwen/Qwen2.5-7B": "Qwen",
    "Qwen/Qwen3-8B-Base": "Qwen",
    "google/gemma-2-9b": "Gemma",
    "google/gemma-3-4b-pt": "Gemma",
    "microsoft/phi-2": "Phi",
    "deepseek-ai/DeepSeek-R1": "DeepSeek",
    "google-bert/bert-base-uncased": "BERT",
}
FAMILIES = ["Llama", "Qwen", "Mistral", "Gemma", "Phi", "DeepSeek", "BERT"]


def short_name(model_id):
    """'meta-llama/Llama-3.1-8B' -> 'Llama-3.1-8B' for axis labels."""
    return model_id.split("/", 1)[-1] if model_id else str(model_id)
