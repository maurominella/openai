#-------------------------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE file in the project root for license information.
#-------------------------------------------------------------------------------------------------------------

FROM mcr.microsoft.com/devcontainers/python:3.11

#
# Update the OS and maybe install packages
#
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
   && apt-get upgrade -y  \
   && apt-get -y install --no-install-recommends build-essential \
   && apt-get autoremove -y \
   && apt-get clean -y \
   && rm -rf /var/lib/apt/lists/*
