Summary:	ncurses based ACPI monitor for text mode
Summary(pl.UTF-8):	Oparty na ncurses tekstowy monitor ACPI
Name:		yacpi
Version:	3.0.1
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://www.ngolde.de/download/%{name}-%{version}.tar.gz
# Source0-md5:	1b03394ee3b916f686cdc3e2c05ddb7a
Patch0:		%{name}-Makefile.patch
URL:		http://www.ngolde.de/yacpi.html
BuildRequires:	libacpi-devel
BuildRequires:	ncurses-devel
ExclusiveArch:	%{ix86} %{x8664} ia64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
yacpi (Yet Another Configuration and Power Interface) is an ncurses
based ACPI monitoring program for notebooks. There is also a text-only
output so it is possible to include it in scripts. It displays various
ACPI information like battery status, temperature, charging circuits
and AC status. Additionally it displays CPU governor and current
frequency.

%description -l pl.UTF-8
yacpi (Yet Another Configuration and Power Interface, czyli jeszcze
jeden interfejs do konfiguracji i zasilania) to oparty na ncurses
program do monitorowania ACPI dla notebooków. Ma także wyjście
tekstowe, więc nadaje się do używania w skryptach. Wyświetla różne
informacje ACPI, takie jak stan baterii, temperatura, prąd ładowania i
stan zasilania AC. Ponadto wyświetla stan regulacji procesora i jego
aktualną częstotliwość.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	CPPFLAGS="$CPPFLAGS -I/usr/include/ncurses"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix="%{_prefix}"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README THANKS
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
