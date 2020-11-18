FROM adreeve/python-numpy

RUN pip install splatoon_league_corr
RUN apt-get update
RUN apt-get -y install locales-all vim

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8

WORKDIR /app

ADD main.py .
ADD ikaWidgetCSV_20201118144206.tcsv .
