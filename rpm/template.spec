Name:           ros-hydro-leap-motion
Version:        0.0.6
Release:        0%{?dist}
Summary:        ROS leap_motion package

Group:          Development/Libraries
License:        BSD
URL:            https://wiki.ros.org/leap_motion
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-camera-calibration-parsers
Requires:       ros-hydro-camera-info-manager
Requires:       ros-hydro-geometry-msgs
Requires:       ros-hydro-image-transport
Requires:       ros-hydro-message-runtime
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-roslib
Requires:       ros-hydro-rospack
Requires:       ros-hydro-rospy
Requires:       ros-hydro-std-msgs
Requires:       ros-hydro-visualization-msgs
BuildRequires:  ros-hydro-camera-calibration-parsers
BuildRequires:  ros-hydro-camera-info-manager
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-geometry-msgs
BuildRequires:  ros-hydro-image-transport
BuildRequires:  ros-hydro-message-generation
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-roslib
BuildRequires:  ros-hydro-rospack
BuildRequires:  ros-hydro-rospy
BuildRequires:  ros-hydro-std-msgs
BuildRequires:  ros-hydro-visualization-msgs

%description
ROS driver for the Leap Motion gesture sensor

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Tue Nov 18 2014 Florian Lier <flier@techfak.uni-bielefeld.de> - 0.0.6-0
- Autogenerated by Bloom

* Tue Nov 18 2014 Florian Lier <flier@techfak.uni-bielefeld.de> - 0.0.4-1
- Autogenerated by Bloom

