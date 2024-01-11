# We build libbpf from RHEL kernel sources, that's why we use
# directly kernel tar for RHEL kernel build.
# We update libbpf's 'sources' file with proper hash that's
# used as kernel tar.

# RHEL kernel version-release
%define kver   4.18.0-402
%define source linux-%{kver}.el8

Name:           libbpf
Version:        0.5.0
Release:        1%{?dist}
Summary:        Libbpf library

License:        LGPLv2 or BSD
Source0:        %{source}.tar.xz
BuildRequires:  gcc elfutils-libelf-devel elfutils-devel python3
Conflicts:      bcc < 0.10

%description
A mirror of bpf-next linux tree bpf-next/tools/lib/bpf directory plus its
supporting header files. The version of the package reflects the version of
ABI.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       kernel-headers >= %{kver}

%description devel
The %{name}-devel package contains libraries header files for
developing applications that use %{name}

%package static
Summary: Static library for libbpf development
Requires: %{name}-devel = %{version}-%{release}

%description static
The %{name}-static package contains static library for
developing applications that use %{name}

%global libbpf_make \
  make EXTRA_CFLAGS="${RPM_OPT_FLAGS}" LDFLAGS="%{__global_ldflags}" DESTDIR=%{buildroot} V=1

%prep
%setup -n %{source}

%build
pushd tools/lib/bpf
%{libbpf_make} prefix=%{_prefix}
popd

%install
pushd tools/lib/bpf
%{libbpf_make} prefix=%{_prefix} install_lib install_headers install_pkgconfig
popd

%files
%{_libdir}/libbpf.so.%{version}
%{_libdir}/libbpf.so.0

%files devel
%{_libdir}/libbpf.so
%{_includedir}/bpf
%{_libdir}/pkgconfig/libbpf.pc

%files static
%{_libdir}/libbpf.a

%changelog
* Tue Jun 21 2022 Viktor Malik <vmalik@redhat.com> - 2:0.5.0-1
- kernel update
- Related: rhbz#2097413

* Thu Dec 23 2021 Jiri Olsa <jolsa@redhat.com> - 2:0.4.0-3
- kernel update
- Related: rhbz#2010431

* Tue Nov 16 2021 Jiri Olsa <jolsa@redhat.com> - 2:0.5.0-2
- fix LDFLAGS passing
- Related: rhbz#2023488

* Wed Aug 18 2021 Jiri Olsa <jolsa@redhat.com> - 0.4.0-1
- update [1995111]

* Wed Jul 21 2021 Jiri Olsa <jolsa@redhat.com> - 0.3.0-1
- update [1944754]

* Sun Jun 06 2021 Jiri Olsa <jolsa@redhat.com> - 0.2.0-2
- update [1944754]

* Fri Feb 05 2021 Jiri Olsa <jolsa@redhat.com> - 0.2.0-1
- new kernel version [1919345]

* Fri Jan 22 2021 Jiri Olsa <jolsa@redhat.com> - 0.0.9-1
- new kernel version [1919345]

* Wed Aug 12 2020 Jiri Olsa <jolsa@redhat.com> - 0.0.8-4
- new kernel version [1846820]

* Mon Jul 20 2020 Jiri Olsa <jolsa@redhat.com> - 0.0.8-3
- add Conflicts for bcc < 0.10 [1855816]

* Wed Jul 08 2020 Jiri Olsa <jolsa@redhat.com> - 0.0.8-2
- new kernel version [1846820]

* Fri Jun 26 2020 Jiri Olsa <jolsa@redhat.com> - 0.0.8-1
- new kernel version [1846820]

* Wed Mar 04 2020 Jiri Olsa <jolsa@redhat.com> - 0.0.4-5
- new kernel version [1809913]

* Thu Jan 09 2020 Jiri Olsa <jolsa@redhat.com> - 0.0.4-4
- missing libbpf.pc file [1759154]

* Sun Dec 15 2019 Jiri Olsa <jolsa@redhat.com> - 0.0.4-3
- new kernel version [1759154]

* Tue Dec 10 2019 Jiri Olsa <jolsa@redhat.com> - 0.0.4-2
- new build for gating [1759154]

* Mon Nov 02 2019 Jiri Olsa <jolsa@redhat.com> - 0.0.4-1
- version 0.0.4 [1759154]

* Mon Nov 02 2019 Jiri Olsa <jolsa@redhat.com> - 0.0.2-1
- initial package [1759154]
