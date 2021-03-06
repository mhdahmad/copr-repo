%global common_configure --with-gnome-shell=3.36 --disable-cinnamon --disable-unity --disable-xfwm --disable-openbox --disable-lighter

%global common_desc Arc is a flat theme with transparent elements for GTK 3, GTK 2 and GNOME Shell, Unity, Pantheon, Xfce, MATE, Cinnamon, Budgie Desktop.

%global         branch master

Name:		arc-theme
Version:	20200513
Release:	1%{?dist}
Summary:	A flat theme with transparent elements

License:	GPLv3+
URL:		https://github.com/jnsh/%{name}
Source0:	%{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk3-devel
BuildRequires:	gtk-murrine-engine
BuildRequires:	inkscape
BuildRequires:	optipng
BuildRequires:	sassc
BuildRequires:  pkgconf

Requires:	filesystem
Requires:	gnome-themes-extra
Requires:	gtk-murrine-engine

%description
%{common_desc}

%prep
%autosetup -n %{name}-%{version}
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
* Thu May 14 2020 Muhammad Ahmad <mhdxahmad93@gmail.com>
- New Version

* Sun May 03 2020 Muhammad Ahmad <mhdxahmad93@gmail.com>
- New Version

* Mon Apr 27 2020 Muhammad Ahmad <mhdxahmad93@gmail.com>
- New Version

* Wed Apr 15 2020 Muhammad Ahmad <mhdxahmad93@gmail.com>
- New Version

* Sun Apr 12 2020 Muhammad Ahmad <mhdxahmad93@gmail.com>
- Switch to new repository jnsh/arc-theme - gnome 3.34

* Mon Apr 6 2020 Muhammad Ahmad <mhdxahmad93@gmail.com>
- Switch to new repository jnsh/arc-theme

* Fri Feb 7 2020 Muhammad Ahmad <mhdxahmad93@gmail.com>
- New Version

