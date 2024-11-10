FROM node:16

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY src/ ./src

RUN npm install -g serve

EXPOSE 3000

CMD ["serve", "-s", "src", "-l", "3000"]

