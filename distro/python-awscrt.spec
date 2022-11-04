Name:           python-awscrt
Version:        0.12.6
Release:        3%{?dist}
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
BuildRequires:  aws-c-common-devel
BuildRequires:  aws-c-sdkutils-devel
BuildRequires:  aws-c-cal-devel
BuildRequires:  aws-c-io-devel
BuildRequires:  aws-checksums-devel
BuildRequires:  aws-c-compression-devel
BuildRequires:  aws-c-event-stream-devel
BuildRequires:  aws-c-http-devel
BuildRequires:  aws-c-auth-devel
BuildRequires:  aws-c-mqtt-devel
BuildRequires:  aws-c-s3-devel

Requires:  openssl
Requires:  s2n-tls-libs
Requires:  aws-c-common-libs
Requires:  aws-c-sdkutils-libs
Requires:  aws-c-cal-libs
Requires:  aws-c-io-libs
Requires:  aws-checksums-libs
Requires:  aws-c-compression-libs
Requires:  aws-c-event-stream-libs
Requires:  aws-c-http-libs
Requires:  aws-c-auth-libs
Requires:  aws-c-mqtt-libs
Requires:  aws-c-s3-libs


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
* Tue Feb 22 2022 David Duncan <davdunc@amazon.com> - 0.12.6-3
- Updated for package review

* Wed Feb 02 2022 David Duncan <davdunc@amazon.com> - 0.12.6-2
- Prepare for package review

* Thu Jan 20 2022 Kyle Knapp <kyleknap@amazon.com> - 0.12.6-1
- initial package development
