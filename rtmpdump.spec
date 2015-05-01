%lib_package rtmp 0

Summary: A toolkit for RTMP streams
Name: rtmpdump
Version: 2.3
Release: 1%{?dist}
License: GPLv2
Group: System Environment/Libraries
URL: http://rtmpdump.mplayerhq.hu/
Source0: http://rtmpdump.mplayerhq.hu/download/rtmpdump-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: openssl-devel

%description
rtmpdump is a toolkit for RTMP streams. All forms of RTMP are
supported, including rtmp://, rtmpt://, rtmpe://, rtmpte://, and
rtmps://.

%prep
%setup -q

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
* Mon Mar 14 2011 Axel Thimm <Axel.Thimm@ATrpms.net> - 2.3-1
- Initial build.

