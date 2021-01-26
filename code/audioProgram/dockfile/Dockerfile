# This dockerfile demo for project build to docker images
# VERSION 2
# Author: wangyechao
# Command format: Instruction [arguments / command] …
# 2021/01/19- firstversion: wangyechao

# 第一行必须指定基础容器，建议使用aipln类型的小容器
FROM ubuntu:16.04
RUN apt-get update
COPY . /app
WORKDIR /app
COPY ../requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt
