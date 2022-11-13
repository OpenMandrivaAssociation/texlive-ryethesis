Name:		texlive-ryethesis
Version:	33945
Release:	1
Summary:	Class for Ryerson Unversity Graduate School requirements
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ryethesis
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ryethesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ryethesis.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ryethesis.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
