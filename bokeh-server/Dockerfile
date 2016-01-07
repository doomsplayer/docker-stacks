# Copyright (c) Jupyter Development Team.
FROM torz/minimal-notebook

MAINTAINER Jupyter Project <jupyter@googlegroups.com>

COPY notebook.conf /etc/supervisor/conf.d/
COPY run-bokeh /usr/bin/

USER jovyan

# Install Python 3 packages
RUN conda install --yes \
    'pandas' \
    'cython' \
    'bokeh' \
    'redis' \
    'redis-py'\
    && conda clean -yt

USER root

