#mongodb container

#start a mongo instance
docker run --name userManager -d mongo

#connect to it from an application
docker run --name userManager --link userManager:mongo -d express-api-demo

#start the database from docker
docker run --name userManager -d mongo --auth