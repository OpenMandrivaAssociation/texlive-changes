# revision 26165
# category Package
# catalog-ctan /macros/latex/contrib/changes
# catalog-date 2012-04-26 11:05:40 +0200
# catalog-license lppl1.3
# catalog-version 1.0.0
Name:		texlive-changes
Version:	1.0.0
Release:	2
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
%{_texmfdistdir}/scripts/changes/delcmdchanges.bash
%{_texmfdistdir}/tex/latex/changes/changes.sty
%doc %{_texmfdistdir}/doc/latex/changes/README
%doc %{_texmfdistdir}/doc/latex/changes/changes.english.pdf
%doc %{_texmfdistdir}/doc/latex/changes/changes.english.withcode.pdf
%doc %{_texmfdistdir}/doc/latex/changes/changes.ngerman.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.addedmarkup.bf.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.addedmarkup.bf.tex
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.addedmarkup.dashuline.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.addedmarkup.dashuline.tex
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.addedmarkup.dotuline.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.addedmarkup.dotuline.tex
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.addedmarkup.em.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.addedmarkup.em.tex
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.addedmarkup.it.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.addedmarkup.it.tex
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.addedmarkup.none.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.addedmarkup.none.tex
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.addedmarkup.sl.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.addedmarkup.sl.tex
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.addedmarkup.sout.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.addedmarkup.sout.tex
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.addedmarkup.uline.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.addedmarkup.uline.tex
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.addedmarkup.uuline.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.addedmarkup.uuline.tex
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.addedmarkup.uwave.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.addedmarkup.uwave.tex
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.addedmarkup.wrong.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.addedmarkup.wrong.tex
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.addedmarkup.xout.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.addedmarkup.xout.tex
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.authormarkup.brackets.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.authormarkup.brackets.tex
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.authormarkup.footnote.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.authormarkup.footnote.tex
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.authormarkup.subscript.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.authormarkup.subscript.tex
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.authormarkup.superscript.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.authormarkup.superscript.tex
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.authormarkup.wrong.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.authormarkup.wrong.tex
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.authormarkupposition.left.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.authormarkupposition.left.tex
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.authormarkupposition.right.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.authormarkupposition.right.tex
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.authormarkupposition.wrong.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.authormarkupposition.wrong.tex
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.authormarkuptext.id.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.authormarkuptext.id.tex
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.authormarkuptext.name.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.authormarkuptext.name.tex
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.authormarkuptext.wrong.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.authormarkuptext.wrong.tex
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.deletedmarkup.bf.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.deletedmarkup.bf.tex
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.deletedmarkup.dashuline.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.deletedmarkup.dashuline.tex
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.deletedmarkup.dotuline.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.deletedmarkup.dotuline.tex
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.deletedmarkup.em.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.deletedmarkup.em.tex
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.deletedmarkup.it.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.deletedmarkup.it.tex
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.deletedmarkup.none.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.deletedmarkup.none.tex
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.deletedmarkup.sl.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.deletedmarkup.sl.tex
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.deletedmarkup.sout.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.deletedmarkup.sout.tex
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.deletedmarkup.uline.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.deletedmarkup.uline.tex
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.deletedmarkup.uuline.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.deletedmarkup.uuline.tex
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.deletedmarkup.uwave.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.deletedmarkup.uwave.tex
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.deletedmarkup.wrong.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.deletedmarkup.wrong.tex
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.deletedmarkup.xout.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.deletedmarkup.xout.tex
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.draft.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.draft.tex
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.final.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.final.tex
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.markup.bfit.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.markup.bfit.tex
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.markup.default.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.markup.default.tex
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.markup.nocolor.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.markup.nocolor.tex
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.markup.underlined.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.markup.underlined.tex
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.markup.wrong.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.markup.wrong.tex
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.setaddedmarkup.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.setaddedmarkup.tex
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.setauthormarkup.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.setauthormarkup.tex
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.setauthormarkupposition.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.setauthormarkupposition.tex
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.setauthormarkuptext.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.setauthormarkuptext.tex
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.setdeletedmarkup.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.setdeletedmarkup.tex
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.setlocextension.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.setlocextension.tex
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.setremarkmarkup.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.setremarkmarkup.tex
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.simple.pdf
%doc %{_texmfdistdir}/doc/latex/changes/examples/changes.example.simple.tex
#- source
%doc %{_texmfdistdir}/source/latex/changes/changes.drv
%doc %{_texmfdistdir}/source/latex/changes/changes.dtx
%doc %{_texmfdistdir}/source/latex/changes/changes.ins
%doc %{_texmfdistdir}/source/latex/changes/examples.dtx
%doc %{_texmfdistdir}/source/latex/changes/userdoc/authors.tex
%doc %{_texmfdistdir}/source/latex/changes/userdoc/changes.de.tex
%doc %{_texmfdistdir}/source/latex/changes/userdoc/changes.en.tex
%doc %{_texmfdistdir}/source/latex/changes/userdoc/command_definechangesauthor.tex
%doc %{_texmfdistdir}/source/latex/changes/userdoc/command_listofchanges.tex
%doc %{_texmfdistdir}/source/latex/changes/userdoc/command_setaddedmarkup.tex
%doc %{_texmfdistdir}/source/latex/changes/userdoc/command_setauthormarkup.tex
%doc %{_texmfdistdir}/source/latex/changes/userdoc/command_setauthormarkupposition.tex
%doc %{_texmfdistdir}/source/latex/changes/userdoc/command_setauthormarkuptext.tex
%doc %{_texmfdistdir}/source/latex/changes/userdoc/command_setdeletedmarkup.tex
%doc %{_texmfdistdir}/source/latex/changes/userdoc/command_setlocextension.tex
%doc %{_texmfdistdir}/source/latex/changes/userdoc/command_setremarkmarkup.tex
%doc %{_texmfdistdir}/source/latex/changes/userdoc/copyright.tex
%doc %{_texmfdistdir}/source/latex/changes/userdoc/email.tex
%doc %{_texmfdistdir}/source/latex/changes/userdoc/files_generated.tex
%doc %{_texmfdistdir}/source/latex/changes/userdoc/files_original.tex
%doc %{_texmfdistdir}/source/latex/changes/userdoc/option_addedmarkup.tex
%doc %{_texmfdistdir}/source/latex/changes/userdoc/option_authormarkup.tex
%doc %{_texmfdistdir}/source/latex/changes/userdoc/option_authormarkupposition.tex
%doc %{_texmfdistdir}/source/latex/changes/userdoc/option_authormarkuptext.tex
%doc %{_texmfdistdir}/source/latex/changes/userdoc/option_deletedmarkup.tex
%doc %{_texmfdistdir}/source/latex/changes/userdoc/option_draft.tex
%doc %{_texmfdistdir}/source/latex/changes/userdoc/option_final.tex
%doc %{_texmfdistdir}/source/latex/changes/userdoc/option_markup.tex
%doc %{_texmfdistdir}/source/latex/changes/userdoc/option_ulem.tex
%doc %{_texmfdistdir}/source/latex/changes/userdoc/option_xcolor.tex
%doc %{_texmfdistdir}/source/latex/changes/userdoc/path_examples.tex
%doc %{_texmfdistdir}/source/latex/changes/userdoc/path_scripts.tex
%doc %{_texmfdistdir}/source/latex/changes/userdoc/url.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar scripts tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Mon Jun 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0.0-1
+ Revision: 804510
- Update to latest release.

* Thu Jan 19 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.6.0-1
+ Revision: 762535
- Update to latest upstream package

* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.5.4-2
+ Revision: 750100
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.5.4-1
+ Revision: 718032
- texlive-changes
- texlive-changes
- texlive-changes
- texlive-changes
- texlive-changes

