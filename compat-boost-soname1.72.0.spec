Name:           compat-boost-soname1.72.0
Version:        1.72.0
Release:        2
License:        BSL-1.0
Summary:        Useful C++ source libraries
Url:            http://www.boost.org/
Group:          base
Source0:        https://dl.bintray.com/boostorg/release/1.72.0/source/boost_1_72_0.tar.bz2
BuildRequires:  bzip2-dev
BuildRequires:  libstdc++-dev
BuildRequires:  python3-dev
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  gmp-dev
BuildRequires:  mpfr-dev
BuildRequires:  icu4c-dev
BuildRequires:  valgrind-dev
%global debug_package %{nil}
Patch1: no-async-pipe-test.patch

%description
Useful C++ source libraries.


%prep
%setup -q -n boost_1_72_0
%patch1 -p1

%build
./bootstrap.sh --prefix=%{buildroot}/usr --libdir=%{buildroot}/usr/lib64 --with-python=python3

# add include path for python headers
sed -i '/using python/ s|^\(.*using python : \([0-9.][0-9.]*\) .*\);$|\1: /usr/include/python\2 ;|' project-config.jam

./b2 %{?_smp_mflags} stage threading=multi link=shared

%install
./b2 %{?_smp_mflags} install threading=multi link=shared

rm -rf %{buildroot}/usr/include/boost
rm -rf %{buildroot}/usr/lib64/cmake
rm -f %{buildroot}/usr/lib64/*.so
rm -f %{buildroot}/usr/lib64/*.so.1
rm -f %{buildroot}/usr/lib64/*.a

%files
/usr/lib64/libboost_atomic.so.1.*
/usr/lib64/libboost_chrono.so.1.*
/usr/lib64/libboost_container.so.1.*
/usr/lib64/libboost_context.so.1.*
/usr/lib64/libboost_contract.so.1.*
/usr/lib64/libboost_coroutine.so.1.*
/usr/lib64/libboost_date_time.so.1.*
/usr/lib64/libboost_fiber.so.1.*
/usr/lib64/libboost_filesystem.so.1.*
/usr/lib64/libboost_graph.so.1.*
/usr/lib64/libboost_iostreams.so.1.*
/usr/lib64/libboost_locale.so.1.*
/usr/lib64/libboost_log.so.1.*
/usr/lib64/libboost_log_setup.so.1.*
/usr/lib64/libboost_math_c99.so.1.*
/usr/lib64/libboost_math_c99f.so.1.*
/usr/lib64/libboost_math_c99l.so.1.*
/usr/lib64/libboost_math_tr1.so.1.*
/usr/lib64/libboost_math_tr1f.so.1.*
/usr/lib64/libboost_math_tr1l.so.1.*
/usr/lib64/libboost_prg_exec_monitor.so.1.*
/usr/lib64/libboost_program_options.so.1.*
/usr/lib64/libboost_python38.so.1.*
/usr/lib64/libboost_random.so.1.*
/usr/lib64/libboost_regex.so.1.*
/usr/lib64/libboost_serialization.so.1.*
/usr/lib64/libboost_stacktrace_addr2line.so.1.*
/usr/lib64/libboost_stacktrace_basic.so.1.*
/usr/lib64/libboost_stacktrace_noop.so.1.*
/usr/lib64/libboost_system.so.1.*
/usr/lib64/libboost_thread.so.1.*
/usr/lib64/libboost_timer.so.1.*
/usr/lib64/libboost_type_erasure.so.1.*
/usr/lib64/libboost_unit_test_framework.so.1.*
/usr/lib64/libboost_wave.so.1.*
/usr/lib64/libboost_wserialization.so.1.*
