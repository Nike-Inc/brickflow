FROM ubuntu:20.04
USER root

ARG brickflow_version=1.0.0
ARG node_version=18.14.0

# DO NOT ADD AS ENV:
#   debconf noninteractive
#          This is the anti-frontend. It never interacts with you  at  all,
#          and  makes  the  default  answers  be used for all questions. It
#          might mail error messages to root, but that's it;  otherwise  it
#          is  completely  silent  and  unobtrusive, a perfect frontend for
#          automatic installs. If you are using this front-end, and require
#          non-default  answers  to questions, you will need to preseed the
#          debconf database; see the section below  on  Unattended  Package
#          Installation for more details.

RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections && \
    apt-get update -y && apt-get install -y git curl wget unzip software-properties-common openjdk-11-jdk curl python3-psutil
SHELL ["/bin/bash", "-c"]

ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH=$PATH:$JAVA_HOME/bin

RUN git clone https://github.com/tfutils/tfenv /tfenv  \
    && ln -s /tfenv/bin/* /usr/local/bin \
    && tfenv install 1.3.0 && tfenv use 1.3.0

ENV NODE_VERSION ${node_version}

RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections  \
    && curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash  \
    && . $HOME/.nvm/nvm.sh \
    && nvm install $NODE_VERSION \
    && nvm use $NODE_VERSION \
    && npm install --global cdktf-cli@latest

ENV NODE_PATH /root/.nvm/versions/node/v$NODE_VERSION/lib/node_modules
ENV PATH /root/.nvm/versions/node/v$NODE_VERSION/bin:$PATH
ENV NVM_DIR /root/.nvm

RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get install -y python3.9 python3-pip python3.9-distutils && ln -s /usr/bin/python3.9 /usr/bin/python

ARG CACHEBUST=1

RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
    python3.9 get-pip.py && \
    ln -s /usr/local/bin/pip3.9 /usr/bin/pip3 && \
    ln -s /usr/local/bin/pip3.9 /usr/bin/pip

RUN python -m pip install -U pip && pip install -U setuptools poetry \
    && python -m pip install -U brickflow==${brickflow_version} \
    && python -m pip install -U cdktf

RUN  openssl s_client -connect github.com:443 2>/dev/null </dev/null | sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' > github.crt \
     && openssl s_client -connect objects.githubusercontent.com:443 2>/dev/null </dev/null | sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' > githubusercontent.crt \
     && cp github*.crt /usr/local/share/ca-certificates \
     && update-ca-certificates


CMD ["/bin/bash"]
