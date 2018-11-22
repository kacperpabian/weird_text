FROM python:3.7

ADD weird_text.py /

CMD [ "python", "./weird_text.py" ]