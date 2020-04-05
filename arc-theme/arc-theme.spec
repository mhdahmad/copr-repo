%global common_configure --with-gnome-shell=3.36 --disable-cinnamon --disable-unity --disable-xfwm --disable-plank --disable-openbox --disable-lighter

%global common_desc Arc is a flat theme with transparent elements for GTK 3, GTK 2 and GNOME Shell, Unity, Pantheon, Xfce, MATE, Cinnamon, Budgie Desktop.

%global         branch master

Name:		arc-theme
Version:	20200328
Release:	1%{?dist}
Summary:	A flat theme with transparent elements

License:	GPLv3+
URL:		https://github.com/jnsh/%{name}
Source0:	%{url}/archive/master.zip#/%{name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk3-devel
BuildRequires:	gtk-murrine-engine
BuildRequires:	inkscape < 1.0
BuildRequires:	optipng
BuildRequires:	sassc
BuildRequires:  pkgconf

Requires:	filesystem
Requires:	gnome-themes-extra
Requires:	gtk-murrine-engine

%description
%{common_desc}

%prep
%autosetup -n %{name}-%{branch}

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

* Mon Apr 6 2020 Muhammad Ahmad <mhdxahmad93@gmail.com>
- Switch to new repository jnsh/arc-theme

* Fri Feb 7 2020 Muhammad Ahmad <mhdxahmad93@gmail.com>
- New Version

