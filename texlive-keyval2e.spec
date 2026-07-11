%global tl_name keyval2e
%global tl_revision 23698

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.0.2
Release:	%{tl_revision}.1
Summary:	A lightweight and robust key-value parser
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/keyval2e
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/keyval2e.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/keyval2e.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides lightweight and robust facilities for creating and
managing keys. Its machinery isn't as extensive as that of, e.g., the
ltxkeys package, but it is equally robust; ease of use and speed of
processing are the design aims of the package.

