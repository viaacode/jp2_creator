# jp2_creator

This is a worker that will listen to a queue from RabbitMQ, converts the images specified in the message and post a message to the given exchange about the result.

# Installation

Make sure kakadu is installed and available in the /usr/local/lib and /usr/local/bin directories. You can install it this way following the steps below:

```
    1. Unzip kakadu to a location of choice
    2. make -f {location}/make/{make_file_for_your_env}
    3. sudo mv {location}/lib/{folder_for_your_env}/libkdu_v75R.so /usr/local/lib/libkdu_v75R.so
    4. sudo mv -v {location}/bin/{folder_for_your_env}/* /usr/local/bin/
```

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
