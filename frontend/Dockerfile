FROM node:16.14.2

RUN mkdir /app
RUN chmod -R 777 /app

WORKDIR /app

COPY . /app

RUN yarn

EXPOSE 3000

ENV NUXT_HOST=0.0.0.0
ENV NUXT_PORT=3000
