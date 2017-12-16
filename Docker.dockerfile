#mongodb container

#start a mongo instance
docker run --name userManager -d mongo

#connect to it from an application
docker run --name userManager --link userManager:mongo -d express-api-demo


#via mongo
docker run -it --link userManager:mongo --rm mongo sh -c 'exec mongo "127.0.0.1:27017/userManager"'

#start the database from docker
docker run --name userManager -d mongo --auth