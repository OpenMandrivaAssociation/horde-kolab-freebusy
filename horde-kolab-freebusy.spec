%define prj Kolab_FreeBusy
%define kolab_webroot %{_var}/www/html/kolab
%define xmldir  %{_var}/lib/pear
%define peardir %(pear config-get php_dir 2> /dev/null)
%define cachedir %{_var}/cache/freebusy

Name:          horde-kolab-freebusy
Version:       0.1.7
Release:       %mkrel 1
Summary:       A package for providing free/busy information
License:       LGPL
Group:         Networking/Mail
Url:           http://pear.horde.org/index.php?package=%{prj}
Source0:       %{prj}-%{version}.tgz
BuildArch:     noarch
Requires(pre): %{_bindir}/pear
Requires:      php-pear
Requires:      horde-framework
Requires:      horde-date
Requires:      horde-icalendar
Requires:      horde-kolab-storage
Requires:      horde-kolab-server
Requires:      php-dba
BuildRequires: horde-framework
BuildRequires: php-pear
BuildRequires: php-pear-channel-horde


%description
This package provides free/busy information for the users of a Kolab server.
A Kolab client changing calendar data in an IMAP folder is required to call
the triggering script provided within this package via HTTP. This will
refresh the cache maintained by this package with partial free/busy data.
This partial data sets are finally combined to the complete free/busy
information once a client requests this data for a particular user.

%prep
%setup -q -n %{prj}-%{version}
cp %{SOURCE0} %{prj}-%{version}.tgz


%build

%install
pear -d www_dir=/var/www/html/kolab/freebusy install --packagingroot %{buildroot} --nodeps --offline %{prj}-%{version}.tgz

%__rm -rf %{buildroot}/%{peardir}/.{filemap,lock,registry,channels,depdb,depdblock}

%__mkdir_p %{buildroot}%{xmldir}
%__cp %{_builddir}/package.xml %{buildroot}%{xmldir}/%{prj}.xml
install -d -m 750 %{buildroot}%{cachedir}

%clean
%__rm -rf %{buildroot}

%post
pear install --nodeps --soft --force --register-only %{xmldir}/%{prj}.xml

%postun
if [ "$1" -eq "0" ]; then
  pear uninstall --nodeps --ignore-errors --register-only pear.horde.org/%{prj}
fi

