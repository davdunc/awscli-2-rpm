.ONESHELL:

ARCH := $(shell arch)

setup:
        rm -rf ~/rpmbuild && rpmdev-setuptree
        cd ../rpmbuild/SPECS
        ln -s ../../awscli-2-rpm/specs/s2n-tls.spec ./

build:
        cd ../rpmbuild/SOURCES && rm -f ./*
        spectool --get-files ../SPECS/s2n-tls.spec
        cd ../SPECS
        rpmbuild -ba ./s2n-tls.spec
install:
        rpm -ql ../rpmbuild/RPMS/${ARCH}/s2n-tls-debugsource-1.3.2-1.fc35
	rpm -ql ../rpmbuild/RPMS/${ARCH}/s2n-tls-1.3.2-1.fc35.x86_64.rpm

