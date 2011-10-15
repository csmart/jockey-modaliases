Name:           parsidora-modaliases
Version:        1.0.1
Release:        1%{?dist}
Summary:        Provides modaliases for Parsidora'a additional kernel modules

License:        GPLv2+
URL:            http://parsidora.org
Source0:        rpmfusion-modules.aliases
Source1:        rpmfusion-modules-PAE.aliases

BuildArch:      noarch

%description
This package provides modaliases for kernel modules which are not installed
by default. This is used by Jockey to detect required modules for system's
hardware.

%prep

%build

%install
mkdir -p %{buildroot}%{_datadir}/jockey/{modaliases,modaliases-PAE}/
install -m 644 %{SOURCE0} %{buildroot}%{_datadir}/jockey/modaliases/
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/jockey/modaliases-PAE/

%files
%{_datadir}/jockey/modaliases*

%changelog
* Sun Oct 16 2011 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 1.0.1-1
- Add PAE modaliases

* Thu Jul 28 2011 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 1.0.0-1
- Initial version

