#!/bin/bash
. /appenv/bin/activate

# Download requirements to build cache
pip3 download -d /build -r requirements_test.txt --no-input

# install application test requirements
pip3 install --no-index -f /build -r requirements_test.txt

# Run test.sh arguments
exec $@