%global         debug_package %{nil}

Summary:        A kart racing mod based on the 3D Sonic the Hedgehog fangame Sonic Robo Blast 2, based on a modified version of Doom Legacy.
Name:           srb2kart
Version:        1.3

Release:        2%{?dist}
License:        GPLv2
URL:            https://mb.srb2.org/showthread.php?t=43708
Source0:        https://github.com/STJr/Kart-Public/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        srb2kart.desktop
Source2:        srb2kart-opengl.desktop

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  mesa-libGLU-devel
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_mixer-devel
BuildRequires:  libpng-devel
BuildRequires:  zlib-devel
BuildRequires:  game-music-emu-devel
BuildRequires:  libupnp-devel
BuildRequires:  nasm
BuildRequires:  libcurl-devel

Requires:       SDL2
Requires:       SDL2_mixer
Requires:       libpng
Requires:       game-music-emu
Requires:       libupnp
# license of assets is unclear, no response when asked
Requires:       lpf-srb2kart-data

%description
A kart racing mod based on the 3D Sonic the Hedgehog fangame Sonic Robo Blast 2, based on a modified version of Doom Legacy.


%prep
%autosetup -n Kart-Public-%{version}

%build
cd src

[ "%{__isa_bits}" == "64" ] && IS64BIT="64" || IS64BIT=""

%{set_build_flags}
%make_build NOUPX=1 LINUX$IS64BIT=1 ECHO=1

%install
# icon + .desktop
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/applications/srb2kart.desktop
install -m644  %{SOURCE2} %{buildroot}%{_datadir}/applications/srb2kart-opengl.desktop

[ "%{__isa_bits}" == "64" ] && IS64BIT="64" || IS64BIT=""

install -Dm755 bin/Linux$IS64BIT/Release/lsdl2srb2kart \
               %{buildroot}/usr/bin/srb2kart
install -Dm644 src/sdl/SDL_icon.xpm \
               %{buildroot}%{_datadir}/pixmaps/srb2kart.xpm

%files
%{_bindir}/srb2kart
%{_datadir}/pixmaps/srb2kart.xpm
%{_datadir}/applications/srb2kart.desktop
%{_datadir}/applications/srb2kart-opengl.desktop

%changelog
* Tue Jun 08 2021 Jan Drögehoff <sentrycraft123@gmail.com> - 1.3-2
- move to an lpf release model

