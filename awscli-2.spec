%global srcname aws-cli
%global pkgname awscli
%global branchname poc-sdist-refresh
%bcond_with examples
%bcond_with test
%bcond_with download_deps

Name:     %{pkgname}-2
Version:  2.2.1
Release:  1%{?dist}
Summary:  Universal Command Line Environment for AWS, Version 2

License:  ASL 2.0 and MIT
URL:      https://github.com/kyelknapp

Source0:  %{url}/%{srcname}/archive/%{branchname}/%{version}/%{pkgname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  autoconf
BuildRequires:  coreutils
BuildRequires:  python3-wheel
BuildRequires:  python3-devel
Provides: bundled(python3-pyinstaller) == 4.2
Provides: bundled(python3-jsonschema) == 2.5.1
Provides: bundled(python3-awscrt)

%description

Version 2 of the unified command line interface to Amazon Web Services.

%prep
%autosetup -n %{srcname}-%{branchname} -p1 


%if %{with examples}
find awscli/examples/ -type f -name '*.rst' -executable -exec chmod -x '{}' +
%else
rm -vr awscli/examples
%endif
%if %{with test}
%else

%endif
%build -n %{srcname}-%{branchname}

# Can't do this in koji
%configure

make build

%install 
rm -rf $RPM_BUILD_ROOT
%make_install

%files
%docs
%config(noreplace)
%
