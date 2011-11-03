# revision 23698
# category Package
# catalog-ctan /macros/latex/contrib/keyval2e
# catalog-date 2011-08-26 11:26:23 +0200
# catalog-license lppl1.3
# catalog-version 0.0.2
Name:		texlive-keyval2e
Version:	0.0.2
Release:	1
Summary:	A lightweight and robust key-value parser
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/keyval2e
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/keyval2e.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/keyval2e.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides lightweight and robust facilities for
creating and managing keys. Its machinery isn't as extensive as
that of, e.g., the ltxkeys package, but it is equally robust;
ease of use and speed of processing are the design aims of the
package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/keyval2e/keyval2e.sty
%doc %{_texmfdistdir}/doc/latex/keyval2e/README
%doc %{_texmfdistdir}/doc/latex/keyval2e/keyval2e-examples.pdf
%doc %{_texmfdistdir}/doc/latex/keyval2e/keyval2e-examples.tex
%doc %{_texmfdistdir}/doc/latex/keyval2e/keyval2e-guide.pdf
%doc %{_texmfdistdir}/doc/latex/keyval2e/keyval2e-guide.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
