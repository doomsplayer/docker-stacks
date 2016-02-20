from bokeh.plotting import Figure
from bokeh.core.properties import Dict, String, List, Tuple, Instance
from bokeh.models.plots import Plot
from bokeh.core.properties import HasProps

class EnhancedFigure(Figure):
    variables = Dict(String, String)
    category = List(String)
