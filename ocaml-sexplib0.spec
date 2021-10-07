#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	Library containing the definition of S-expressions and some base converters
Summary(pl.UTF-8):	Biblioteka z definicjami S-wyrażeń i podstawowych konwerterów
Name:		ocaml-sexplib0
Version:	0.14.0
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/janestreet/sexplib0/releases
Source0:	https://github.com/janestreet/sexplib0/archive/v%{version}/sexplib0-%{version}.tar.gz
# Source0-md5:	dc32962c9596f55db4a607f0536b6f23
URL:		https://github.com/janestreet/sexplib0/
BuildRequires:	ocaml >= 1:4.04.2
BuildRequires:	ocaml-dune >= 2.0.0
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
sexplib0 is a part of Jane Street's Core library. It contains the
definition of S-expressions and some base converters.

This package contains files needed to run bytecode executables using
sexplib0 library.

%description -l pl.UTF-8
sexplib0 to część biblioteki podstawowej Jane Street. Zawiera
definicje S-wyrażeń oraz trochę podstawowych konwerterów.

Ten pakiet zawiera binaria potrzebne do uruchamiania programów
używających biblioteki sexplib0.

%package devel
Summary:	OCaml sexplib0 library - development part
Summary(pl.UTF-8):	Biblioteka OCamla sexplib0 - cześć programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml

%description devel
This package contains files needed to develop OCaml programs using
sexplib0 library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki sexplib0.

%prep
%setup -q -n sexplib0-%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/sexplib0/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/sexplib0

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.md
%dir %{_libdir}/ocaml/sexplib0
%{_libdir}/ocaml/sexplib0/META
%{_libdir}/ocaml/sexplib0/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/sexplib0/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/sexplib0/*.cmi
%{_libdir}/ocaml/sexplib0/*.cmt
%{_libdir}/ocaml/sexplib0/*.cmti
%{_libdir}/ocaml/sexplib0/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/sexplib0/*.a
%{_libdir}/ocaml/sexplib0/*.cmx
%{_libdir}/ocaml/sexplib0/*.cmxa
%endif
%{_libdir}/ocaml/sexplib0/dune-package
%{_libdir}/ocaml/sexplib0/opam
