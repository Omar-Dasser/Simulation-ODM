FROM tiangolo/uwsgi-nginx:python3.7

MAINTAINER DASSER omar "omar.dasser@ibm.com"

RUN apt-get upgrade -y && \  
    apt-get update -y && \
    apt-get install -y wget git

RUN git clone https://github.com/Omar-Dasser/Simulation-ODM.git tmp && mv tmp/.git . && rm -rf tmp && git reset --hard
