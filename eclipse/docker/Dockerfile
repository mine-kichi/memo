FROM nvidia/cuda:8.0-cudnn5-devel-ubuntu14.04

RUN	apt-get update
RUN	apt-get -y install firefox
RUN	apt-get -y install language-pack-ja-base language-pack-ja
RUN	apt-get -y install language-pack-gnome-ja
RUN	apt-get -y install fonts-takao-gothic
ENV	LANG=ja_JP.UTF-8
RUN	apt-get -y install gedit
RUN	apt-get -y install python python-pip python-dev python-matplotlib python-scipy python-opencv
ADD	make_user.sh /home/make_user.sh
ADD	init.sh /home/init.sh
RUN 	chmod 777 /home/make_user.sh
RUN 	chmod 777 /home/init.sh
RUN	/home/init.sh
RUN	gpasswd -a mine sudo
RUN     apt-get install -y software-properties-common
RUN     add-apt-repository ppa:openjdk-r/ppa
RUN     apt-get update
RUN	apt-get -y install openjdk-8-jdk
RUN	pip install chainer==1.8.1
