%global         asset_dir %{_prefix}/local/games/SRB2Kart

Summary:        A kart racing mod based on the 3D Sonic the Hedgehog fangame Sonic Robo Blast 2, based on a modified version of Doom Legacy.
Name:           srb2kart
Version:        1.6
Release:        1%{?dist}
License:        GPLv2
URL:            https://mb.srb2.org/addons/srb2kart.2435/
Source0:        https://github.com/STJr/Kart-Public/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/STJr/Kart-Public/releases/download/v%{version}/AssetsLinuxOnly.zip#/%{name}-assets.zip
Source2:        srb2kart.desktop
Source3:        srb2kart-opengl.desktop

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  mesa-libGLU-devel
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_mixer-devel
BuildRequires:  libpng-devel
BuildRequires:  zlib-devel
BuildRequires:  game-music-emu-devel
BuildRequires:  libupnp-devel
BuildRequires:  libcurl-devel
BuildRequires:  unzip
BuildRequires:  cmake

Requires:       %{name}-data = %{version}
Obsoletes:      lpf-srb2kart-data <= 1.3

%description
A kart racing mod based on the 3D Sonic the Hedgehog fangame Sonic Robo Blast 2, based on a modified version of Doom Legacy.

%package data
Summary:        game data for %{name}
BuildArch:      noarch

%description data
game data for %{name}

%prep
%autosetup -n Kart-Public-%{version}

mkdir -p assets/installer
cd assets/installer
unzip %{SOURCE1}

%build
%cmake \
    -DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo

%cmake_build

%install
install -Dm755 %{__cmake_builddir}/bin/srb2kart \
               %{buildroot}/%{_bindir}/srb2kart
install -Dm644 src/sdl/SDL_icon.xpm \
               %{buildroot}%{_datadir}/pixmaps/srb2kart.xpm

# icon + .desktop
install -Dm644 %{SOURCE2} %{buildroot}%{_datadir}/applications/srb2kart.desktop
install -m644  %{SOURCE3} %{buildroot}%{_datadir}/applications/srb2kart-opengl.desktop

# assets
mkdir -p %{buildroot}%{asset_dir}/
cp -pr assets/installer/* %{buildroot}%{asset_dir}/

%files
%{_bindir}/srb2kart
%{_datadir}/pixmaps/srb2kart.xpm
%{_datadir}/applications/srb2kart.desktop
%{_datadir}/applications/srb2kart-opengl.desktop

%files data
%{asset_dir}/

%changelog
* Wed Apr 19 2023 Jan Drögehoff <sentrycraft123@gmail.com> - 1.6-1
- Update to 1.6
- Migrate to cmake
- Bundle assets

* Tue Jun 08 2021 Jan Drögehoff <sentrycraft123@gmail.com> - 1.3-3
- move to an lpf release model
