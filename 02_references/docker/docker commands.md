---
title: docker commands
tags: [command, docker]
aliases: []
date modified: 2024-12-16 15:31:56 +09:00
date created: 2024-12-09 21:31:10 +09:00
---

- List all docker containers (running and stopped):

```bash
docker ps --all
```

- Start a container from an image, with a custom name:

```bash
docker run --name container_name image
```

- Start or stop an existing container:

```bash
docker start|stop container_name
```

- Pull an image from a docker registry:

```bash
docker pull image
```

- Display the list of already downloaded images:

```bash
docker images
```

- Open a shell inside a running container:

```bash
docker exec -it container_name sh
```

- Remove a stopped container:

```bash
docker rm container_name
```

- Fetch and follow the logs of a container:

```bash
docker logs -f container_name
```
