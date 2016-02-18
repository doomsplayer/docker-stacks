from bokeh.plotting import Figure
from bokeh.core.properties import Dict, String, List, Tuple, Instance

class EnhancedFigure():
    variables = Dict(String, String))
    category = List(String)
    plot = Instance(Figure)

    def __getattr__(self, attrib):
        return getattr(self.plot, attrib)
