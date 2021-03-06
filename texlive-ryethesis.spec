# revision 33945
# category Package
# catalog-ctan /macros/latex/contrib/ryethesis
# catalog-date 2014-05-09 11:52:57 +0200
# catalog-license lppl1.3
# catalog-version 1.36
Name:		texlive-ryethesis
Version:	1.36
Release:	6
Summary:	Class for Ryerson Unversity Graduate School requirements
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ryethesis
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ryethesis.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ryethesis.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ryethesis.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The class offers support for formatting a thesis, dissertation
or project according to Ryerson University's School of Graduate
Studies thesis formatting regulations.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ryethesis/ryethesis.cls
%doc %{_texmfdistdir}/doc/latex/ryethesis/Makefile
%doc %{_texmfdistdir}/doc/latex/ryethesis/README
%doc %{_texmfdistdir}/doc/latex/ryethesis/figure1.pdf
%doc %{_texmfdistdir}/doc/latex/ryethesis/ryesample.bib
%doc %{_texmfdistdir}/doc/latex/ryethesis/ryesample.pdf
%doc %{_texmfdistdir}/doc/latex/ryethesis/ryesample.tex
%doc %{_texmfdistdir}/doc/latex/ryethesis/ryethesis.pdf
#- source
%doc %{_texmfdistdir}/source/latex/ryethesis/ryethesis.dtx
%doc %{_texmfdistdir}/source/latex/ryethesis/ryethesis.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
