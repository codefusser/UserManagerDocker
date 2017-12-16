@echo off

::goto the app directory, the directory must be empty
echo 'git init'
echo 'git clone https://github.com/codefusser/userManagerDocker'
echo 'node crud_mongoose.js %*'

echo 'docker build -it admin/express-api-demo'
echo 'docker run -p 127.0.0.1:8080 -d admin/express-api-demo'