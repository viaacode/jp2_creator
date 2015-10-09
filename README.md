# jp2_creator

This is a worker that will listen to a queue from RabbitMQ, converts the images specified in the message and post a message to the given exchange about the result.

# Installation

Simply check out this repository and run:

```
    [sudo] python3 setup.py install [--record files.txt]
```

# Usage

You can run the worker by executing the following command:

```
    jp2worker [-h] [-p BROKER_PORT] [-q RESULT_QUEUE] [-t TOPIC_TYPE] broker_ip incoming_queue result_exchange result_routing username password
```

Information about every parameter can be consulted with:

```
    jp2worker -h
```

# Documentation

Any further documentation can be found on the [VIAA Confluence page](https://viaadocumentation.atlassian.net/wiki/display/SI/JP2+creator)
