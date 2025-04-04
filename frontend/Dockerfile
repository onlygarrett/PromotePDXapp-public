FROM node:23.1.0-alpine

WORKDIR /app/frontend/

ENV PATH /app/frontend/node_modules/.bin:$PATH

COPY ./package.json ./package-lock.json ./

RUN npm cache verify && npm install

# add app
COPY . ./

# EXPOSE 3000

CMD ["npm", "start"]
