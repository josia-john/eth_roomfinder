Currently hosted on [rooms.jlabs.ch](https://rooms.jlabs.ch).

To build the docker image: `sudo docker build -t <image_name> src`

To save the docker image: `docker save -o <path for created tar file> <image name>`

To load the docker image: `docker load -i <path to docker image tar file>`

To run the docker image: `sudo docker run -p <PORT>:8000 --restart=always eth_roomfinder`
where `<PORT>` is the port it will bind to on the server.

Don't forget to set URL in index.html!

default image name: "eth_roomfinder"