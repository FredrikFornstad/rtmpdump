%define commit fa8646daeb19dfd12c181f7d19de708d623704c0
%global libver 1

Summary: A toolkit for RTMP streams
Name: rtmpdump
Version: 2.4
Release: 4%{?dist}
License: GPLv2
Group: System Environment/Libraries
URL: http://rtmpdump.mplayerhq.hu/
Source0: https://github.com/mirror/rtmpdump/archive/%{commit}.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: openssl-devel
Requires: %{name}-libs_%{libver}

%description
rtmpdump is a toolkit for RTMP streams. All forms of RTMP are
supported, including rtmp://, rtmpt://, rtmpe://, rtmpte://, and
rtmps://.

%package libs_%{libver}
Summary: rtmpdump shared library
Group: Development/Libraries
Obsoletes: librtmp*

%description libs_%{libver}
This package contains the rtmpdump shared library

%package devel
Summary: rtmpdump shared library development files
Group: Development/Libraries
Requires:  %{name}-libs_%{libver}

%description devel
This package contains the rtmpdump shared library development files

%prep
%setup -q -n %{name}-%{commit}

%build
make

%install
rm -rf %{buildroot}
make install \
  bindir=%{_bindir} \
  sbindir=%{_sbindir} \
  mandir=%{_mandir} \
  incdir=%{_includedir}/librtmp \
  libdir=%{_libdir} \
  DESTDIR=%{buildroot}

%post libs_%{libver} -p /sbin/ldconfig

%postun libs_%{libver} -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc ChangeLog COPYING README
%{_bindir}/rtmpdump
%{_sbindir}/rtmpgw
%{_sbindir}/rtmpsrv
%{_sbindir}/rtmpsuck
%{_mandir}/man1/rtmpdump.1*
%{_mandir}/man8/rtmpgw.8*

%files libs_%{libver}
%defattr(-,root,root,-)
%{_libdir}/librtmp.so.%{libver}

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_mandir}/man3/*

%changelog
* Sat Aug 20 2016 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 2.4-4
- New upstream release

* Sat Jun 13 2015 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 2.4-3
- Removed dependency on atrpms scripts to comply with ClearOS policy

* Wed May 6 2015 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 2.4-2
- Added buildrequirement atrpms-rpm-config

* Sat May 2 2015 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 2.4-1
- Changed source origin to Git
- Updated to latest release with support for RTMPE version 9

* Mon Mar 14 2011 Axel Thimm <Axel.Thimm@ATrpms.net> - 2.3-1
- Initial build.