%files
%defattr(-, root, root)
%{xmldir}/%{prj}.xml
%dir %{peardir}/Horde/Kolab
%dir %{peardir}/Horde/Kolab/FreeBusy
%dir %{peardir}/Horde/Kolab/FreeBusy/Cache
%dir %{peardir}/Horde/Kolab/Test
%dir %{peardir}/docs/Kolab_FreeBusy
%dir %{peardir}/tests/Kolab_FreeBusy
%dir %{peardir}/tests/Kolab_FreeBusy/Horde
%dir %{peardir}/tests/Kolab_FreeBusy/Horde/Kolab
%dir %{peardir}/tests/Kolab_FreeBusy/Horde/Kolab/FreeBusy
%dir /var/www/html/kolab/freebusy
%{peardir}/Horde/Kolab/FreeBusy.php
%{peardir}/Horde/Kolab/FreeBusy/Access.php
%{peardir}/Horde/Kolab/FreeBusy/Cache.php
%{peardir}/Horde/Kolab/FreeBusy/Imap.php
%{peardir}/Horde/Kolab/FreeBusy/View.php
%{peardir}/Horde/Kolab/FreeBusy/Report.php
%{peardir}/Horde/Kolab/FreeBusy/Cache/DB.php
%{peardir}/Horde/Kolab/FreeBusy/Cache/DB/acl.php
%{peardir}/Horde/Kolab/FreeBusy/Cache/DB/xacl.php
%{peardir}/Horde/Kolab/FreeBusy/Cache/File.php
%{peardir}/Horde/Kolab/FreeBusy/Cache/File/acl.php
%{peardir}/Horde/Kolab/FreeBusy/Cache/File/pvcal.php
%{peardir}/Horde/Kolab/FreeBusy/Cache/File/vcal.php
%{peardir}/Horde/Kolab/FreeBusy/Cache/File/xacl.php
%{peardir}/Horde/Kolab/FreeBusy/Cache/Freebusy/Partial.php
%{peardir}/Horde/Kolab/FreeBusy/Cache/Freebusy/Partial/Decorator/Log.php
%{peardir}/Horde/Kolab/FreeBusy/Cache/Freebusy/Partials.php
%{peardir}/Horde/Kolab/FreeBusy/Export/Freebusy/Acl.php
%{peardir}/Horde/Kolab/FreeBusy/Export/Freebusy/Acl/Cache.php
%{peardir}/Horde/Kolab/FreeBusy/Export/Freebusy/Acl/Null.php
%{peardir}/Horde/Kolab/FreeBusy/Export/Freebusy/Combined.php
%{peardir}/Horde/Kolab/FreeBusy/Export/Freebusy/Combined/Decorator/Cache.php
%{peardir}/Horde/Kolab/FreeBusy/Export/Freebusy/Xacl.php
%{peardir}/Horde/Kolab/FreeBusy/Export/Freebusy/Xacl/Cache.php
%{peardir}/Horde/Kolab/FreeBusy/Export/Freebusy/Xacl/Configuration.php
%{peardir}/Horde/Kolab/FreeBusy/Export/Freebusy/Xacl/Decorator/Log.php
%{peardir}/Horde/Kolab/Test/FreeBusy.php
%{peardir}/docs/Kolab_FreeBusy/COPYING
%{peardir}/tests/Kolab_FreeBusy/Horde/Kolab/FreeBusy/AllTests.php
%{peardir}/tests/Kolab_FreeBusy/Horde/Kolab/FreeBusy/FreeBusyTest.php
%{peardir}/tests/Kolab_FreeBusy/Horde/Kolab/FreeBusy/FreeBusyScenarioTest.php
%{peardir}/tests/Kolab_FreeBusy/Horde/Kolab/FreeBusy/Autoload.php
%{peardir}/tests/Kolab_FreeBusy/Horde/Kolab/FreeBusy/Class/CacheTest.php
%{peardir}/tests/Kolab_FreeBusy/Horde/Kolab/FreeBusy/Class/Export/Freebusy/Combined/Decorator/CacheTest.php
%{peardir}/tests/Kolab_FreeBusy/Horde/Kolab/FreeBusy/Class/Export/Freebusy/CombinedTest.php
%{peardir}/tests/Kolab_FreeBusy/Horde/Kolab/FreeBusy/phpunit.xml
%config %{kolab_webroot}/freebusy/config.php
%{kolab_webroot}/freebusy/freebusy.php
%{kolab_webroot}/freebusy/pfb.php
%{kolab_webroot}/freebusy/regenerate.php
%attr(750,root,root) %{cachedir}


%changelog
* Sun Aug 08 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.1.7-1mdv2011.0
+ Revision: 567497
- Updated to version 0.1.7
- added version 0.1.7 source file

* Sat Jul 31 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.1.5-5mdv2011.0
+ Revision: 564069
- Removed Patch0 config.php.diff
- Increased release for rebuild
- removed the accidently added patch
- added the patch
- Updated release to 4
  Corrected the location of the web files
  Added config patch

* Wed May 12 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.1.5-3mdv2010.1
+ Revision: 544545
- changed dependencies from kolab-server and kolab-storage to horde-kolab-server and horde-kolab-storage
  increase rel to 3

* Wed Mar 17 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.1.5-2mdv2010.1
+ Revision: 523083
- replaced Requires(pre): %%{_bindir}/pear with Requires(pre): php-pear
  increased release version

* Sun Feb 28 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.1.5-1mdv2010.1
+ Revision: 512769
- removed BuildRequires: horde-framework
- import horde-kolab-freebusy


