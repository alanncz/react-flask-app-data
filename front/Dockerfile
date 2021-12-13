FROM node:16-alpine as build-step

WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
COPY package.json yarn.lock ./
COPY ./src ./src
COPY ./public ./public
RUN npm install -g npm@8.3.0
RUN yarn install
RUN yarn build
CMD ["npm", "start" ]
