%global         source_name Bibata_Cursor

Name:		bibata-cursor-theme
Version:	0.4.2
Release:	1%{?dist}
Summary:	Material Based Cursor Theme

License:	GPLv3+
URL:		https://github.com/KaizIqbal/Bibata_Cursor
Source0:	%{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	inkscape < 1.0
BuildRequires:	gnome-themes-extra
BuildRequires:	xcursorgen
BuildRequires:	git
BuildRequires:	python3
BuildRequires:	python3-pip
BuildRequires:	python3-pillow

%description
Material Based Cursor Theme.
	
%prep
%autosetup -n %{source_name}-%{version}

%build
for varient in Bibata_Classic Bibata_Amber Bibata_Ice Bibata_Oil  ; do
  echo "Building ${varient} is started..."
  python3 render-cursors.py ./src/${varient}/source-cursors.svg -o -a --name ${varient}
  ./tweak.sh ${varient}
  ./x11-make.sh ${varient}
  cp src/${varient}/*.theme ${varient}/out/X11/${varient}
done

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p "$RPM_BUILD_ROOT/%{_datadir}/icons"
for varient in Bibata_Classic Bibata_Amber Bibata_Ice Bibata_Oil  ; do
  mv $RPM_BUILD_DIR/%{source_name}-%{version}/${varient}/out/X11/${varient} "$RPM_BUILD_ROOT/%{_datadir}/icons"
done

%files
%license LICENSE
%doc README.md
%{_datadir}/icons/*
	
%changelog

* Tue Feb 11 2020 Muhammad Ahmad <mhdxahmad93@gmail.com>
- New Release - v0.4.2
