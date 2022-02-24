
.ONESHELL:
.PHONY: all clean setup

PACKAGER := nobody

BUILD_DIR := 
SRPMS_DIR := $(BUILD_DIR)SRPMS/

rpmbuild := rpmbuild --define "_topdir  $(abspath $(BUILD_DIR)rpmbuild)"

ARCH := $(shell arch)
SRCS = aws-c-common aws-c-cal aws-c-compression aws-checksums s2n-tls	\
aws-c-io aws-c-http aws-c-mqtt aws-c-sdkutils aws-c-auth		\
aws-c-event-stream aws-c-s3 python-awscrt awscli-2
setup:
	if [[ ! -d $(BUILD_DIR)$(SRPMS_DIR) ]]; then mkdir $(BUILD_DIR)$(SRPMS_DIR); fi
	@touch $(SRPMS_DIR)/$(shell date "+%Y%m%d").build
	@mkdir -p -v $(BUILD_DIR)rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}

build: $(SRCS)

$(SRCS):
	@install specs/$@.spec $(BUILD_DIR)rpmbuild/SPECS/
	@ls sources/$@* && install sources/$@* $(BUILD_DIR)rpmbuild/SOURCES/
	@pushd $(BUILD_DIR)rpmbuild/SOURCES
	if [[ -f $@*.tar.gz ]]; then rm -f $@.*.tar.gz; fi
	spectool --get-files ../SPECS/$@.spec
	popd
	$(rpmbuild)  -ba $(BUILD_DIR)rpmbuild/SPECS/$@.spec
	sudo rpm -ivh $(BUILD_DIR)rpmbuild/RPMS/$(ARCH)/$@*.rpm

install:
	install -m 660  $(BUILD_DIR)rpmbuild/SRPMS/*.src.rpm $(SRPMS_DIR)


all: setup build install 

clean:
	sudo dnf remove -y awscli-2*
	sudo dnf remove -y python-awscrt*
	sudo dnf remove -y aws-c-s3*
	sudo dnf remove -y aws-c-event-stream*
	sudo dnf remove -y aws-c-auth* 
	sudo dnf remove -y aws-c-sdkutils*
	sudo dnf remove -y aws-c-mqtt*
	sudo dnf remove -y aws-c-http*
	sudo dnf remove -y aws-c-compression*
	sudo dnf remove -y aws-checksums*
	sudo dnf remove -y aws-c-io*
	sudo dnf remove -y s2n-tls*
	sudo dnf remove -y aws-c-cal*
	sudo dnf remove -y aws-c-common*
	rm -fr $(BUILD_DIR)rpmbuild 
	rm -r $(SRPMS_DIR)
