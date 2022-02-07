
.ONESHELL:
.PHONY: all clean setup

PACKAGER := nobody

BUILD_DIR := ./
SRPMS_DIR := $(BUILD_DIR)SRPMS/

rpmbuild := rpmbuild --define "_topdir  $(abspath $(BUILD_DIR)rpmbuild)"

ARCH := $(shell arch)
SRCS = aws-c-common.spec, aws-c-auth.spec, aws-c-cal.spec,		\
aws-c-compression.spec, aws-c-event-stream.spec, aws-checksums.spec,	\
aws-c-http.spec, aws-c-io.spec, awscli-2.spec, aws-c-mqtt.spec,		\
aws-c-s3.spec, aws-c-sdkutils.spec, python-awscrt.spec, s2n-tls.spec
setup:
	if [[ ! -d $(BUILD_DIR)$(SRPMS_DIR) ]]; then mkdir $(BUILD_DIR)$(SRPMS_DIR); fi
	@touch $(SRPMS_DIR)/$(shell date "+%Y%m%d").build
	@mkdir -p -v $(BUILD_DIR)rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}

build: $(SRCS)

$(SRCS):
	@install specs/$@.spec $(BUILD_DIR)rpmbuild/SPECS/
	@pushd $(BUILD_DIR)rpmbuild/SOURCES
	if [[ -f $@*.tar.gz ]]; then rm -f $@.*.tar.gz; fi
	spectool --get-files ../SPECS/$@.spec
	if [[ -f sources/$@*.patch ]] ; then cp sources/$@* $(BUILD_DIR)rpmbuild/SOURCES/ ; fi
	popd
	$(rpmbuild)  -ba $(BUILD_DIR)rpmbuild/SPECS/$@.spec
	sudo rpm -ivh $(BUILD_DIR)rpmbuild/RPMS/$(ARCH)/$@*.rpm

install:
	install -m 660  $(BUILD_DIR)rpmbuild/SRPMS/*.src.rpm $(SRPMS_DIR)


all: setup build install 

clean:
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
