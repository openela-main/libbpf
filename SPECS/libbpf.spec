# We build libbpf from RHEL kernel sources, that's why we use
# directly kernel tar for RHEL kernel build.
# We update libbpf's 'sources' file with proper hash that's
# used as kernel tar.

# RHEL kernel version-release
%define kver   6.12.0-32
%define source linux-%{kver}%{?dist}

Name:           libbpf
Version:        1.5.0
Release:        4%{?dist}
Summary:        Libbpf library

License:        LGPL-2.1-only OR BSD-2-Clause
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
    make prefix=%{_prefix} DESTDIR=%{buildroot} OBJDIR=%{_builddir} CFLAGS="%{build_cflags} -fPIC" LDFLAGS="%{build_ldflags} -Wl,--no-as-needed" LIBDIR=/%{_libdir} NO_PKG_CONFIG=1

%prep
%setup -n %{source}

%build
pushd tools/lib/bpf
%{libbpf_make}

%install
pushd tools/lib/bpf
%{libbpf_make} install

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
* Tue Dec 10 2024 Viktor Malik <vmalik@redhat.com> - 2:1.5.0-4
- Rebuild after kernel rebase to 6.12
- Resolves: RHEL-63890

* Tue Oct 29 2024 Troy Dawson <tdawson@redhat.com> - 2:1.5.0-3
- Bump release for October 2024 mass rebuild:
  Resolves: RHEL-64018

* Wed Sep 25 2024 Viktor Malik <vmalik@redhat.com> - 2:1.5.0-2
- Rebase to released RHEL 10 Beta kernel
- Resolves: RHEL-36077

* Thu Jul 18 2024 Viktor Malik <vmalik@redhat.com> - 2:1.5.0-1
- Rebase to upstream kernel 6.10
- keep FD_CLOEXEC flag when dup()'ing FD
- Resolves: RHEL-37631

* Mon Jun 24 2024 Troy Dawson <tdawson@redhat.com> - 2:1.4.0-3
- Bump release for June 2024 mass rebuild

* Tue May 07 2024 Viktor Malik <vmalik@redhat.com> - 2:1.4.0-1
- Rebuild from latest RHEL 10.0 Beta source tree
- Resolves: RHEL-30627

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Sep 05 2023 Jiri Olsa <olsajiri@gmail.com> - 2:1.2.0-1
- release 1.2.0-1

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Viktor Malik <vmalik@redhat.com> - 2:1.1.0-3
- Migrate license to SPDX

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 22 2022 Jiri Olsa <olsajiri@gmail.com> - 2:1.1.0-1
- release 1.1.0-1

* Tue Dec 20 2022 Jiri Olsa <olsajiri@gmail.com> - 2:1.0.0-4
- CVE-2022-3606 fix

* Tue Nov 01 2022 Jiri Olsa <olsajiri@gmail.com> - 2:1.0.0-3
- release 1.0.0-3

* Sat Sep 03 2022 Jiri Olsa <olsajiri@gmail.com> - 2:1.0.0-1
- release 1.0.0-1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2:0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 18 2022 Jiri Olsa <olsajiri@gmail.com> - 2:0.8.0-1
- release 0.8.0-1

* Fri Feb 18 2022 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2:0.7.0-3
- Re-enable package notes

* Fri Feb 15 2022 Jay W <git.jaydobuleu@gmail.com> - 2:0.7.0-2
- Ensure PREFIX=%{_prefix} INCLUDEDIR=%{_includedir} are set so that flatpak is
  able to build libbpf as dependency.

* Sun Feb 13 2022 Jiri Olsa <jolsa@redhat.com> - 2:0.7.0-1
- release 0.7.0-1

* Tue Feb 08 2022 Jiri Olsa <jolsa@redhat.com> - 2:0.6.1-1
- release 0.6.1-1

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2:0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Sep 10 2021 Jiri Olsa <jolsa@redhat.com> - 2:0.5.0-1
- release 0.5.0-1

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2:0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed May 26 2021 Jiri Olsa <jolsa@redhat.com> - 2:0.4.0-1
- release 0.4.0-1

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
