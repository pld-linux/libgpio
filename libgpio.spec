%define		snap	20010730
Summary:	GPhoto I/O library
Summary(pl.UTF-8):   Biblbioteka wejścia/wyjścia GPhoto
Name:		libgpio
Version:	0.0.2
Release:	6.%{snap}.1
License:	LGPL
Group:		Libraries
# Source0-md5:	d69c918b8a5f6b3188449139124fd1c3
Source0:	http://ep09.pld-linux.org/~djrzulf/%{name}-%{snap}.tar.gz
#Source0:	cvs://:pserver:anonymous@cvs.gphoto.sourceforge.net:/cvsroot/gphoto/%{name}-%{snap}.tar.gz
Patch0:		%{name}-alpha.patch
Patch1:		%{name}-libdir.patch
URL:		http://www.gphoto.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libusb-devel >= 0.1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library which provides uniform interface to access serial, parallel,
USB, IEE1394 devices.

%description -l pl.UTF-8
Biblioteka dostarczająca jednolity interfejs dostępu do urządzeń
komunikacyjnych np. portów szeregowych i równoległych, USB, IEE1394
itd.

%package devel
Summary:	%{name} library headers
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki %{name}
Group:		Development/Libraries
Requires:	libusb-devel >= 0.1.5
Requires:	%{name} = %{version}-%{release}

%description devel
This is the libraries, include files and other resources you can use
to incorporate %{name} into applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe oraz dokumentacja pozwalająca na dodawanie obsługi
%{name} w swoich programach.

%package static
Summary:	Static %{name} libraries
Summary(pl.UTF-8):   Statyczne biblioteki %{name}
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static %{name} libraries.

%description static -l pl.UTF-8
Statyczne biblioteki %{name}.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/gpio/*.{so.?,so,la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README AUTHORS
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/gpio
# ONLY one file == library is required (no symlinks or .la libtool files)
%attr(755,root,root) %{_libdir}/gpio/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/*sections*
%attr(755,root,root) %{_bindir}/*-config
%attr(755,root,root) %{_libdir}/gpio*.sh
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/gpio

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
