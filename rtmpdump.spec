%define commit a107cef9b392616dff54fabfd37f985ee2190a6f
%lib_package rtmp 1

Summary: A toolkit for RTMP streams
Name: rtmpdump
Version: 2.4
Release: 2%{?dist}
License: GPLv2
Group: System Environment/Libraries
URL: http://rtmpdump.mplayerhq.hu/
Source0: https://github.com/mirror/rtmpdump/archive/%{commit}.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: openssl-devel, atrpms-rpm-config

%description
rtmpdump is a toolkit for RTMP streams. All forms of RTMP are
supported, including rtmp://, rtmpt://, rtmpe://, rtmpte://, and
rtmps://.

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

%changelog
* Wed May 6 2015 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 2.4-2
- Added buildrequirement atrpms-rpm-config

* Sat May 2 2015 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 2.4-1
- Changed source origin to Git
- Updated to latest release with support for RTMPE version 9

* Mon Mar 14 2011 Axel Thimm <Axel.Thimm@ATrpms.net> - 2.3-1
- Initial build.

