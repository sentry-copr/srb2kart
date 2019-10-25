
%define _disable_source_fetch 0

Summary: Data files for Sonic Robo Blast 2 Kart
Name: srb2kart-data
Version: 1.1
%define LongVersion 11
Release: 1%{?dist}
License: custom
Group: Game
Source: https://github.com/STJr/Kart-Public/releases/download/v%{version}/srb2kart-v%{LongVersion}-Installer.exe
URL: https://mb.srb2.org/showthread.php?t=43708

BuildArch: noarch
BuildRequires: bsdtar

%global debug_package %{nil}

%description
Data files for Sonic Robo Blast 2 Kart

%prep
%setup -T -q -c
bsdtar xfv %_topdir/SOURCES/srb2kart-v%{LongVersion}-Installer.exe
                        
%install
install -d %{buildroot}/usr/share/games/SRB2Kart
install -m644 {music,textures,gfx,maps,sounds,chars,bonuschars}.kart srb2.srb %{buildroot}/usr/share/games/SRB2Kart

%files
/usr/share/games/SRB2Kart