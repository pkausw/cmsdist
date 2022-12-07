### RPM external py3-typing_extensions 4.4.0
## INITENV +PATH PYTHON3PATH %{i}/${PYTHON3_LIB_SITE_PACKAGES}

Source: https://github.com/python/typing_extensions/archive/refs/tags/%{realversion}.tar.gz

Requires: python3 py3-setuptools py3-pip

%prep
%setup -n typing_extensions-%{realversion}

%build
# python3 setup.py build
# python3 setup.py egg_info

%install
python3 -m pip install --prefix=%{i} .
# sed -i 's|#!.*python.*|#!/usr/bin/env python3|' \
#  %{i}/${PYTHON3_LIB_SITE_PACKAGES}/setuptools/command/easy_install.py \
#  %{i}/${PYTHON3_LIB_SITE_PACKAGES}/pkg_resources/_vendor/appdirs.py

