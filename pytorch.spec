### RPM external pytorch 1.12.1

%define python_cmd python3
%define python_env PYTHON3PATH

##Pytorch Common build files
BuildRequires: git cmake python3 eigen py3-pip
Requires: py3-astunparse py3-numpy ninja py3-pyyaml py3-setuptools py3-cffi py3-typing_extensions py3-future py3-six py3-requests

Source: https://github.com/pytorch/pytorch/releases/download/v%{realversion}/pytorch-v%{realversion}.tar.gz

%prep

%setup -q -n %{n}-v%{realversion}

%build
# cmake flags

pwd
ls
cmake -DBUILD_SHARED_LIBS:BOOL=ON -DCMAKE_BUILD_TYPE:STRING=Release -DPYTHON_EXECUTABLE:PATH=`which python3` -DCMAKE_INSTALL_PREFIX:PATH=%{n}-v%{realversion} ../%{n}-v%{realversion}
cmake --build . --target install 

%install
# make
