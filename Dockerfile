FROM python:3-alpine

WORKDIR /app

COPY FinalProject.py Board.py Game.py /app/

CMD ["python", "/app/FinalProject.py"]