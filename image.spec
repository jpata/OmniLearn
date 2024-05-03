Bootstrap: docker

From: vmikuni/tensorflow:ngc-23.12-tf2-v1

%post
    python3 -m pip install notebook
    python3 -m pip install -U awkward vector
 
%environment
    export PIP_DEFAULT_TIMEOUT=500
    export LC_ALL=""

%runscript
    /bin/bash
