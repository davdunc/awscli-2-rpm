Name:           python-awscrt
Version:        0.12.6
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
BuildRequires:  aws-c-common-devel = 1:0.6.14
BuildRequires:  aws-c-sdkutils-devel = 1:0.1.1
BuildRequires:  aws-c-cal-devel = 1:0.5.12
BuildRequires:  aws-c-io-devel = 1:0.10.12
BuildRequires:  aws-checksums-devel = 1:0.1.12
BuildRequires:  aws-c-compression-devel = 1:0.2.14
BuildRequires:  aws-c-event-stream-devel = 1:0.2.7
BuildRequires:  aws-c-http-devel = 1:0.6.8
BuildRequires:  aws-c-auth-devel = 1:0.6.5
BuildRequires:  aws-c-mqtt-devel = 1:0.7.8
BuildRequires:  aws-c-s3-devel = 1:0.1.27

Requires:  openssl
Requires:  s2n-tls-libs
Requires:  aws-c-common-libs = 1:0.6.14
Requires:  aws-c-sdkutils-libs = 1:0.1.1
Requires:  aws-c-cal-libs = 1:0.5.12
Requires:  aws-c-io-libs = 1:0.10.12
Requires:  aws-checksums-libs = 1:0.1.12
Requires:  aws-c-compression-libs = 1:0.2.14
Requires:  aws-c-event-stream-libs = 1:0.2.7
Requires:  aws-c-http-libs = 1:0.6.8
Requires:  aws-c-auth-libs = 1:0.6.5
Requires:  aws-c-mqtt-libs = 1:0.7.8
Requires:  aws-c-s3-libs = 1:0.1.27


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
* Thu Jan 20 2022 Kyle Knapp <kyleknap@amazon.com>
- 
