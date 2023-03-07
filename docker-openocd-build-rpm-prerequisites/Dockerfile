FROM fedora:37
LABEL maintainer="Raphael Lehmann <raphael+docker@rleh.de>"
LABEL Description="Image for building the upstream OpenOCD RPM package on Fedora"
WORKDIR /work

RUN dnf update -y \
    && dnf install -y make libtool pkg-config autoconf automake texinfo tree libusbx-devel hidapi-devel libftdi-devel rpm git which zip rpm-build capstone-devel chrpath jimtcl-devel libjaylink-devel libgpiod-devel sdcc \
    && dnf clean all \
  	&& rm -rf /var/cache/yum
