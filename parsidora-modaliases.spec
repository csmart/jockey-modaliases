Name:           parsidora-modaliases
Version:        1.0.0
Release:        1%{?dist}
Summary:        Provides modaliases for Parsidora'a additional kernel modules

License:        GPLv2+
URL:            http://parsidora.org
Source0:        rpmfusion-modules.aliases

BuildArch:      noarch

%description
This package provides modaliases for kernel modules which are not installed
by default. This is used by Jockey to detect required modules for system's
hardware.

%prep

%build

%install
mkdir -p %{buildroot}%{_datadir}/jockey/modaliases/
install -m 644 %{SOURCE0} %{buildroot}%{_datadir}/jockey/modaliases/

%files
%{_datadir}/jockey/modaliases

%changelog
* Thu Jul 28 2011 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 1.0.0-1
- Initial version

