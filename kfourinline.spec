#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kfourinline
Version  : 22.12.0
Release  : 47
URL      : https://download.kde.org/stable/release-service/22.12.0/src/kfourinline-22.12.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/22.12.0/src/kfourinline-22.12.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/22.12.0/src/kfourinline-22.12.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GFDL-1.2 GPL-2.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: kfourinline-bin = %{version}-%{release}
Requires: kfourinline-data = %{version}-%{release}
Requires: kfourinline-license = %{version}-%{release}
Requires: kfourinline-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kdnssd-dev
BuildRequires : libkdegames-dev

%description
# KFourInLine
KFourInLine is a board game for two players based on the Connect-Four game. The
players try to build up a row of four pieces using different strategies.

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
%setup -q -n kfourinline-22.12.0
cd %{_builddir}/kfourinline-22.12.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1670540559
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1670540559
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kfourinline
cp %{_builddir}/kfourinline-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/kfourinline/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/kfourinline-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kfourinline/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kfourinline-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kfourinline/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/kfourinline-%{version}/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/kfourinline/7697008f58568e61e7598e796eafc2a997503fde || :
cp %{_builddir}/kfourinline-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kfourinline/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
cp %{_builddir}/kfourinline-%{version}/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kfourinline/a4c60b3fefda228cd7439d3565df043192fef137 || :
cp %{_builddir}/kfourinline-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kfourinline/a4c60b3fefda228cd7439d3565df043192fef137 || :
cp %{_builddir}/kfourinline-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/kfourinline/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567 || :
cp %{_builddir}/kfourinline-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kfourinline/19d98e1b6f8ef12849ea4012a052d3907f336c91 || :
cp %{_builddir}/kfourinline-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kfourinline/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kfourinline-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kfourinline/e458941548e0864907e654fa2e192844ae90fc32 || :
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
/usr/share/doc/HTML/ca/kfourinline/gameboard.png
/usr/share/doc/HTML/ca/kfourinline/index.cache.bz2
/usr/share/doc/HTML/ca/kfourinline/index.docbook
/usr/share/doc/HTML/ca/kfourinline/settings.png
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
/usr/share/package-licenses/kfourinline/19d98e1b6f8ef12849ea4012a052d3907f336c91
/usr/share/package-licenses/kfourinline/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/kfourinline/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/kfourinline/7697008f58568e61e7598e796eafc2a997503fde
/usr/share/package-licenses/kfourinline/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567
/usr/share/package-licenses/kfourinline/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/kfourinline/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/kfourinline/a4c60b3fefda228cd7439d3565df043192fef137
/usr/share/package-licenses/kfourinline/e458941548e0864907e654fa2e192844ae90fc32

%files locales -f kfourinline.lang
%defattr(-,root,root,-)

