FROM docker.io/debian:stable AS base

RUN apt-get update && \
    apt-get install -y --no-install-recommends git graphviz make pipx sudo && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN useradd \
    --create-home \
    --shell /bin/bash \
    -G sudo \
    developer && \
    echo '%sudo ALL=(ALL) NOPASSWD:ALL' | tee /etc/sudoers.d/99_nopasswd_sudo && \
    chmod 0440 /etc/sudoers.d/99_nopasswd_sudo && \
    mkdir -p /home/developer/.local/bin && \
    chown -R developer:developer /home/developer && \
    chmod 755 /home/developer


USER developer
RUN pipx install 'uv>=0.7.20,<0.8'
ENV PATH=/home/developer/.local/bin:${PATH}


FROM base AS devcontainer

RUN sudo apt-get update && \
    sudo apt-get install -y --no-install-recommends git ssh vim less gnupg2 && \
    sudo apt-get clean && \
    sudo rm -rf /var/lib/apt/lists/*

FROM base AS build

USER developer
RUN mkdir -p /home/developer/blog-v3
WORKDIR /home/developer/blog-v3

COPY --chown=developer:developer pyproject.toml uv.lock ./
RUN uv sync --locked --dev --no-install-project

COPY --chown=developer:developer .git .git
COPY --chown=developer:developer content content
COPY --chown=developer:developer src src
COPY --chown=developer:developer Makefile pyproject.toml README.md uv.lock ./

RUN uv sync --locked --dev
RUN uv run make html
RUN tar -cvvf build/html.tar -C build html


FROM scratch AS artifact
COPY --from=build /home/developer/blog-v3/build/html.tar /

FROM scratch AS default
RUN use-a-specific-target-not-default
