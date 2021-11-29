FROM ubuntu:18.04
RUN apt update -y && apt upgrade -y python python-dev python-pip python3 python2.7-dev python3-dev python3-pip
RUN apt update && apt install -y python-setuptools python3-setuptools 2to3 python3-lib2to3 python3-toolz git && pip3 install numpy flask-cors
RUN pip3 install Pillow==7.1.1 && pip3 install torch==1.10.0+cpu torchvision==0.11.1+cpu torchaudio==0.10.0+cpu -f https://download.pytorch.org/whl/cpu/torch_stable.html
RUN git clone https://github.com/facebookresearch/detectron2.git && python3 -m pip install -e detectron2
RUN git clone https://github.com/cocodataset/cocoapi.git && cd cocoapi/PythonAPI && 2to3 . -w && python3 setup.py install 
RUN mkdir pythonSv
COPY ./ /pythonSv
EXPOSE 5001
WORKDIR /pythonSv
ENTRYPOINT [ "python3","sv.py","5001" ]