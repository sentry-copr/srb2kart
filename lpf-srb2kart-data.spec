%global     debug_package %{nil}

%define     target_pkg %(t=%{name}; echo ${t#lpf-})

Name:       lpf-srb2kart-data
Summary:    A kart racing mod based on the 3D Sonic the Hedgehog fangame Sonic Robo Blast 2, based on a modified version of Doom Legacy.
Version:    1.3

Release:    1%{?dist}
License:    GPLv2
URL:        https://mb.srb2.org/showthread.php?t=43708
BuildArch:  noarch

Source0:    srb2kart-data.spec.in

BuildRequires:  desktop-file-utils
BuildRequires:  lpf >= 0.1
Requires:       lpf >= 0.1

%description
Bootstrap package allowing the lpf system to build the non-redistributable
srb2kart-data package.

%prep
%setup -cT

%build

%install
/usr/share/lpf/scripts/lpf-setup-pkg %{buildroot} %{SOURCE0}
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%check
%lpf_check %{SOURCE0}

%post
%lpf_post

%postun
%lpf_postun
%lpf_triggerpostun

%files
%{_datadir}/applications/%{name}.desktop
%{_datadir}/lpf/packages/%{target_pkg}
%attr(775,pkg-build,pkg-build) /var/lib/lpf/packages/%{target_pkg}

%changelog
* Tue Jun 08 2021 Jan Drögehoff <sentrycraft123@gmail.com> - 1.3-1
- initial lpf package

