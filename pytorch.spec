### RPM external pytorch 1.12.1

%define python_cmd python3
%define python_env PYTHON3PATH

##Pytorch Common build files
BuildRequires: git cmake

Source: https://github.com/pytorch/pytorch/archive/refs/tags/v%{realversion}.tar.gz

%prep

%setup -q -n %{n}-%{realversion}

%build
# cmake flags

pwd
ls
cmake ../%{n}-%{realversion}

%install
# make
