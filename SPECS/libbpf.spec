# We build libbpf from RHEL kernel sources, that's why we use
# directly kernel tar for RHEL kernel build.
# We update libbpf's 'sources' file with proper hash that's
# used as kernel tar.

# RHEL kernel version-release
%define kver   5.14.0-333
%define source linux-%{kver}.el9

Name:           libbpf
Version:        1.2.0
Release:        1%{?dist}
Summary:        Libbpf library

License:        LGPLv2 or BSD
Source0:        %{source}.tar.xz
BuildRequires:  gcc elfutils-libelf-devel elfutils-devel python3
BuildRequires: make

# This package supersedes libbpf from kernel-tools,
# which has default Epoch: 0. By having Epoch: > 0
# this libbpf will take over smoothly
Epoch:          2

%description
A mirror of bpf-next linux tree bpf-next/tools/lib/bpf directory plus its
supporting header files. The version of the package reflects the version of
ABI.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = 2:%{version}-%{release}
Requires:       kernel-headers >= %{kver}
Requires:       zlib

%description devel
The %{name}-devel package contains libraries header files for
developing applications that use %{name}

%package static
Summary: Static library for libbpf development
Requires: %{name}-devel = 2:%{version}-%{release}

%description static
The %{name}-static package contains static library for
developing applications that use %{name}

%global libbpf_make \
  make DESTDIR=%{buildroot} OBJDIR=%{_builddir} CFLAGS="%{build_cflags} -fPIC" LDFLAGS="%{build_ldflags} -Wl,--no-as-needed" LIBDIR=/%{_libdir} NO_PKG_CONFIG=1

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
%{_libdir}/libbpf.so.1

%files devel
%{_libdir}/libbpf.so
%{_includedir}/bpf/
%{_libdir}/pkgconfig/libbpf.pc

%files static
%{_libdir}/libbpf.a

%changelog
* Mon Jul 03 2023 Viktor Malik <vmalik@redhat.com> - 1.2.0-1
- Update to BPF 6.3 rebase
- Resolves: rhbz#2178933

* Tue May 16 2023 Viktor Malik <vmalik@redhat.com> - 1.1.0-2
- Update to BPF 6.2 rebase
- Resolves: rhbz#2178932

* Thu Mar 30 2023 Viktor Malik <vmalik@redhat.com> - 2:1.1.0-1
- Update to BPF 6.1 rebase
- Resolves: rhbz#2178931

* Thu Jan 19 2023 Viktor Malik <vmalik@redhat.com> - 2:1.0.0-2
- Update to BPF 6.0 rebase
- Resolves: rhbz#2159763

* Mon Jan 02 2023 Viktor Malik <vmalik@redhat.com> - 2:1.0.0-1
- Update to 1.0.0 (BPF 5.19 rebase)
- Resolves: rhbz#2157592

* Tue Dec 13 2022 Viktor Malik <vmalik@redhat.com> - 2:0.8.0-1
- Update to 0.8.0 (BPF 5.18 rebase)
- Resolves: rhbz#2149243

* Fri Jun 24 2022 Viktor Malik <vmalik@redhat.com> - 2:0.6.0-1
- Update to 0.6.0 (BPF 5.16 rebase)
- Related: rhbz#2010428
- Enable LTO
- Related: rhbz#1990029

* Wed Feb 23 2022 Viktor Malik <vmalik@redhat.com> - 2:0.5.0-4
- Backport fix for netlink operations on ppc
- Related: rhbz#2057476

* Tue Nov 09 2021 Jiri Olsa <jolsa@redhat.com> - 2:0.5.0-3
- pull new kernel sources with fixes
- Related: rhbz#2006305

* Fri Oct 11 2021 Jiri Olsa <jolsa@redhat.com> - 2:0.5.0-2
- Fix passing of system's CFLAGS/LDFLAGS
- Related: rhbz#2012774

* Fri Oct 1 2021 Jiri Olsa <jolsa@redhat.com> - 2:0.5.0-1
- update to RHEL spec
- Related: rhbz#2009725

* Wed Aug 25 2021 Jiri Olsa <jolsa@redhat.com> - 2:0.4.0-1
- updated to 0.4.0
  Related: rhbz#1997597

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 2:0.3.0-4
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 2:0.3.0-3
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2:0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jiri Olsa <jolsa@redhat.com> - 2:0.3.0-1
- release 0.3.0-1

* Thu Oct 01 2020 Jiri Olsa <jolsa@redhat.com> - 2:0.1.0-1
- release 0.1.0

* Sun Aug 02 2020 Jiri Olsa <jolsa@redhat.com> - 2:0.0.9-1
- release 0.0.9

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2:0.0.8-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2:0.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 10 2020 Jiri Olsa <jolsa@redhat.com> - 2:0.0.8-1
- release 0.0.8

* Wed Mar 03 2020 Jiri Olsa <jolsa@redhat.com> - 2:0.0.7-1
- release 0.0.7

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2:0.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 2 2020 Jiri Olsa <jolsa@redhat.com> - 0.0.6-2
- release 0.0.6-2, build server issues

* Mon Dec 30 2019 Jiri Olsa <jolsa@redhat.com> - 0.0.6-1
- release 0.0.6

* Thu Nov 28 2019 Jiri Olsa <jolsa@redhat.com> - 0.0.5-3
- release 0.0.5

* Fri Nov 22 2019 Jiri Olsa <jolsa@redhat.com> - 0.0.3-3
- Revert to 0.0.3 version and adjust kernel-headers dependency (BZ#1755317)

* Tue Nov 12 2019 Jiri Olsa <jolsa@redhat.com> - 0.0.5-2
- Add kernel-headers dependency

* Thu Oct 03 2019 Jiri Olsa <jolsa@redhat.com> - 0.0.5-1
- release 0.0.5

* Wed Sep 25 2019 Jiri Olsa <jolsa@redhat.com> - 0.0.3-2
- Fix libelf linking (BZ#1755317)

* Fri Sep 13 2019 Jiri Olsa <jolsa@redhat.com> - 0.0.3-1
- Initial release
