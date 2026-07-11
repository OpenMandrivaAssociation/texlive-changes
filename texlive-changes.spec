%global tl_name changes
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.2.1
Release:	%{tl_revision}.1
Summary:	Manual change markup
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/changes
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/changes.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/changes.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/changes.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package allows the user to manually markup changes of text, such as
additions, deletions, or replacements. Changed text is shown in a
different color; deleted text is striked out. Additionally, text can be
highlighted and/or commented. The package allows free definition of
additional authors and their associated color. It also allows you to
change the markup of changes, authors, highlights or comments. A Python
script is provided for removing the changes.

