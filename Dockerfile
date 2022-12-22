FROM fedora:latest
RUN mkdir -m 777 -p /rpmbuild_dir
WORKDIR /rpmbuild_dir
RUN sudo dnf update -y \
    && dnf install -y python3 \
    && dnf groupinstall -y "C Development Tools and Libraries" \
    && dnf -y groupinstall "RPM Development Tools"
RUN dnf install -y cmake openssl-devel openssl # aws-c-cal
RUN dnf install -y ninja-build # s2n-tls
RUN dnf install -y python3-devel python3-wheel # aws-crt
RUN dnf install -y python3-flit-core python3-jsonschema \
    python3-mock python3-pytest python3-pytest-xdist \
    python3-sphinx python3-sphinx-notfound-page python3-colorama \
    python3-cryptography python3-jmespath python3-ruamel-yaml \
    python3-prompt-toolkit python3-wcwidth  # awscli
COPY . /rpmbuild_dir
RUN make setup && make build
