#!/bin/bash

nvidia-docker run \
-e DISPLAY=172.17.0.1$DISPLAY \
-v /mnt/HDD/work:/home/mine/work \
--rm=true \
-u mine \
-it \
eclipse_chainer:1.0
