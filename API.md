# Project Hogwarts - Node API Documentation

## Endpoints

- GET /node/status  << Returns the status of all items on the node >> <br>
- GET /node/light << perfrom an action (turn off or on) a light>> <br>
    parameters: <br>
        ID - ID of light to turn on (led0..led5) <br>
        action - action to perform ('on', 'off') <br>


## this is an example of json file for status

```
{
    'name' : 'nodeName1',
    status = {
            'datetime' = 'datetime',
            'light_status' : [ {'id'= 'led0','state'=0 },{'id'= 'led1','state'=0 }...]
        }
}
```