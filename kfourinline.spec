#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kfourinline
Version  : 20.08.0
Release  : 23
URL      : https://download.kde.org/stable/release-service/20.08.0/src/kfourinline-20.08.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/20.08.0/src/kfourinline-20.08.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/20.08.0/src/kfourinline-20.08.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0 LGPL-2.0
Requires: kfourinline-bin = %{version}-%{release}
Requires: kfourinline-data = %{version}-%{release}
Requires: kfourinline-license = %{version}-%{release}
Requires: kfourinline-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kdnssd-dev
BuildRequires : libkdegames-dev
BuildRequires : qtbase-dev mesa-dev

%description
GENERAL NOTE:
http://games.kde.org/

%package bin
Summary: bin components for the kfourinline package.
Group: Binaries
Requires: kfourinline-data = %{version}-%{release}
Requires: kfourinline-license = %{version}-%{release}

%description bin
bin components for the kfourinline package.


%package data
Summary: data components for the kfourinline package.
Group: Data

%description data
data components for the kfourinline package.


%package doc
Summary: doc components for the kfourinline package.
Group: Documentation

%description doc
doc components for the kfourinline package.


%package license
Summary: license components for the kfourinline package.
Group: Default

%description license
license components for the kfourinline package.


%package locales
Summary: locales components for the kfourinline package.
Group: Default

%description locales
locales components for the kfourinline package.


%prep
%setup -q -n kfourinline-20.08.0
cd %{_builddir}/kfourinline-20.08.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1597781850
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1597781850
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kfourinline
cp %{_builddir}/kfourinline-20.08.0/COPYING %{buildroot}/usr/share/package-licenses/kfourinline/fafaf6b2753f82aa8df1d206d6b76c2241c2dfa8
cp %{_builddir}/kfourinline-20.08.0/COPYING.DOC %{buildroot}/usr/share/package-licenses/kfourinline/bd75d59f9d7d9731bfabdc48ecd19e704d218e38
cp %{_builddir}/kfourinline-20.08.0/COPYING.LIB %{buildroot}/usr/share/package-licenses/kfourinline/ba8966e2473a9969bdcab3dc82274c817cfd98a1
pushd clr-build
%make_install
popd
%find_lang kfourinline

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kfourinline
/usr/bin/kfourinlineproc

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kfourinline.desktop
/usr/share/config.kcfg/kwin4.kcfg
/usr/share/icons/hicolor/128x128/apps/kfourinline.png
/usr/share/icons/hicolor/16x16/apps/kfourinline.png
/usr/share/icons/hicolor/22x22/apps/kfourinline.png
/usr/share/icons/hicolor/32x32/apps/kfourinline.png
/usr/share/icons/hicolor/48x48/apps/kfourinline.png
/usr/share/icons/hicolor/64x64/apps/kfourinline.png
/usr/share/kfourinline/grafix/default.desktop
/usr/share/kfourinline/grafix/default.rc
/usr/share/kfourinline/grafix/default.svg
/usr/share/kfourinline/grafix/gray_reflection.desktop
/usr/share/kfourinline/grafix/gray_reflection.rc
/usr/share/kfourinline/grafix/gray_reflection.svg
/usr/share/kfourinline/grafix/yellow.desktop
/usr/share/kfourinline/grafix/yellow.rc
/usr/share/kfourinline/grafix/yellow.svg
/usr/share/kfourinline/grafix/yellow_reflection.desktop
/usr/share/kfourinline/grafix/yellow_reflection.rc
/usr/share/metainfo/org.kde.kfourinline.appdata.xml
/usr/share/qlogging-categories5/kfourinline.categories

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/de/kfourinline/index.cache.bz2
/usr/share/doc/HTML/de/kfourinline/index.docbook
/usr/share/doc/HTML/en/kfourinline/gameboard.png
/usr/share/doc/HTML/en/kfourinline/index.cache.bz2
/usr/share/doc/HTML/en/kfourinline/index.docbook
/usr/share/doc/HTML/en/kfourinline/settings.png
/usr/share/doc/HTML/es/kfourinline/index.cache.bz2
/usr/share/doc/HTML/es/kfourinline/index.docbook
/usr/share/doc/HTML/et/kfourinline/index.cache.bz2
/usr/share/doc/HTML/et/kfourinline/index.docbook
/usr/share/doc/HTML/fr/kfourinline/index.cache.bz2
/usr/share/doc/HTML/fr/kfourinline/index.docbook
/usr/share/doc/HTML/it/kfourinline/index.cache.bz2
/usr/share/doc/HTML/it/kfourinline/index.docbook
/usr/share/doc/HTML/nl/kfourinline/index.cache.bz2
/usr/share/doc/HTML/nl/kfourinline/index.docbook
/usr/share/doc/HTML/pl/kfourinline/index.cache.bz2
/usr/share/doc/HTML/pl/kfourinline/index.docbook
/usr/share/doc/HTML/pt/kfourinline/index.cache.bz2
/usr/share/doc/HTML/pt/kfourinline/index.docbook
/usr/share/doc/HTML/pt_BR/kfourinline/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kfourinline/index.docbook
/usr/share/doc/HTML/sv/kfourinline/index.cache.bz2
/usr/share/doc/HTML/sv/kfourinline/index.docbook
/usr/share/doc/HTML/uk/kfourinline/gameboard.png
/usr/share/doc/HTML/uk/kfourinline/index.cache.bz2
/usr/share/doc/HTML/uk/kfourinline/index.docbook
/usr/share/doc/HTML/uk/kfourinline/settings.png

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kfourinline/ba8966e2473a9969bdcab3dc82274c817cfd98a1
/usr/share/package-licenses/kfourinline/bd75d59f9d7d9731bfabdc48ecd19e704d218e38
/usr/share/package-licenses/kfourinline/fafaf6b2753f82aa8df1d206d6b76c2241c2dfa8

%files locales -f kfourinline.lang
%defattr(-,root,root,-)

