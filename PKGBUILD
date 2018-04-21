# Script generated with Bloom
pkgdesc="ROS - ROS driver for the Leap Motion gesture sensor"
url='https://wiki.ros.org/leap_motion'

pkgname='ros-kinetic-leap-motion'
pkgver='0.0.11_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-camera-calibration-parsers'
'ros-kinetic-camera-info-manager'
'ros-kinetic-catkin'
'ros-kinetic-geometry-msgs'
'ros-kinetic-image-transport'
'ros-kinetic-message-generation'
'ros-kinetic-roscpp'
'ros-kinetic-roslib'
'ros-kinetic-rospack'
'ros-kinetic-rospy'
'ros-kinetic-rostest'
'ros-kinetic-std-msgs'
'ros-kinetic-visualization-msgs'
)

depends=('ros-kinetic-camera-calibration-parsers'
'ros-kinetic-camera-info-manager'
'ros-kinetic-geometry-msgs'
'ros-kinetic-image-transport'
'ros-kinetic-message-runtime'
'ros-kinetic-roscpp'
'ros-kinetic-roslib'
'ros-kinetic-rospack'
'ros-kinetic-rospy'
'ros-kinetic-std-msgs'
'ros-kinetic-visualization-msgs'
)

conflicts=()
replaces=()

_dir=leap_motion
source=()
md5sums=()

prepare() {
    cp -R $startdir/leap_motion $srcdir/leap_motion
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

