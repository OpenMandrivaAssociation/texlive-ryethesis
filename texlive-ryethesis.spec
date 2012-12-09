# revision 21316
# category Package
# catalog-ctan /macros/latex/contrib/ryethesis
# catalog-date 2011-02-05 10:59:30 +0100
# catalog-license lppl1.3
# catalog-version 1.3
Name:		texlive-ryethesis
Version:	1.3
Release:	2
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

%define		_unpackaged_subdirs_terminate_build	0

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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.3-2
+ Revision: 756075
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.3-1
+ Revision: 719476
- texlive-ryethesis
- texlive-ryethesis
- texlive-ryethesis
- texlive-ryethesis

