#----------------------------
# Define the build image
#----------------------------
FROM python:3.10.4-slim as builder

# Update pip as root user
RUN pip install --upgrade pip==22.0.2

# Add non-root user
ARG UID=501
RUN adduser --disabled-password \
            --uid ${UID} \
            --shell /bin/bash \
            --gecos "" \
            leaf
USER leaf

# Use bash rather than sh
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

#----------------------------
# Install poetry
#----------------------------
# Set path to where poetry gets installed
ENV PATH=/home/leaf/.local/bin:${PATH}
RUN pip install --user --no-cache-dir poetry==1.2.0b1

#----------------------------
# Install dependencies
#----------------------------
WORKDIR /home/leaf

# This will get poetry to install in $PWD/.venv
RUN poetry config virtualenvs.in-project true
# Add .venv to $PATH
ENV PATH="/home/leaf/.venv/bin:${PATH}"

# Copy over the dependency definitions from the client
COPY --chown=leaf:leaf pyproject.toml /home/leaf/
COPY --chown=leaf:leaf poetry.lock /home/leaf/

# Now install dependencies into /home/leaf/.venv
ARG POETRY_DEV_OPTION=--no-dev
RUN poetry install --no-interaction --no-ansi ${POETRY_DEV_OPTION}


#----------------------------
# Define the runnable image
#----------------------------
FROM python:3.10.4-slim

# Install Java8
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       # Manage the version of this here:
       # https://tracker.debian.org/pkg/openjdk-8
       openjdk-11-jdk \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Add non-root user
ARG UID=501
RUN adduser --disabled-password \
            --uid ${UID} \
            --shell /bin/bash \
            --gecos "" \
            leaf
RUN mkdir /opt/app/
RUN chown leaf:leaf /opt/app
USER leaf

# Add .venv to $PATH
ENV PATH="/home/leaf/.venv/bin:${PATH}"

# Copy in python dependencies
COPY --from=builder --chown=leaf:leaf /home/leaf/.venv/ /home/leaf/.venv/

# Copy in everything else not listed in .dockerignore:
WORKDIR /opt/app/
COPY --chown=leaf:leaf . /opt/app/

LABEL owner="cfdair"
LABEL account="cfdair"

CMD python -m seek_coding_challenge
