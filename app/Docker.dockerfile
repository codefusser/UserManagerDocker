
FROM node:Carbon

#Directory where app image exist

WORKDIR ./

COPY package*.json /../userManagerRepo

RUN npm install

COPY . /../userManagerRepo

EXPOSE 8080

CMD [ "npm", "start" ]


