# BackEnd

This is the server in charge of connecting the Front End with the Back End of our application

It is written in Python, using [the Flask web framework][flask].

The source code is contained in the `sv.py` module.

### Luncher

docker build -f .\Dockerfile . 

docker run -d -p 5000:5000 [imageID] or docker run -p 5000:5000 [imageID]
