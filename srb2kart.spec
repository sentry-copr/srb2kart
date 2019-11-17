%global debug_package %{nil}

Summary: A kart racing mod based on the 3D Sonic the Hedgehog fangame Sonic Robo Blast 2, based on a modified version of Doom Legacy.
Name: srb2kart
Version: 1.1
%define LongVersion 11
%define dataversion 1.1
Release: 2%{?dist}
License: GPLv2
Group: Game
#Source:  https://github.com/STJr/Kart-Public/releases/download/v%{version}/srb2kart-v%{LongVersion}-patch.zip
Source: https://github.com/STJr/Kart-Public/archive/v%{version}.zip
Source1: srb2kart.desktop
Source2: srb2kart-opengl.desktop
Source3: srb2kart-getcontent
URL: https://mb.srb2.org/showthread.php?t=43708

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

Requires:       SDL2
Requires:       SDL2_mixer
Requires:       libpng
Requires:       game-music-emu
Requires:       libupnp

# Required to unpack the game files
Requires:       bsdtar
Requires:       unzip

%description
A kart racing mod based on the 3D Sonic the Hedgehog fangame Sonic Robo Blast 2, based on a modified version of Doom Legacy.


%prep
%setup -q -c -n %{name}-%{version}

%build
cd Kart-Public-%{version}/src

[ "%{__isa_bits}" == "64" ] && IS64BIT="64" || IS64BIT=""
# Don't compress with UPX
make NOUPX=1 LINUX$IS64BIT=1

%install
# icon + .desktop
install -Dm644 %{SOURCE1} %{buildroot}/usr/share/applications/srb2kart.desktop
install -m644  %{SOURCE2} %{buildroot}/usr/share/applications/srb2kart-opengl.desktop

cd Kart-Public-%{version}
[ "%{__isa_bits}" == "64" ] && IS64BIT="64" || IS64BIT=""

install -Dm755 bin/Linux$IS64BIT/Release/lsdl2srb2kart \
               %{buildroot}/usr/bin/srb2kart
install -Dm644 src/sdl/SDL_icon.xpm \
               %{buildroot}/usr/share/pixmaps/srb2kart.xpm

install -m755 %{SOURCE3} %{buildroot}/usr/bin/srb2kart-getcontent

%files
/usr/bin/srb2kart
/usr/bin/srb2kart-getcontent
/usr/share/pixmaps/srb2kart.xpm
/usr/share/applications/srb2kart.desktop
/usr/share/applications/srb2kart-opengl.desktop
