docker build -t ml-31156-a1 .
docker run -it -v "$PWD":/usr/src/app/src  --rm ml-31156-a1 bash