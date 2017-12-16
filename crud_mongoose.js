var new_user = require('mongoose');

var mcrud = require('crud'),
    cm = require('crud-mongoose');

  new_user.connect("mongodb://localhost:27017/userManager");
  
  let data = {
        "_id": "59071791b0lkscm2325794",
        "name": "John Doe",
        "email": "john.doe@gmail.com",
        "password": "johndoe",
        "__v": 0
      };
    
  var dataCon = new_user.connection;
  var userdata = dataCon.collection("users").insert(data);           
 
