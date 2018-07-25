FROM tensorflow/tensorflow:1.9.0-py3
LABEL maintainer="Ryohei Kuroki <ryohei.kuroki@gmail.com>"

RUN pip install -q keras
RUN pip install -q tqdm

COPY jupyter_notebook_config.py /root/.jupyter/
CMD ["bash"]
