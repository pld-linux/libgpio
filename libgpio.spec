%define		snap	20010730
Summary:	GPhoto I/O library
Summary(pl):	Biblbioteka wej¶cia/wyj¶cia GPhoto
Name:		libgpio
Version:	0.0.2
Release:	4.%{snap}
License:	LGPL
Group:		Libraries
Source0:	cvs://:pserver:anonymous@cvs.gphoto.sourceforge.net:/cvsroot/gphoto/%{name}-%{snap}.tar.gz
URL:		http://www.gphoto.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libusb-devel >= 0.1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library which provides uniform interface to access serial, parallel,
USB, IEE1394 devices.

%description -l pl
Biblioteka dostarczaj±ca jednolity interfejs dostêpu do urz±dzeñ
kominikacyjnych np. portów szeregowych i równoleg³ych, USB, IEE1394
itd.

%package devel
Summary:	%{name} library headers
Summary(pl):	Pliki nag³ówkowe biblioteki %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
This is the libraries, include files and other resources you can use
to incorporate %{name} into applications.

%description devel -l pl
Pliki nag³ówkowe oraz dokumentacja pozwalaj±ca na dodawanie obs³ugi
%{name} w swoich programach.

%package static
Summary:	%{name} static libraries
Summary(pl):	Statyczne biblioteki %{name}
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
This is package with static %{name} libraries.

%description static -l pl
Statyczne biblioteki %{name}.

%prep
%setup  -q -n %{name}

%build
libtoolize --copy --force
aclocal
autoheader
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README AUTHORS doc/*sections*

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/gpio
# ONLY one file == library is required (no symlinks or .la libtool files)
%attr(755,root,root) %{_libdir}/gpio/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/*.gz
%attr(755,root,root) %{_bindir}/*-config
%attr(755,root,root) %{_libdir}/gpio*.sh
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/gpio

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
