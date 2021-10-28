%global srcname aws-cli
%global appname awscli

%bcond_with examples

# python3-aws-crt-python
%global awscrt_version 0.12.4
%global awscrt_repo_name aws-crt-python
%global bundled_lib_dir bundled
%global awscrt_dir ${bundled_lib_dir}/awscrt

Name:           %{appname}-2
Version:        2.3.0
Release:        1%{?dist}
Summary:        Universal Command Line Environment for AWS, Version 2

License:        ASL 2.0 and MIT
URL:            https://github.com/aws/aws-cli
Source0:        %{url}/archive/%{version}/%{appname}-%{version}.tar.gz
Spirce0:        %{url}/archive/%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
Source1:        https://github.com/awslabs/%{awscrt_repo_name}/%{awscrt_version}.tar.gz#/%{awscrt_srcname}-%{awscrt_version}.tar.gz

BuildArch:      noarch
# The botocore library is no longer separate from the awscli
# Requires:       python3-botocore-2
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-toml


Requires:       python3-prompt-toolkit
Requires:       python3-colorama
Requires:       python3-cryptography
Requires:       python3-s3transfer
Provides:       bundled(python3-awscrt) == %{version}

Recommends:     groff
Obsoletes:      awscli <= 1
Obsoletes:      python3-botocore <= 1

%{?python_provide:%python_provide python3-%{name}}

%description

This package provides version 2 of the unified command line
interface to Amazon Web Services.

%pyproject_extras_subpkg -n %{srcname}-%{version}

%prep
# extract the crt first
%setup -T -b1 -c -n awscrt-crt-python-${awscrt_version}
%autosetup -n %{srcname}-%{version}

%if %{with examples}
find awscli/examples/ -type f -name '*.rst' -executable -exec chmod -x '{}' +
%else
rm -r awscli/examples
%endif

%generate_buildrequires
%pyproject_buildrequires -r requirements.txt

%build
%pyproject_wheel


%install
%pyproject_install
# rm -vf %{buildroot}%{_bindir}/{aws_bash_completer,aws_zsh_completer.sh,aws.cmd}
# install -Dpm0644 bin/aws_bash_completer \
#   %{buildroot}%{_datadir}/bash-completion/completions/aws
# install -Dpm0644 bin/aws_zsh_completer.sh \
#   %{buildroot}%{_datadir}/zsh/site-functions/_awscli
# install -Dpm0644 doc/README.rst %{buildroot}%{_datadir}/doc


%files -f %{pyproject_files}
%doc %{name}/doc/README.rst
%license %{name}/LICENSE.txt
%{_bindir}/aws
%{_bindir}/aws_completer
%{_bindir}/aws_legacy_completer
%{python3_sitelib}/awscli/
%{python3_sitelib}/awscli-%{version}-*.egg-info/
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/aws 
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_awscli

%changelog
* Fri Mar 13 2020 David Duncan <davdunc@amazon.com> - 2.0.3-2
- Modify python3-botocore dependency to python3-botocore-2

* Fri Mar 13 2020 David Duncan <davdunc@amazon.com> - 2.0.3-1
- Initial Commit for awscli version 2
