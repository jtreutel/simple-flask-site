FROM circleci/python:latest
LABEL "maintainer"="github.com/jtreutel"

EXPOSE 5000

USER root
WORKDIR /tmp
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN sudo apt install ./google-chrome-stable_current_amd64.deb
RUN wget https://chromedriver.storage.googleapis.com/86.0.4240.22/chromedriver_linux64.zip
RUN unzip ./chromedriver_linux64.zip
RUN sudo mv chromedriver /usr/local/bin/

RUN mkdir /app
WORKDIR /app/
RUN git clone https://github.com/jtreutel/simple-flask-site.git
WORKDIR /app/simple-flask-site/
RUN pip3 install -r requirements.txt

ENTRYPOINT python3 src/site.py