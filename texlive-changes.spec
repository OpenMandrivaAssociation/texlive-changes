# revision 31424
# category Package
# catalog-ctan /macros/latex/contrib/changes
# catalog-date 2013-08-13 17:34:49 +0200
# catalog-license lppl1.3
# catalog-version 2.0.2
Name:		texlive-changes
Version:	2.0.2
Release:	7
Summary:	Manual change markup
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/changes
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/changes.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/changes.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/changes.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows the user to manually markup changes of text,
such as additions, deletions, or replacements. Changed text is
shown in a different colour; deleted text is crossed out. The
package allows definition of additional authors and their
associated colour. It also allows you to define a markup for
authors or annotations. A bash script is provided for removing
the changes.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/changes/changes.sty
%doc %{_texmfdistdir}/doc/latex/changes/README
%doc %{_texmfdistdir}/doc/latex/changes/changes.english.pdf
%doc %{_texmfdistdir}/doc/latex/changes/changes.english.withcode.pdf
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.addedmarkup.bf.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.addedmarkup.dashuline.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.addedmarkup.dotuline.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.addedmarkup.em.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.addedmarkup.it.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.addedmarkup.none.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.addedmarkup.sl.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.addedmarkup.sout.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.addedmarkup.uline.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.addedmarkup.uuline.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.addedmarkup.uwave.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.addedmarkup.wrong.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.addedmarkup.xout.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.authormarkup.brackets.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.authormarkup.footnote.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.authormarkup.none.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.authormarkup.subscript.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.authormarkup.superscript.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.authormarkup.wrong.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.authormarkupposition.left.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.authormarkupposition.right.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.authormarkupposition.wrong.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.authormarkuptext.id.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.authormarkuptext.name.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.authormarkuptext.wrong.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.deletedmarkup.bf.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.deletedmarkup.dashuline.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.deletedmarkup.dotuline.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.deletedmarkup.em.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.deletedmarkup.it.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.deletedmarkup.none.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.deletedmarkup.sl.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.deletedmarkup.sout.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.deletedmarkup.uline.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.deletedmarkup.uuline.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.deletedmarkup.uwave.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.deletedmarkup.wrong.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.deletedmarkup.xout.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.draft.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.final.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.listofchanges.both.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.listofchanges.list.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.listofchanges.summary.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.listofchanges.wrong.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.markup.bfit.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.markup.default.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.markup.nocolor.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.markup.underlined.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.markup.wrong.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.setaddedmarkup.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.setauthormarkup.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.setauthormarkupposition.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.setauthormarkuptext.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.setdeletedmarkup.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.setremarkmarkup.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.setsocextension.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.example.simple.tex
%doc %{_texmfdistdir}/doc/latex/changes/changes.ngerman.pdf
%doc %{_texmfdistdir}/doc/latex/changes/delcmdchanges.bash
%doc %{_texmfdistdir}/doc/latex/changes/userdoc/changes.de.tex
%doc %{_texmfdistdir}/doc/latex/changes/userdoc/changes.en.tex
#- source
%doc %{_texmfdistdir}/source/latex/changes/changes.drv
%doc %{_texmfdistdir}/source/latex/changes/changes.dtx
%doc %{_texmfdistdir}/source/latex/changes/changes.ins
%doc %{_texmfdistdir}/source/latex/changes/examples.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
