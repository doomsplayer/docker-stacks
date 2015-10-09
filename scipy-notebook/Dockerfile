# Copyright (c) Jupyter Development Team.
FROM torz/minimal-notebook

MAINTAINER Jupyter Project <jupyter@googlegroups.com>

USER jovyan

# Install Python 3 packages
RUN conda install --yes \
    'ipywidgets' \
    'pandas' \
    'matplotlib' \
    'scipy' \
    'seaborn' \
    'scikit-learn' \
    'scikit-image' \
    'sympy' \
    'cython' \
    'patsy' \
    'statsmodels' \
    'cloudpickle' \
    'dill' \
    'numba' \
    'bokeh' \
    && conda clean -yt

USER root

