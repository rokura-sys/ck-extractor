FROM ubuntu:20.04
WORKDIR /ck-extractor
RUN chmod -R 777 /ck-extractor
ENV TZ Asia/Kolkata
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get -yqq update

RUN apt -yqq install python3 python3-pip wget curl mediainfo ffmpeg mkvtoolnix
COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["bash","run.sh"]
