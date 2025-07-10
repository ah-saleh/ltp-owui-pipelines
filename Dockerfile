FROM python:3.11-slim-bookworm AS base

# Use args
ARG USE_CUDA
ARG USE_CUDA_VER
ARG PIPELINES_URLS
ARG PIPELINES_REQUIREMENTS_PATH

## Basis ##
ENV ENV=prod \
    PORT=9099 \
    # pass build args to the build
    USE_CUDA_DOCKER=${USE_CUDA} \
    USE_CUDA_DOCKER_VER=${USE_CUDA_VER} \
    # Poetry configuration
    POETRY_VERSION=1.8.2 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_VIRTUALENVS_IN_PROJECT=false \
    POETRY_NO_INTERACTION=1

# Install GCC and build tools. 
# These are kept in the final image to enable installing packages on the fly.
RUN apt-get update && \
    apt-get install -y gcc build-essential curl git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="$POETRY_HOME/bin:$PATH"

WORKDIR /app

# Copy Poetry files
COPY pyproject.toml poetry.lock ./

# Install torch with CUDA support if needed (before other dependencies to avoid conflicts)
RUN if [ "$USE_CUDA_DOCKER" = "true" ]; then \
        pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/$USE_CUDA_DOCKER_VER --no-cache-dir; \
    else \
        pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu --no-cache-dir; \
    fi

# Install all dependencies using Poetry
RUN poetry install --no-root --no-dev


# Layer on for other components
FROM base AS app

ENV PIPELINES_URLS=${PIPELINES_URLS} \
    PIPELINES_REQUIREMENTS_PATH=${PIPELINES_REQUIREMENTS_PATH}

# Copy the application code
COPY . .

# Run a docker command if either PIPELINES_URLS or PIPELINES_REQUIREMENTS_PATH is not empty
RUN if [ -n "$PIPELINES_URLS" ] || [ -n "$PIPELINES_REQUIREMENTS_PATH" ]; then \
    echo "Running docker command with PIPELINES_URLS or PIPELINES_REQUIREMENTS_PATH"; \
    ./start.sh --mode setup; \
    fi

# Expose the port
ENV HOST="0.0.0.0"
ENV PORT="9099"

# if we already installed the requirements on build, we can skip this step on run
ENTRYPOINT [ "bash", "start.sh" ]
