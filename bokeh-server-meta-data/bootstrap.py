from bokeh.models.glyphs import Glyph
from bokeh.core.properties import Dict, String
class MetaGlyph(Glyph):
    meta = Dict(String, String)
