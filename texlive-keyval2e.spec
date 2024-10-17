Name:		texlive-keyval2e
Version:	23698
Release:	2
Summary:	A lightweight and robust key-value parser
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/keyval2e
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/keyval2e.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/keyval2e.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides lightweight and robust facilities for
creating and managing keys. Its machinery isn't as extensive as
that of, e.g., the ltxkeys package, but it is equally robust;
ease of use and speed of processing are the design aims of the
package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/keyval2e/keyval2e.sty
%doc %{_texmfdistdir}/doc/latex/keyval2e/README
%doc %{_texmfdistdir}/doc/latex/keyval2e/keyval2e-examples.pdf
%doc %{_texmfdistdir}/doc/latex/keyval2e/keyval2e-examples.tex
%doc %{_texmfdistdir}/doc/latex/keyval2e/keyval2e-guide.pdf
%doc %{_texmfdistdir}/doc/latex/keyval2e/keyval2e-guide.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
