### RPM external pytorch 1.12.1

%define python_cmd python3
%define python_env PYTHON3PATH

##Pytorch Common build files
BuildRequires: git cmake python3 eigen

Source: https://github.com/pytorch/pytorch/releases/download/v%{realversion}/pytorch-v%{realversion}.tar.gz

%prep

%setup -q -n %{n}-v%{realversion}

%build
# cmake flags

pwd
ls
cmake -DCMAKE_USE_GLOG=OFF -DCMAKE_USE_CUDA=OFF -DBUILD_PYTHON=OFF -DBUILD_DOCS=OFF ../%{n}-v%{realversion}

%install
# make
