%define		snap	20010730
Summary:	GPhoto I/O library
Summary(pl):	Biblbioteka wej∂cia/wyj∂cia GPhoto
Name:		libgpio
Version:	0.0.2
Release:	2.%{snap}
License:	LGPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
Source0:	cvs://:pserver:anonymous@cvs.gphoto.sourceforge.net:/cvsroot/gphoto/%{name}-%{snap}.tar.gz
URL:		http://www.gphoto.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libusb-devel >= 0.1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library which provides uniform interface to access serial, parallel,
USB, IEE1394 devices.

%description -l pl
Biblioteka dostarczaj±ca jednolity interfejs dostÍpu do urz±dzeÒ
kominikacyjnych np. portÛw szeregowych i rÛwnoleg≥ych, USB, IEE1394
itd.

%package devel
Summary:	%{name} library headers
Summary(pl):	Pliki nag≥Ûwkowe biblioteki %{name}
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description devel
This is the libraries, include files and other resources you can use
to incorporate %{name} into applications.

%description -l pl devel
Pliki nag≥Ûwkowe oraz dokumentacja pozwalaj±ca na dodawanie obs≥ugi
%{name} w swoich programach.

%package static
Summary:	%{name} static libraries
Summary(pl):	Statyczne biblioteki %{name}
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description static
This is package with static %{name} libraries.

%description -l pl static
Statyczne biblioteki %{name}.

%prep
%setup  -q -n %{name}

%build
libtoolize --copy --force
aclocal
autoheader
autoconf
automake -a -c
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
