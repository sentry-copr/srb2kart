
%define _disable_source_fetch 0

Summary: Data files for Sonic Robo Blast 2 Kart
Name: srb2kart-data
Version: 1.1
Release: 2%{?dist}
License: custom
Group: Game

BuildArch: noarch

%global debug_package %{nil}

%description
Data files for Sonic Robo Blast 2 Kart

%install
%{__mkdir_p} %{buildroot}/usr/share/games/SRB2Kart
touch %{buildroot}/usr/share/games/SRB2Kart/.temporary

%files
/usr/share/games/SRB2Kart/.temporary