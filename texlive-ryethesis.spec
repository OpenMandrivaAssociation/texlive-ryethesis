%global tl_name ryethesis
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.36
Release:	%{tl_revision}.1
Summary:	Class for Ryerson University Graduate School requirements
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ryethesis
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ryethesis.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ryethesis.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ryethesis.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The class offers support for formatting a thesis, dissertation or
project according to Ryerson University's School of Graduate Studies
thesis formatting regulations.

