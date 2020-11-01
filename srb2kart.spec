%global debug_package %{nil}

Summary: A kart racing mod based on the 3D Sonic the Hedgehog fangame Sonic Robo Blast 2, based on a modified version of Doom Legacy.
Name: srb2kart
Version: 1.3
%global longVersion 13
%global dataVersion 1.3
# the source code at the 1.2 tag is broken on gcc 10
#%%global commit e229aabf229058e90c2a76552ef942be05ae71e5
Release: 1%{?dist}
License: GPLv2
Group: Game
Source0: https://github.com/STJr/Kart-Public/archive/v%{version}.tar.gz
#Source0: https://github.com/STJr/Kart-Public/archive/%{commit}.tar.gz#/%{name}-%{version}-%{commit}.tar.gz
Source1: srb2kart.desktop
Source2: srb2kart-opengl.desktop
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
BuildRequires:	libcurl-devel

Requires:       SDL2
Requires:       SDL2_mixer
Requires:       libpng
Requires:       game-music-emu
Requires:       libupnp

# Required to unpack the game files
Requires:       bsdtar
Requires:       /usr/bin/install

%description
A kart racing mod based on the 3D Sonic the Hedgehog fangame Sonic Robo Blast 2, based on a modified version of Doom Legacy.


%prep
#%%autosetup -n Kart-Public-%{commit}
%autosetup -n Kart-Public-%{version}

%build
cd src

[ "%{__isa_bits}" == "64" ] && IS64BIT="64" || IS64BIT=""
# Don't compress with UPX
%make_build NOUPX=1 LINUX$IS64BIT=1

%install
# icon + .desktop
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/applications/srb2kart.desktop
install -m644  %{SOURCE2} %{buildroot}%{_datadir}/applications/srb2kart-opengl.desktop

[ "%{__isa_bits}" == "64" ] && IS64BIT="64" || IS64BIT=""

install -Dm755 bin/Linux$IS64BIT/Release/lsdl2srb2kart \
               %{buildroot}/usr/bin/srb2kart
install -Dm644 src/sdl/SDL_icon.xpm \
               %{buildroot}%{_datadir}/pixmaps/srb2kart.xpm

mkdir -p %{buildroot}%{_prefix}/local/games/SRB2Kart

%post
TMP_DIR=$(mktemp -d)
pushd $TMP_DIR

wget -O Installer.exe https://github.com/STJr/Kart-Public/releases/download/v%{dataVersion}/srb2kart-v%{longVersion}-Installer.exe
bsdtar xfv Installer.exe
install -Dm644 {music,textures,gfx,maps,sounds,chars,bonuschars}.kart srb2.srb %{_prefix}/local/games/SRB2Kart

wget -O Patcher.exe https://github.com/STJr/Kart-Public/releases/download/v%{dataVersion}/srb2kart-v%{longVersion}-patcher.exe
bsdtar xfv Patcher.exe
install -p -Dm664 patch.kart %{_prefix}/local/games/SRB2Kart

popd

rm -rf $TMP_DIR

%postun
rm -rf %{_prefix}/local/games/SRB2Kart

%files
%{_bindir}/srb2kart
%{_datadir}/pixmaps/srb2kart.xpm
%{_datadir}/applications/srb2kart.desktop
%{_datadir}/applications/srb2kart-opengl.desktop
%dir %{_prefix}/local/games/SRB2Kart
