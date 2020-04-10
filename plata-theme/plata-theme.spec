%define git_owner       tista500
%define git_url         https://gitlab.com/%{git_owner}/%{name}
Name:           plata-theme
Summary:        Plata Gtk Theme
License:        GPL 2.0 ans SA 4.0
URL:            %{git_url}

Version:        0.9.7
Release:        1%{?dist}
Source0:        %{git_url}/-/archive/%{version}/%{name}-%{version}.tar.gz       

BuildArch:      noarch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  procps
BuildRequires:  inkscape < 1.0
BuildRequires:  parallel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  sassc    >= 3.3
BuildRequires:  zip
BuildRequires:  marco-devel >= 1.22.2


%description
Plata-theme
A Gtk+ theme based on Material Design Refresh.

%package        Plata
Summary:        A Gtk+ theme based on Material Design Refresh.
%description    Plata

%package        Plata-Lumine
Summary:        A Gtk+ theme based on Material Design Refresh.
%description    Plata-Lumine

%package        Plata-Noir
Summary:        A Gtk+ theme based on Material Design Refresh.
%description    Plata-Noir

%prep
%autosetup
%{_bindir}/autoreconf -fiv

%build
%configure \
--prefix=%{_prefix} \
--enable-parallel \
--enable-plank \
--enable-telegram \
--enable-tweetdeck \
--enable-gtk_next
%make_build

%install
%make_install

%files Plata
%license COPYING LICENSE_CC_BY_SA4
%doc README.md
%{_datadir}/themes/Plata/*
%{_datadir}/themes/Plata-Compact/*

%files Plata-Lumine
%license COPYING LICENSE_CC_BY_SA4
%doc README.md
%{_datadir}/themes/Plata-Lumine/*
%{_datadir}/themes/Plata-Lumine-Compact/*

%files Plata-Noir
%license COPYING LICENSE_CC_BY_SA4
%doc README.md
%{_datadir}/themes/Plata-Noir/*
%{_datadir}/themes/Plata-Noir-Compact/*

%files
%license COPYING LICENSE_CC_BY_SA4
%doc README.md
%{_datadir}/*

%changelog
* Fri Apr 10 2020 Muhammad Ahmad <mhdxahmad93@gmail.com> 0.9.7
- New Version

* Fri Apr 10 2020 Muhammad Ahmad <mhdxahmad93@gmail.com> 0.9.6
- New Version

* Tue Mar 10 2020 Muhammad Ahmad <mhdxahmad93@gmail.com> 0.9.4
- New Version

* Sun Mar 1 2020 Muhammad Ahmad <mhdxahmad93@gmail.com> 0.9.3
- New Version

* Fri Feb 7 2020 Muhammad Ahmad <mhdxahmad93@gmail.com> 0.9.2
- New Version

