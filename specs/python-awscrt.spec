Name:           python-awscrt
Version:        0.16.0
Release:        1%{?dist}
Summary:        Python bindings for the AWS Common Runtime
License:        AL-2.0
URL:            https://github.com/awslabs/aws-crt-python
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         python-awscrt-setup.patch

BuildRequires:  python3-devel
BuildRequires:  python3-wheel

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  openssl-devel
BuildRequires:  s2n-tls-devel
BuildRequires:  aws-c-common-devel = 0.8.5
BuildRequires:  aws-c-sdkutils-devel = 0.1.7
BuildRequires:  aws-c-cal-devel = 0.5.20
BuildRequires:  aws-c-io-devel = 0.13.11
BuildRequires:  aws-checksums-devel = 0.1.72
BuildRequires:  aws-c-compression-devel = 0.2.16
BuildRequires:  aws-c-event-stream-devel = 0.2.15
BuildRequires:  aws-c-http-devel = 0.6.27
BuildRequires:  aws-c-auth-devel = 0.6.21
BuildRequires:  aws-c-mqtt-devel = 0.8.0
BuildRequires:  aws-c-s3-devel = 0.2.0

Requires:  openssl
Requires:  s2n-tls-libs
Requires:  aws-c-common-libs = 0.8.5
Requires:  aws-c-sdkutils-libs = 0.1.7
Requires:  aws-c-cal-libs = 0.5.20
Requires:  aws-c-io-libs = 0.13.11
Requires:  aws-checksums-libs = 0.1.72
Requires:  aws-c-compression-libs = 0.2.16
Requires:  aws-c-event-stream-libs = 0.2.15
Requires:  aws-c-http-libs = 0.6.27
Requires:  aws-c-auth-libs = 0.6.21
Requires:  aws-c-mqtt-libs = 0.8.0
Requires:  aws-c-s3-libs = 0.2.0


%global _description %{expand:
Python bindings for the AWS Common Runtime}

%description %_description

%package -n python3-awscrt
Summary:        %{summary}

%description -n python3-awscrt %_description


%prep
%autosetup -p1 -n aws-crt-python-%{version}

# Fix the CRT version number to represent the
# actual tagged version is instead of the placeholder
# 1.0.0-dev
sed -i "s/1.0.0-dev/%{version}/g" awscrt/__init__.py

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files awscrt



%files -n python3-awscrt -f %{pyproject_files}
%doc README.md
%{python3_sitearch}/_awscrt%{python3_ext_suffix}


%changelog
* Sat Dec 03 2022 David Duncan <davdunc@amazon.com> - 0.16.0-1
- bump spec to 0.16.0 release

* Tue Feb 22 2022 David Duncan <davdunc@amazon.com> - 0.12.6-3
- Updated for package review

* Wed Feb 02 2022 David Duncan <davdunc@amazon.com> - 0.12.6-2
- Prepare for package review

* Thu Jan 20 2022 Kyle Knapp <kyleknap@amazon.com> - 0.12.6-1
- initial package development
