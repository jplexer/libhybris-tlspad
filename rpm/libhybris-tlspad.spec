Name:       libhybris-tlspad
Version:    1.0
Release:    1
Summary:    Static TLS padding so libhybris-loaded bionic libraries work in glibc threads
License:    MIT
Source0:    %{name}-%{version}.tar.bz2

%description
libhybris places bionic static TLS of loaded Android libraries (e.g. the Mali
GLES driver) at fixed offsets from the thread pointer, which glibc threads do
not own. Preloading this library reserves a static TLS block directly after
the executable's in every thread. Uses /etc/ld.so.preload so it also applies
to AT_SECURE processes (file capabilities), e.g. lipstick.

%prep
%autosetup -n %{name}-%{version}

%build
gcc %{optflags} -shared -fPIC -Wl,-soname,libhybris-tlspad.so -o libhybris-tlspad.so tlspad.c

%install
install -Dm755 libhybris-tlspad.so %{buildroot}%{_libdir}/libhybris-tlspad.so
mkdir -p %{buildroot}%{_sysconfdir}
echo %{_libdir}/libhybris-tlspad.so > %{buildroot}%{_sysconfdir}/ld.so.preload

%files
%{_libdir}/libhybris-tlspad.so
%config(noreplace) %{_sysconfdir}/ld.so.preload
