FROM python:2.7.11
MAINTAINER Michael J. Stealey <mjstealey@gmail.com>

RUN apt-get update && apt-get install -y \
    postgresql postgresql-client \
    openssh-server
RUN pip install mezzanine
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Install SSH for remote PyCharm debugging
RUN mkdir /var/run/sshd
RUN echo 'root:screencast' | chpasswd
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

# Add docker user for use with SSH debugging
RUN useradd -m docker
RUN echo docker:docker | chpasswd

ADD . /home/docker/lucid
WORKDIR /home/docker/lucid

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]