%global common_configure --with-gnome-shell=3.34 --disable-cinnamon --disable-unity --disable-xfwm --disable-plank --disable-openbox

%global common_desc Arc is a flat theme with transparent elements for GTK 3, GTK 2 and GNOME Shell, Unity, Pantheon, Xfce, MATE, Cinnamon, Budgie Desktop.

Name:		arc-theme
Version:	20190917
Release:	3%{?dist}
Summary:	A flat theme with transparent elements

License:	GPLv3+
URL:		https://github.com/arc-design/%{name}
Source0:	%{url}/archive/%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk3-devel
BuildRequires:	gtk-murrine-engine
BuildRequires:	inkscape <= 0.92
BuildRequires:	optipng
BuildRequires:	sassc

Requires:	filesystem
Requires:	gnome-themes-extra
Requires:	gtk-murrine-engine

%description
%{common_desc}
	
%prep
%autosetup -p 1
%{_bindir}/autoreconf -fiv

%build	
%configure %{common_configure}
%make_build

%install	
%make_install
	
%files
%license AUTHORS COPYING
%doc README.md
%{_datadir}/themes/*
	
%changelog

* Fri Feb 7 2020 Muhammad Ahmad <mhdxahmad93@gmail.com>
- New Version

