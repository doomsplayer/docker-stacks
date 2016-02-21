from bokeh.plotting import Figure
from bokeh.core.properties import Dict, String, List

class EnhancedFigure(Figure):
    __implementation__ = """
    Plots = require "models/plots/plot"
    class EnhancedFigure extends Plots.Model
        type: "EnhancedFigure"
    module.exports =
        Model: EnhancedFigure
    """
    variables = Dict(String, String)
    category = List(String)
